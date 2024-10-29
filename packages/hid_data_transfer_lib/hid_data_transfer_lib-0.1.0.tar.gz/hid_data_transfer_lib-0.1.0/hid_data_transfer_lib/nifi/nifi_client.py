"""
Copyright 2024 Eviden
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an 'AS IS' BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


This module defines the NIFI API client class.
It provides methods to interface the NIFI server to in instantiate templates,
and run processors in a process group.
"""

import glob
import json
import os
import sys
import uuid
from enum import Enum
from time import sleep
from typing import Optional

from hid_data_transfer_lib.conf.hid_dt_configuration import (
    HidDataTransferConfiguration
)
from hid_data_transfer_lib.exceptions.hid_dt_exceptions import (
    HidDataTransferException
)
from hid_data_transfer_lib.keycloak.keycloak_rest import KeycloakRESTClient
from hid_data_transfer_lib.nifi.nifi_rest import NIFIRESTClient
from hid_data_transfer_lib.util.util import (
    order_process_group, sftp_get, sftp_put,
    ssh_create_folder, ssh_delete_file, ssh_delete_folder,
    ssh_list
)


# Helper enums
# An enum describing the types of processor exectution, either once or forever
class ExecutionType(Enum):
    """An enum describing the types of processor exectution,
    either once or forever"""

    ONCE = "once"
    FOREVER = "forever"


class NIFIClient:
    """main NIFI API client class
    contains methods to interact with the remote NIFI
    (taken from configuration)
    """

    # Requests constants
    __CHECK_STATUS_SLEEP_LAPSE = 10

    # Commands parameters
    HPC_HOST = "hpc.host"
    HPC_PORT = "hpc.port"
    HPC_USERNAME = "hpc.username"
    HPC_PASSWORD_PROPERTY = "Password"
    HPC_SECRET_KEY_PATH = "hpc.secret_key_path"
    HPC_SECRET_KEY_PATH_PASSWORD_PROPERTY = "Private Key Passphrase"
    CKAN_HOST = "ckan.host"
    CKAN_APIKEY_PROPERTY = "Api_Key"
    CKAN_ORGANIZATION = "ckan.organization"
    CKAN_PACKAGE = "ckan.package"
    CKAN_RESOURCE = "ckan.resource"

    def __init__(self, conf: HidDataTransferConfiguration,
                 secure: bool = False) -> None:
        """constructs a NIFI client,
        with the NIFI endpoint taken from configuration
        """
        self.__conf = conf
        self.nifi_rest_client = NIFIRESTClient(conf, secure)
        self.keycloak_rest_client = KeycloakRESTClient(
            conf, secure, refresh=True)
        self.__logger = self.__conf.logger("nifi.v2.client")

    def get_access_token(self) -> str:
        """gets the NIFI access token,
        using NIFI account taken from configuration
        this access token is required for any further request sent to NIFI
        """
        if self.__conf.nifi_login() and self.__conf.nifi_passwd():
            return self.nifi_rest_client.get_access_token()
        elif self.__conf.keycloak_login() and self.__conf.keycloak_passwd():
            return self.keycloak_rest_client.get_token()
        else:
            raise HidDataTransferException(
                "NIFI or Keycloak login and password must be provided"
            )

    def set_access_token(self, keycloak_token):
        """sets the given JWT token for getting access to NIFI"""
        self.keycloak_rest_client.set_token(
            user=keycloak_token["username"],
            token=keycloak_token["token"],
            expires_in=keycloak_token["expires_in"],
            refresh_token=keycloak_token["refresh_token"],
        )
        return keycloak_token["token"]

    def cancel_access_token(self):
        """cancel the access token refresh timer in case of Keycloak"""
        if self.__conf.keycloak_login() and self.__conf.keycloak_passwd():
            self.keycloak_rest_client.cancel_token()

    # GET requests

    def get_process_group(self, group_id, token) -> dict:
        """gets a process group identified by id"""
        return self.nifi_rest_client.process_group_get_request(group_id, token)

    def get_process_group_processors(self, group_id, token) -> dict:
        """gets the processors of a process group identified by id"""
        return self.nifi_rest_client.process_group_get_request(
            group_id, token, "processors"
        )

    def get_process_group_connections(self, group_id, token) -> dict:
        """gets the connetions of a process group identified by id"""
        return self.nifi_rest_client.process_group_get_request(
            group_id, token, "connections"
        )

    def get_processors_sequence(self, group_id, token) -> list:
        """computes the sequence of processors of a process group
        identified by id"""
        connections = self.get_process_group_connections(group_id, token)
        connections_pairs = []
        for connection in connections["connections"]:
            connections_pairs.append(
                [connection["sourceId"], connection["destinationId"]]
            )
        return order_process_group(connections_pairs)

    def get_processor_error_bulletins(self, processor_id, token):
        """Get the error bulletins of a processor identified by id"""
        # Retrieve current version of processor
        processor = self.nifi_rest_client.get_processor(processor_id, token)
        error_bulletins = []
        bulletins = processor["bulletins"]
        for _bulletin in bulletins:
            bulletin = _bulletin["bulletin"]
            if bulletin["level"] == "ERROR":
                error_bulletins.append(bulletin)
        return error_bulletins

    # POST requests

    # PUT requests

    def update_parameters(self, parameter_context, arguments, token) -> bool:
        """updates the parameters of a parameter context
        arguments contains the parameters to inject in the context
        """
        parameters = parameter_context["component"]["parameters"]
        for _, (key, value) in enumerate(arguments.items()):
            self.add_parameter(parameters, key, value)

        parameter_context["component"]["parameters"] = parameters
        modified_parameter_context_json = json.dumps(parameter_context)
        return self.nifi_rest_client.save_parameter_context(
            modified_parameter_context_json, parameter_context["id"], token
        )

    def update_processor_property(
        self, processor, property_name, property_value
    ):
        """updates the property of a processor"""
        processor["component"]["config"]["properties"][property_name] = \
            property_value

    # DELETE requests

    # MULTI-REQUESTS methods

    def run_processor(self, execution_type, token, processor):
        """run a processor once or forever depending on the execution type"""
        ok, response = None, None
        processor_name = processor["component"]["name"]
        if execution_type[processor_name] == ExecutionType.ONCE:
            ok, response = self._run_processor_once(processor, token)
        elif execution_type[processor_name] == ExecutionType.FOREVER:
            ok, response = self._run_processor_forever(processor, token)
        else:
            raise HidDataTransferException(
                f"Incompatible execution type {execution_type[processor_name]}"
                f" for processor {processor_name}"
            )

        return ok, response

    def _run_processor_once(self, processor, token) -> tuple[bool, str]:
        """run once a given processor"""
        return self.nifi_rest_client.change_processor_run_status(
            processor, token, "RUN_ONCE"
        )

    def _run_processor_forever(self, processor, token) -> tuple[bool, str]:
        """run a given processor until it is stopped"""
        return self.nifi_rest_client.change_processor_run_status(
            processor, token, "RUNNING"
        )

    def stop_processor(self, processor, token) -> tuple[bool, str]:
        """stop a given processor"""
        return self.nifi_rest_client.change_processor_run_status(
            processor, token, "STOPPED"
        )

    def are_all_processor_queued_flowfiles_consumed(
        self, processor, process_group_id, token
    ) -> bool:
        """Check if all queued flowfiles have been consumed by the processor"""
        # Get the process group connections
        connections = self.get_process_group_connections(
            process_group_id, token)[
            "connections"
        ]
        for connection in connections:
            if connection["component"]["destination"]["id"] == processor["id"]:
                if connection["status"]["aggregateSnapshot"][
                    "flowFilesQueued"
                ] == 0:
                    return True
                else:
                    return False
        raise HidDataTransferException(
            f"Incomming connection not found for processor {processor['id']}"
        )

    def are_expected_outgoing_flowfiles_created(
        self,
        processor,
        process_group_id,
        expected_outgoing_flowfiles,
        token,
    ) -> bool:
        """Check if all expected outgoing flowfiles
        have been generated by the processor"""
        # Get the process group connections
        connections = self.get_process_group_connections(
            process_group_id, token)[
            "connections"
        ]
        for connection in connections:
            if connection["component"]["source"]["id"] == processor["id"]:
                return (
                    connection["status"]["aggregateSnapshot"][
                        "flowFilesQueued"
                    ] == expected_outgoing_flowfiles
                )
        raise HidDataTransferException(
            f"Incomming connection not found for processor {processor['id']}"
        )

    def has_created_outgoing_flowfiles(
        self,
        processor,
        process_group_id,
        token,
    ) -> bool:
        """Check if at least one outgoing flowfile
        has been generated by the processor"""
        # Get the process group connections
        connections = self.get_process_group_connections(
            process_group_id, token)[
            "connections"
        ]
        for connection in connections:
            if connection["component"]["source"]["id"] == processor["id"]:
                return connection["status"]["aggregateSnapshot"][
                    "flowFilesQueued"
                ] > 0
        raise HidDataTransferException(
            f"Incomming connection not found for processor {processor['id']}"
        )

    # Class helper methods

    def upload_keys(self, keys, process_group_id) -> dict:
        """upload keys into the NIFI server by using the user's access"""
        remote_keys = {}
        for key, value in keys.items():
            remote_keys[key] = self.upload_key(value, process_group_id)
        return remote_keys

    def set_key_arguments(self, arguments, remote_keys):
        """updates the key-type argument entries with the keys paths
        on the remote NIFI server
        """
        for key, _ in remote_keys.items():
            arguments[key] = remote_keys[key]

    def add_parameter(self, parameters, key, value):
        """add a parameter (k, v) to a dictionary of parameters"""
        parameters.append({"parameter": {"name": key, "value": value}})
        return parameters

    def order_processors(self, processors, processors_sequence):
        """order the processors list according to the sequence given"""
        ordered_processors = []
        for identifier in processors_sequence:
            found = self.find_processor_by_id(processors, identifier)
            if found:
                ordered_processors.append(found)
        return ordered_processors

    def find_processor_by_id(self, processors, identifier):
        """finds a processor identified by id
        in the given list of processors"""
        for processor in processors:
            if processor["id"] == identifier:
                return processor
        return None

    def find_flow_definition_by_name(self, flow_definition_name, token):
        """Find a flow definition, registered in the NIFI Registry, by name"""
        # Assuming there is only one registered Registry
        registries = self.nifi_rest_client.get_registries(token)
        assert registries is not None
        registry_id = registries["registries"][0]["id"]

        # Assuming there is only one registered Bucket
        buckets = self.nifi_rest_client.get_buckets(registry_id, token)
        assert buckets is not None
        bucket_id = buckets["buckets"][0]["id"]

        flow_definitions = self.nifi_rest_client.get_flow_definitions(
            registry_id, bucket_id, token
        )
        assert flow_definitions is not None
        flow_definition_id = None
        for flow in flow_definitions["versionedFlows"]:
            if (
                flow["versionedFlow"]["flowName"].upper()
                == flow_definition_name.upper()
            ):
                flow_definition_id = flow["versionedFlow"]["flowId"]
                break

        if flow_definition_id is None:
            raise HidDataTransferException(
                f"Flow definition {flow_definition_name} not found"
            )

        versions = self.nifi_rest_client.get_flow_definition_versions(
            registry_id, bucket_id, flow_definition_id, token
        )
        assert versions is not None
        version = versions["versionedFlowSnapshotMetadataSet"][0][
            "versionedFlowSnapshotMetadata"
        ]["version"]

        return {
            "registry_id": registry_id,
            "bucket_id": bucket_id,
            "flow_definition_id": flow_definition_id,
            "version": version,
        }

    def instantiate_process_group(
        self, token, flow_definition_name, arguments, keys_arguments
    ):
        """create a process group from a template
        and its associated parameter context"""
        try:
            # Get flow definition metadata by name
            flow_definition = self.find_flow_definition_by_name(
                flow_definition_name, token
            )

            # Instantiate flow definition as process group
            process_group = (
                self.nifi_rest_client.instantiate_flow_definition_as_process_group(
                    flow_definition["registry_id"],
                    flow_definition["bucket_id"],
                    flow_definition["flow_definition_id"],
                    flow_definition["version"],
                    token,
                )
            )

            # Transfer keys to NIFI server
            if keys_arguments:
                remote_keys = \
                    self.upload_keys(keys_arguments, process_group["id"])
                self.set_key_arguments(
                    arguments, remote_keys
                )  # update arguments with locations of remote keys

            # Instantiate parameter context with parameters
            parameter_context = \
                self.nifi_rest_client.instantiate_parameter_context(
                    token
                )

            # Update parameters
            ok = self.update_parameters(parameter_context, arguments, token)

            if not ok:
                raise HidDataTransferException(
                    f"Exception updating parameter context "
                    f"{parameter_context['id']}"
                )

            # Associate parameter context to process group
            self.nifi_rest_client.associate_parameter_context_to_group(
                parameter_context, process_group, token
            )

            return process_group
        except Exception as ex:
            dtex = HidDataTransferException(ex)
            dtex.set_produced_object(process_group)
            raise dtex from ex

    def run_process_group(
        self,
        template_name,
        execution_type: dict,
        arguments,
        keys_arguments: Optional[dict] = None,
        sensitive_parameters: Optional[dict] = None,
        first_processor_expected_outgoing_flowfiles=None,
        keycloak_token=None,
    ) -> str:
        """MAIN method to run a processor from a template identify by name
        The procedure is as follows:
        - The template is retrieved by name
        - A process group is created from the template
        - A parameter context is created
        - Parameters defined in  arguments are injected in the context
        - The context is associated to the process group
        - For each processor in the group, following the sequence flow,
          the processor is executed once or until it processes all pending
          flowfiles in ingoing connection queue.
          Following processor is executed
          after the termination of the previous one.
        """
        # Manage HPC secret keys
        # Secret key should be read from client side
        # (provided in secret_key_path as local path)
        # Then, transfer to NIFI server in volume
        # (remote path) mounted by NIFI image
        # Using the user account to NIFI server (ssh) to send the key by scp
        # So, this CLI method should read local private_key,
        # transfer the key to a NIFI server folder
        # with read permissions for NIFI account
        # Next, the key remote path is update in parameter private_key_path
        # sent to the NIFI server
        # Upon transfer completion, this key must be automatically removed
        # by this NIFI CLI
        # NOTE: place the key in remote NIFI server upload location,
        # with permissions for user rw only
        # where only the user and NIFI have access but no other users
        # PROCEDURE:
        # - Get user NIFI account from configuration (username, key_path)
        # - Get NIFI upload folder from configuration (e.g. /opt/nifi-data/)
        # - This folder (and root) should have nifi:nifi ownership
        # when mounted in NIFI container
        # - Transfer local key to upload folder in NIFI server
        # - Update private_key_path with remote key path
        # - once this process group ends remote the uploaded key

        # Uses execution_type attribute to determine whether each processor
        # in the group should be executed only once or forever
        # until all incoming flowfiles are consumed
        process_group = {}
        try:
            # Get access token, do not forget to cancel token refresh
            # when done with it
            if keycloak_token:
                token = self.set_access_token(keycloak_token)
            else:
                token = self.get_access_token()

            process_group = self.instantiate_process_group(
                token, template_name, arguments, keys_arguments
            )
            self.__logger.info(
                "Process group %s created\n", process_group["id"])

            # Get all processors in the process group
            processors = self.get_process_group_processors(
                process_group["id"], token)[
                    "processors"
                ]

            # For each processor in group ordered by the sequence,
            # execute processor once
            # Check previous processor has an running instance
            # before launching next one
            processors_sequence = self.get_processors_sequence(
                process_group["id"], token
            )
            processors = self.order_processors(processors, processors_sequence)
            index_processor = 0

            sys.stdout.write(
                f"{template_name} data transfer with id"
                f": {process_group['id']} initiated\n"
            )

            for processor in processors:
                # Set sensitive hpc parameters
                processor = self.set_sensitive_parameters(
                    sensitive_parameters, token, processor
                )

                # Run the processor once or forever
                # until all incoming flowfiles are consumed
                processor_name = processor["component"]["name"]
                ok, response = self.run_processor(
                    execution_type, token, processor)
                index_processor += 1
                if ok:
                    self.wait_for_processor_completion(
                        execution_type,
                        token,
                        index_processor,
                        len(processors),
                        processor,
                        process_group["id"],
                        first_processor_expected_outgoing_flowfiles,
                    )
                    self.__logger.debug(
                        "Processor %s execution completed\n", processor_name
                    )
                else:
                    raise HidDataTransferException(
                        f'Exception running processor {processor["id"]}'
                        f" for group {template_name}"
                        f" with message: {response}"
                    )
            sys.stdout.write(
                f"{template_name} data transfer with id"
                f": {process_group['id']} terminated\n"
            )

            return process_group["id"]
            # Process group and associate parameter context cannot be removed
            # until the process group ends its execution
            # A CLI method: cleanup available to remove them
            # given the process group id
        except Exception as ex:
            if process_group and "id" in process_group:
                raise HidDataTransferException(ex, process_group["id"]) from ex
            else:
                raise HidDataTransferException(ex) from ex
        finally:
            self.cancel_access_token()
            if process_group:
                # Clean up the process group and associated parameter context
                self.clean_process_group_up(process_group["id"], token)
                self.__logger.info("Process group %s cleaned up\n",
                                   process_group["id"])

    def set_sensitive_parameters(self, sensitive_parameters, token, processor):
        """Set sensitive parameters for a processor"""
        processor_name = processor["component"]["name"]
        if sensitive_parameters and processor_name in sensitive_parameters:
            for key in sensitive_parameters[processor_name]:
                self.update_processor_property(
                    processor,
                    key,
                    sensitive_parameters[processor_name][key],
                )
            processor = self.nifi_rest_client.update_processor(
                processor, token)
        return processor

    def wait_for_processor_completion(
        self,
        execution_type,
        token,
        index_processor,
        num_processors,
        processor,
        process_group_id,
        first_processor_expected_outgoing_flowfiles=None,
    ):
        """Wait for processor to complete its execution"""

        are_all_flowfiles_consumed = False
        status = "RUNNING"
        processor_name = processor["component"]["name"]
        while status != "STOPPED" and not are_all_flowfiles_consumed:
            # Check processor has consumed all queued flowfiles
            # First processor does not have incoming connections
            if index_processor != 1:
                are_all_flowfiles_consumed = (
                    self.are_all_processor_queued_flowfiles_consumed(
                        processor, process_group_id, token
                    )
                )
            else:
                # First processor does not have incoming connections
                # But it is expected to produce outcoming flowfiles
                # Mark are_all_flowfiles_consumed as True
                # when first processor has been executed FOREVER
                # and it has created all expected outcoming flowfiles
                if execution_type[processor_name] == ExecutionType.FOREVER:
                    are_all_flowfiles_consumed = (
                        self.are_expected_outgoing_flowfiles_created(
                            processor,
                            process_group_id,
                            first_processor_expected_outgoing_flowfiles,
                            token,
                        )
                    )
            status = self.nifi_rest_client.get_processor_state(
                processor, token)
            # If processor is stopped and not the last one,
            # check it has produced at least one flowfile
            if (
                status == "STOPPED"
                and index_processor != num_processors
                and not self.has_created_outgoing_flowfiles(
                    processor, process_group_id, token
                )
            ):
                raise HidDataTransferException(
                    f"Processor {processor_name} "
                    "has not produced outcoming flowfiles"
                )
            # Check if processor execution has failed with exception
            # Collect them all and raise a single exception
            error_bulletins = self.get_processor_error_bulletins(
                processor["id"], token)
            if error_bulletins:
                raise HidDataTransferException(
                    f"Processor {processor_name} has failed with exception: "
                    f"{error_bulletins}"
                )
            sleep(self.__CHECK_STATUS_SLEEP_LAPSE)

        # If processor has executed for ever, stop it
        if execution_type[processor_name] == ExecutionType.FOREVER:
            # Get current processor version
            processor = self.nifi_rest_client.get_processor(
                processor["id"], token)
            self.stop_processor(processor, token)

    def add_default_hpc_parameters(self, arguments, args):
        """adds default parameters for HPC connection"""
        arguments[self.HPC_HOST] = args.hpc_host
        arguments[self.HPC_PORT] = args.hpc_port if args.hpc_port else 22
        arguments[self.HPC_USERNAME] = args.hpc_username
        arguments[self.HPC_SECRET_KEY_PATH] = args.hpc_secret_key

    def add_default_ckan_parameters(self, arguments, args):
        """adds default parameters for CKAN connection"""
        arguments[self.CKAN_HOST] = args.ckan_host
        arguments[self.CKAN_ORGANIZATION] = args.ckan_organization
        arguments[self.CKAN_PACKAGE] = args.ckan_dataset

    def set_sensitive_hpc_parameters(
        self, processors_with_hpc_sensitive_parameters, args
    ):
        """Set sensitive parameters for HPC connection"""
        sensitive_parameters = {}
        for processor in processors_with_hpc_sensitive_parameters:
            inner_sensitive_parameters = {}
            sensitive_parameters[processor] = inner_sensitive_parameters
            if args.hpc_password:
                inner_sensitive_parameters[self.HPC_PASSWORD_PROPERTY] = (
                    args.hpc_password
                )
            if args.hpc_secret_key_password:
                inner_sensitive_parameters[
                    self.HPC_SECRET_KEY_PATH_PASSWORD_PROPERTY
                ] = args.hpc_secret_key_password
        return sensitive_parameters

    def set_sensitive_ckan_parameters(
        self, processors_with_ckan_sensitive_parameters, args
    ):
        """Set sensitive parameters for CKAN connection"""
        sensitive_parameters = {}
        for processor in processors_with_ckan_sensitive_parameters:
            inner_sensitive_parameters = {}
            sensitive_parameters[processor] = inner_sensitive_parameters
            if args.ckan_api_key:
                inner_sensitive_parameters[self.CKAN_APIKEY_PROPERTY] = (
                    args.ckan_api_key
                )
        return sensitive_parameters

    def clean_process_group_up(self, process_group_id, token):
        """Clean up the process group and associated parameter context"""
        # Get process group
        process_group = self.get_process_group(process_group_id, token)

        # Remove transferred keys
        self.__logger.debug("Removing uploaded keys\n")
        self.remove_uploaded_keys(process_group["id"])

        # Get parameter context
        if "parameterContext" in process_group["component"]:
            # parameter context exists
            parameter_context_id = process_group["component"][
                "parameterContext"
            ]["id"]
            parameter_context = self.nifi_rest_client.get_parameter_context(
                parameter_context_id, token
            )

            # Remove parameter_context
            self.nifi_rest_client.remove_parameter_context(
                parameter_context, token)

        # Remove process_group
        self.nifi_rest_client.remove_process_group(process_group, token)

    def format_args_to_string(self, args):
        """Format dtcli command arguments to string for logging"""
        return " ".join(
            [
                (f"cka_host={args.ckan_host},"
                 if hasattr(args, "ckan_host") else ""),
                (
                    f"ckan_organization={args.ckan_organization},"
                    if hasattr(args, "ckan_organization")
                    else ""
                ),
                (
                    f"ckan_dataset={args.ckan_dataset},"
                    if hasattr(args, "ckan_dataset")
                    else ""
                ),
                (
                    f"ckan_resource={args.ckan_resource},"
                    if hasattr(args, "ckan_resource")
                    else ""
                ),
                (
                    f"data_source={args.data_source},"
                    if hasattr(args, "data_source")
                    else ""
                ),
                (
                    f"data_target={args.data_target},"
                    if hasattr(args, "data_target")
                    else ""
                ),
                (f"hpc_host={args.hpc_host},"
                 if hasattr(args, "hpc_host") else ""),
                (f"hpc_port={args.hpc_port},"
                 if hasattr(args, "hpc_port") else ""),
                (
                    f"hpc_username={args.hpc_username},"
                    if hasattr(args, "hpc_username")
                    else ""
                ),
                (
                    f"hpc_secret_key={args.hpc_secret_key},"
                    if hasattr(args, "hpc_secret_key")
                    else ""
                ),
                (
                    f"command_id={args.command_id},"
                    if hasattr(args, "command_id")
                    else ""
                ),
            ]
        )

    # Methods to upload/download files to/from the NIFI server

    def upload_key(self, key, process_group_id) -> str:
        """upload a single key into the NIFI server
        by using the user's access"""
        __uuid = uuid.uuid4()
        __key_name = f"{process_group_id}_{__uuid}"
        __target = os.path.join(
            self.__conf.nifi_upload_folder(), str(__key_name))
        ownership = f"{self.__conf.nifi_server_user_name()}:nifi"
        sftp_put(
            server=self.__conf.nifi_server(),
            private_key=self.__conf.nifi_server_private_key(),
            username=self.__conf.nifi_server_user_name(),
            target_permissions="660",
            target_ownership=ownership,
            source=key,
            target=__target,
        )
        return __target

    def upload_files(self, local_folder: str,
                     local_regexp: str) -> tuple[str, int]:
        """Upload files from the local folder to the NIFI upload subfolder."""
        # TODO investigate parallel upload using threads
        __uuid = uuid.uuid4()
        upload_folder = os.path.join(
            self.__conf.nifi_upload_folder(), str(__uuid))
        # Create upload folder in the NIFI server
        self.create_folder(upload_folder)
        # Read files in local_folder that matches the local_regexp
        num_files = 0
        for file in self.find_files(local_folder, local_regexp):
            num_files += 1
            target = os.path.join(upload_folder, os.path.basename(file))
            sftp_put(
                server=self.__conf.nifi_server(),
                private_key=self.__conf.nifi_server_private_key(),
                username=self.__conf.nifi_server_user_name(),
                target_permissions="660",
                target_ownership=f"{self.__conf.nifi_server_user_name()}:nifi",
                source=file,
                target=target,
            )
        return upload_folder, num_files

    def download_files(self, download_folder, target_folder):
        """Download files from the NIFI server to the local folder."""
        remote_files = ssh_list(
            server=self.__conf.nifi_server(),
            path=download_folder,
            username=self.__conf.nifi_server_user_name(),
            private_key=self.__conf.nifi_server_private_key(),
        )
        for file in remote_files:
            local_file = os.path.join(target_folder, os.path.basename(file))
            sftp_get(
                source=file,
                server=self.__conf.nifi_server(),
                username=self.__conf.nifi_server_user_name(),
                private_key=self.__conf.nifi_server_private_key(),
                target=local_file,
            )

    def find_files(self, local_folder: str, local_regexp: str) -> list[str]:
        """Find files in a local folder that match a regular expression."""
        if local_regexp == "":
            local_regexp = "*"
        pattern = os.path.join(local_folder, local_regexp)
        return glob.glob(pattern)

    def create_folder(self, upload_folder: str) -> None:
        """Create an upload folder in the NIFI server"""
        ssh_create_folder(
            folder=upload_folder,
            server=self.__conf.nifi_server(),
            username=self.__conf.nifi_server_user_name(),
            private_key=self.__conf.nifi_server_private_key(),
        )

    def remove_download_folder(self, download_folder):
        """Delete an download folder in the NIFI server"""
        ssh_delete_folder(
            folder=download_folder,
            server=self.__conf.nifi_server(),
            username=self.__conf.nifi_server_user_name(),
            private_key=self.__conf.nifi_server_private_key(),
        )

    def remove_upload_folder(self, upload_folder: str) -> None:
        """Remove an upload folder in the NIFI server"""
        # Add your implementation here
        ssh_delete_folder(
            folder=upload_folder,
            server=self.__conf.nifi_server(),
            username=self.__conf.nifi_server_user_name(),
            private_key=self.__conf.nifi_server_private_key(),
        )

    def remove_uploaded_keys(self, process_group_id):
        """deletes the keys uploaded into the NIFI server"""
        # find all keys uploaded in the NIFI server
        # corresponding to the process group
        remote_keys = ssh_list(
            path=self.__conf.nifi_upload_folder(),
            server=self.__conf.nifi_server(),
            username=self.__conf.nifi_server_user_name(),
            private_key=self.__conf.nifi_server_private_key(),
            prefix=process_group_id,
        )
        for file in remote_keys:
            self.remove_uploaded_key(file)

    def remove_uploaded_key(self, remote_key):
        """deletes a keys uploaded into the NIFI server"""
        ssh_delete_file(
            server=self.__conf.nifi_server(),
            private_key=self.__conf.nifi_server_private_key(),
            username=self.__conf.nifi_server_user_name(),
            file=remote_key,
        )
