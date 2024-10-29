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


This module defines the HiDALGO2 Data Transfer API client class.
It provides methods to transfer datasets between different data providers,
including Cloud, HDFS, CKAN, local filesystems and HPC, using NIFI pipelines.
"""

import sys
from typing import Any, Dict, Optional
import uuid
import os
from types import SimpleNamespace

from hid_data_transfer_lib.conf.hid_dt_configuration import (
    HidDataTransferConfiguration
)
from hid_data_transfer_lib.exceptions.hid_dt_exceptions import (
    HidDataTransferException
)
from hid_data_transfer_lib.nifi.nifi_client import NIFIClient, ExecutionType


class HIDDataTransfer:
    """main HiDALGO  API client class
    contains methods to transfer datasets between different data providers
    using NIFI pipelines
    """

    def __init__(
        self, conf: HidDataTransferConfiguration,
        secure: bool = False,
        keycloak_token: Optional[Dict[Any, Any]] = None,
    ) -> None:
        """constructs a NIFI client,
        with the NIFI endpoint taken from configuration
        """
        self.__conf = conf
        self.__nifi_client = NIFIClient(conf, secure)
        self.__logger = self.__conf.logger("hid_data_transfer_lib")
        self.__keycloak_token = keycloak_token

    # MAIN API methods
    def hdfs2hpc(
        self,
        hpc_host,
        hpc_username,
        data_source,
        data_target,
        hpc_port=None,
        hpc_password=None,
        hpc_secret_key_password=None,
        hpc_secret_key_path=None,
    ) -> str:
        """
        transfer data from hdfs to hpc using sftp
        Args:
                hpc_host (str): The hostname of the HPC server.
                hpc_port (int): The port number of the HPC server.
                hpc_username (str): The username for the HPC server.
                hpc_secret_key_path (str): The path to the secret key
                    for HPC authentication.
                data_source (str): The source path in HDFS.
                data_target (str): The target path in HPC.
            Returns:
                str: The id of the data tranfer process group in NIFI.
            Raises:
                HidDataTransferException: If an error occurs during
                the data transfer process
        """
        args = SimpleNamespace(
            hpc_host=hpc_host,
            hpc_port=hpc_port,
            hpc_username=hpc_username,
            hpc_password=hpc_password,
            hpc_secret_key_password=hpc_secret_key_password,
            hpc_secret_key=hpc_secret_key_path,
            data_source=data_source,
            data_target=data_target,
        )

        self.__logger.info(
            "executing hdfs2hpc command with args: %s",
            self.__nifi_client.format_args_to_string(args),
        )
        try:
            arguments: Dict[str, Any] = {}
            self.__nifi_client.add_default_hpc_parameters(arguments, args)
            arguments["hpc.target_folder"] = args.data_target
            arguments["hdfs.filepath"] = \
                "/".join(args.data_source.split("/")[:-1])
            arguments["hdfs.filename"] = args.data_source.split("/")[-1]

            execution_type = {
                "GetHDFS": ExecutionType.ONCE,
                "PutSFTP": ExecutionType.ONCE,
            }
            keys_arguments = {
                self.__nifi_client.HPC_SECRET_KEY_PATH: arguments[
                    self.__nifi_client.HPC_SECRET_KEY_PATH
                ],
            }

            processors_with_hpc_sensitive_parameters = ["PutSFTP"]
            sensitive_parameters = \
                self.__nifi_client.set_sensitive_hpc_parameters(
                    processors_with_hpc_sensitive_parameters,
                    args
                )

            if not args.hpc_secret_key and not args.hpc_password:
                raise HidDataTransferException(
                    "Either hpc_password or hpc_secret_key must be provided"
                )

            return self.__nifi_client.run_process_group(
                "hdfs2hpc",
                execution_type,
                arguments,
                keys_arguments,
                sensitive_parameters,
                keycloak_token=self.__keycloak_token,
            )

        except Exception as ex:
            raise HidDataTransferException(ex) from ex

    def hpc2hdfs(
        self,
        hpc_host,
        hpc_username,
        data_source,
        data_target,
        hpc_port=None,
        hpc_password=None,
        hpc_secret_key_password=None,
        hpc_secret_key_path=None,
    ) -> str:
        """
        transfer data from hpc to hdfs using sftp

        Args:
            hpc_host (str): The hostname of the HPC server.
            hpc_port (int): The port number of the HPC server.
            hpc_username (str): The username for the HPC server.
            hpc_secret_key_path (str): The path to the secret
                key for HPC authentication.
            data_source (str): The source path in HPC.
            data_target (str): The target path in HDFS.
        Returns:
            str: The id of the data tranfer process group in NIFI.
        Raises:
            HidDataTransferException: If an error occurs during
            the data transfer process
        """

        args = SimpleNamespace(
            hpc_host=hpc_host,
            hpc_port=hpc_port,
            hpc_username=hpc_username,
            hpc_password=hpc_password,
            hpc_secret_key_password=hpc_secret_key_password,
            hpc_secret_key=hpc_secret_key_path,
            data_source=data_source,
            data_target=data_target,
        )

        self.__logger.info(
            "executing hpc2hdfs command with args: %s",
            self.__nifi_client.format_args_to_string(args),
        )
        try:
            arguments: Dict[str, Any] = {}
            self.__nifi_client.add_default_hpc_parameters(arguments, args)
            arguments["hpc.filename"] = args.data_source
            arguments["hdfs.target_folder"] = args.data_target

            execution_type = {
                "GenerateFlowFile": ExecutionType.ONCE,
                "FetchSFTP": ExecutionType.ONCE,
                "PutHDFS": ExecutionType.ONCE,
            }
            keys_arguments = {
                self.__nifi_client.HPC_SECRET_KEY_PATH: arguments[
                    self.__nifi_client.HPC_SECRET_KEY_PATH
                ],
            }

            processors_with_hpc_sensitive_parameters = ["FetchSFTP", "PutHDFS"]
            sensitive_parameters = \
                self.__nifi_client.set_sensitive_hpc_parameters(
                    processors_with_hpc_sensitive_parameters, args
                )

            if not args.hpc_secret_key and not args.hpc_password:
                raise HidDataTransferException(
                    "Either hpc_password or hpc_secret_key must be provided"
                )

            return self.__nifi_client.run_process_group(
                "hpc2hdfs",
                execution_type,
                arguments,
                keys_arguments,
                sensitive_parameters,
                keycloak_token=self.__keycloak_token,
            )

        except Exception as ex:
            raise HidDataTransferException(ex) from ex

    def ckan2hpc(
        self,
        ckan_host,
        ckan_api_key,
        ckan_organization,
        ckan_dataset,
        hpc_host,
        hpc_username,
        data_target,
        hpc_port=None,
        hpc_password=None,
        hpc_secret_key_password=None,
        hpc_secret_key_path=None,
        ckan_resource=None,
    ) -> str:
        """
        transfer data from ckan to hpc using sftp

        Args:
            ckan_host (str): The CKAN host URL.
            ckan_organization (str): The CKAN organization name.
            ckan_dataset (str): The CKAN dataset name.
            hpc_host (str): The HPC host URL.
            hpc_port (int): The port number for the HPC connection.
            hpc_username (str): The username for the HPC connection.
            hpc_secret_key_path (str): The file path to the HPC secret key.
            data_target (str): The target directory on the HPC where
                the data will be transferred.
            ckan_resource (str, optional): The specific CKAN resource
                to transfer. Defaults to None.

        Returns:
            str: The result of the process group execution.

        Raises:
            HidDataTransferException: If an error occurs during
            the data transfer process.
        """

        args = SimpleNamespace(
            ckan_host=ckan_host,
            ckan_api_key=ckan_api_key,
            ckan_organization=ckan_organization,
            ckan_dataset=ckan_dataset,
            ckan_resource=ckan_resource,
            hpc_host=hpc_host,
            hpc_port=hpc_port,
            hpc_username=hpc_username,
            hpc_password=hpc_password,
            hpc_secret_key_password=hpc_secret_key_password,
            hpc_secret_key=hpc_secret_key_path,
            data_target=data_target,
        )

        self.__logger.info(
            "executing ckan2hpc command with args: %s",
            self.__nifi_client.format_args_to_string(args),
        )
        try:
            arguments: Dict[str, Any] = {}
            self.__nifi_client.add_default_hpc_parameters(arguments, args)
            arguments["hpc.target_folder"] = args.data_target
            self.__nifi_client.add_default_ckan_parameters(arguments, args)
            arguments[self.__nifi_client.CKAN_RESOURCE] = (
                args.ckan_resource if args.ckan_resource else ".*"
            )

            keys_arguments = {
                self.__nifi_client.HPC_SECRET_KEY_PATH: arguments[
                    self.__nifi_client.HPC_SECRET_KEY_PATH
                ],
            }

            processors_with_hpc_sensitive_parameters = ["PutSFTP"]
            sensitive_parameters = \
                self.__nifi_client.set_sensitive_hpc_parameters(
                    processors_with_hpc_sensitive_parameters, args
                )

            processors_with_ckan_sensitive_parameters = ["CKANFileDownloader"]
            sensitive_parameters = \
                self.__nifi_client.set_sensitive_ckan_parameters(
                    processors_with_ckan_sensitive_parameters, args
                )

            if not args.hpc_secret_key and not args.hpc_password:
                raise HidDataTransferException(
                    "Either hpc_password or hpc_secret_key must be provided"
                )

            execution_type = {
                "CKANFileDownloader": ExecutionType.ONCE,
                "PutSFTP": ExecutionType.ONCE,
            }
            return self.__nifi_client.run_process_group(
                "ckan2hpc",
                execution_type,
                arguments,
                keys_arguments,
                sensitive_parameters,
                keycloak_token=self.__keycloak_token,
            )

        except Exception as ex:
            raise HidDataTransferException(ex) from ex

        return sensitive_parameters

    def hpc2ckan(
        self,
        hpc_host,
        hpc_username,
        ckan_host,
        ckan_api_key,
        ckan_organization,
        ckan_dataset,
        data_source,
        hpc_port=None,
        hpc_password=None,
        hpc_secret_key_password=None,
        hpc_secret_key_path=None,
    ) -> str:
        """
        transfer data from hpc to ckan using sftp

        Args:
            hpc_host (str): The HPC host URL.
            hpc_port (int): The port number for the HPC connection.
            hpc_username (str): The username for the HPC connection.
            hpc_secret_key_path (str): The file path to the HPC secret key.
            ckan_host (str): The CKAN host URL.
            ckan_organization (str): The CKAN organization name.
            ckan_dataset (str): The CKAN dataset name.
            data_source (str): The source directory on the HPC
                whose data will be transferred.

        Returns:
            str: The result of the process group execution.

        Raises:
            HidDataTransferException: If an error occurs during
            the data transfer process.

        """
        args = SimpleNamespace(
            hpc_host=hpc_host,
            hpc_port=hpc_port,
            hpc_username=hpc_username,
            hpc_password=hpc_password,
            hpc_secret_key_password=hpc_secret_key_password,
            hpc_secret_key=hpc_secret_key_path,
            ckan_host=ckan_host,
            ckan_api_key=ckan_api_key,
            ckan_organization=ckan_organization,
            ckan_dataset=ckan_dataset,
            data_source=data_source,
        )

        self.__logger.info(
            "executing hpc2ckan command with args: %s",
            self.__nifi_client.format_args_to_string(args),
        )
        try:
            hpc_filename = args.data_source[args.data_source.rfind("/") + 1 :]
            arguments: Dict[str, Any] = {}
            self.__nifi_client.add_default_hpc_parameters(arguments, args)
            arguments["hpc.filename"] = hpc_filename if hpc_filename else ".*"
            arguments["hpc.data_folder"] = args.data_source[
                : args.data_source.rfind("/")
            ]
            self.__nifi_client.add_default_ckan_parameters(arguments, args)
            ckan_resource = (
                args.data_source.replace("/", "_")
                if not args.data_source.endswith("/")
                else args.data_source[:-1].replace("/", "_")
            )
            if not ckan_resource.endswith(".zip"):
                ckan_resource += ".zip"
            arguments[self.__nifi_client.CKAN_RESOURCE] = ckan_resource

            keys_arguments = {
                self.__nifi_client.HPC_SECRET_KEY_PATH: arguments[
                    self.__nifi_client.HPC_SECRET_KEY_PATH
                ],
            }

            processors_with_hpc_sensitive_parameters = \
                ["ListSFTP", "FetchSFTP"]
            sensitive_parameters = \
                self.__nifi_client.set_sensitive_hpc_parameters(
                    processors_with_hpc_sensitive_parameters, args
                )

            processors_with_ckan_sensitive_parameters = ["CKANFileUploader"]
            sensitive_parameters = \
                self.__nifi_client.set_sensitive_ckan_parameters(
                    processors_with_ckan_sensitive_parameters, args
                )

            if not args.hpc_secret_key and not args.hpc_password:
                raise HidDataTransferException(
                    "Either hpc_password or hpc_secret_key must be provided"
                )

            execution_type = {
                "ListSFTP": ExecutionType.ONCE,
                "FetchSFTP": ExecutionType.FOREVER,
                "MergeContent": ExecutionType.FOREVER,
                "UpdateAttribute": ExecutionType.ONCE,
                "CKANFileUploader": ExecutionType.ONCE,
            }
            return self.__nifi_client.run_process_group(
                "hpc2ckanv2",
                execution_type,
                arguments,
                keys_arguments,
                sensitive_parameters,
                keycloak_token=self.__keycloak_token,
            )

        except Exception as ex:
            raise HidDataTransferException(ex) from ex

    def local2ckan(
        self,
        ckan_host,
        ckan_api_key,
        ckan_organization,
        ckan_dataset,
        ckan_resource,
        data_source,
    ) -> str:
        """
        transfer data from local filesystem to ckan using sftp

        Args:
            ckan_host (str): The CKAN host URL.
            ckan_organization (str): The CKAN organization name.
            ckan_dataset (str): The CKAN dataset name.
            ckan_resource (str): The name of the CKAN resource
                to be created with the data.
            data_source (str): The directory on the local filesystem
                whose data will be transferred.

        Returns:
            str: The result of the process group execution.

        Raises:
            HidDataTransferException: If an error occurs during
            the data transfer process.

        """

        args = SimpleNamespace(
            ckan_host=ckan_host,
            ckan_api_key=ckan_api_key,
            ckan_organization=ckan_organization,
            ckan_dataset=ckan_dataset,
            ckan_resource=ckan_resource,
            data_source=data_source,
        )

        self.__logger.info(
            "executing local2ckan command with args: %s",
            self.__nifi_client.format_args_to_string(args),
        )
        upload_folder = None
        try:
            local_regexp = \
                args.data_source[args.data_source.rfind("/") + 1 :]
            local_folder = args.data_source[: args.data_source.rfind("/")]

            arguments: Dict[str, Any] = {}

            self.__nifi_client.add_default_ckan_parameters(arguments, args)
            arguments[self.__nifi_client.CKAN_RESOURCE] = \
                args.ckan_resource + ".zip"

            # Transfer files from data source to NIFI upload subfolder
            # (within user folder)
            upload_folder, num_files = self.__nifi_client.upload_files(
                local_folder, local_regexp
            )
            if num_files == 0:
                raise HidDataTransferException(
                    f"No files found in {local_folder} "
                    "with pattern {local_regexp}"
                )
            arguments["local.folder"] = upload_folder
            arguments["local.numfiles"] = num_files

            keys_arguments: Dict[str, Any] = {}

            processors_with_ckan_sensitive_parameters = ["CKANFileUploader"]
            sensitive_parameters = \
                self.__nifi_client.set_sensitive_ckan_parameters(
                    processors_with_ckan_sensitive_parameters, args
                )

            execution_type = {
                "GetFile": ExecutionType.FOREVER,
                "MergeContent": ExecutionType.FOREVER,
                "UpdateAttribute": ExecutionType.ONCE,
                "CKANFileUploader": ExecutionType.ONCE,
            }

            return self.__nifi_client.run_process_group(
                "local2ckan",
                execution_type,
                arguments,
                keys_arguments,
                sensitive_parameters,
                first_processor_expected_outgoing_flowfiles=num_files,
                keycloak_token=self.__keycloak_token,
            )

        except Exception as ex:
            raise HidDataTransferException(ex) from ex
        finally:
            # Remove uploaded files
            if upload_folder is not None:
                self.__nifi_client.remove_upload_folder(upload_folder)

    def ckan2local(
        self,
        ckan_host,
        ckan_api_key,
        ckan_organization,
        ckan_dataset,
        data_target,
        ckan_resource=None,
    ) -> str:
        """
        transfer data from ckan to the local filesystem using sftp

        Args:
            ckan_host (str): The CKAN host URL.
            ckan_organization (str): The CKAN organization name.
            ckan_dataset (str): The CKAN dataset name.
            ckan_resource (str): The name of the CKAN resource to transfer.
            data_source (str): The  directory on the local filesystem
                where to transfer the data.

        Returns:
            str: The result of the process group execution.

        Raises:
            HidDataTransferException: If an error occurs during
                the data transfer process.

        """

        args = SimpleNamespace(
            ckan_host=ckan_host,
            ckan_api_key=ckan_api_key,
            ckan_organization=ckan_organization,
            ckan_dataset=ckan_dataset,
            ckan_resource=ckan_resource,
            data_target=data_target,
        )

        self.__logger.info(
            "executing ckan2local command with args: %s",
            self.__nifi_client.format_args_to_string(args),
        )
        try:
            arguments: Dict[str, Any] = {}

            __uuid = uuid.uuid4()
            download_folder = os.path.join(
                self.__conf.nifi_download_folder(), str(__uuid)
            )
            self.__nifi_client.create_folder(download_folder)
            arguments["nifi.download_folder"] = download_folder

            self.__nifi_client.add_default_ckan_parameters(arguments, args)
            if args.ckan_resource:
                arguments[self.__nifi_client.CKAN_RESOURCE] = \
                    args.ckan_resource
            else:
                arguments[self.__nifi_client.CKAN_RESOURCE] = ".*"

            keys_arguments: Dict[str, Any] = {}

            processors_with_ckan_sensitive_parameters = ["CKANFileDownloader"]
            sensitive_parameters = \
                self.__nifi_client.set_sensitive_ckan_parameters(
                    processors_with_ckan_sensitive_parameters, args
                )

            execution_type = {
                "CKANFileDownloader": ExecutionType.ONCE,
                "PutFile": ExecutionType.FOREVER,
            }

            process_group_id = self.__nifi_client.run_process_group(
                "ckan2local",
                execution_type,
                arguments,
                keys_arguments,
                sensitive_parameters,
                keycloak_token=self.__keycloak_token,
            )

            # Transfer files from NIFI upload subfolder to the target folder

            self.__nifi_client.download_files(
                download_folder, args.data_target)

            sys.stdout.write(
                f"{args.ckan_resource} CKAN resource transferred to \
                {args.data_target} local folder\n"
            )

            return process_group_id

        except Exception as ex:
            raise HidDataTransferException(ex) from ex
        finally:
            # Remove uploaded files
            if download_folder is not None:
                self.__nifi_client.remove_download_folder(download_folder)

    def check_command_status(self, command_id):
        """
        Checks the status of a NIFI pipeline (process group) by id

        Args:
            command_id (str): The id of the process group whose status
                is to be checked.

        Returns:
            Prints the status

        Raises:
            HidDataTransferException: If an error occurs
                while processing this method.

        """

        args = SimpleNamespace(
            command_id=command_id,
        )

        # Check process group state by id
        # This implies to check the execution state of
        # the last processor in the group
        self.__logger.info(
            "executing check_command_status command with args: %s",
            self.__nifi_client.format_args_to_string(args),
        )

        # Read arguments
        process_group_id = args.command_id

        try:
            # Get access token, do not forget to cancel
            # the token refresh when done with it
            token = self.__nifi_client.get_access_token()

            # Get all processors in the process group
            processors = self.__nifi_client.get_process_group_processors(
                process_group_id, token
            )["processors"]

            # Order processor by pipeline sequence
            processors_sequence = self.__nifi_client.get_processors_sequence(
                process_group_id, token
            )
            processors = self.__nifi_client.order_processors(
                processors, processors_sequence
            )

            # Get status of last processor
            last_processor = processors[-1]

            if last_processor:
                state = \
                    self.__nifi_client.nifi_rest_client.get_processor_state(
                        last_processor, token
                    )
                # Get if there remains pending incoming flowfiles
                # to be processed
                are_all_flowfiles_consumed = (
                    self.__nifi_client.are_all_processor_queued_flowfiles_consumed(
                        last_processor, process_group_id, token
                    )
                )
                if state == "STOPPED" and are_all_flowfiles_consumed:
                    state = "TERMINATED"
                else:
                    state = "RUNNING"

                sys.stdout.write(f"State of command {process_group_id} "
                                 "is {state}\n")
                # Determine if errors/warnings have been produced
                # in the process.
                # Get processors on group and display bulletins reports
                processors = self.__nifi_client.get_process_group_processors(
                    process_group_id, token
                )
                for processor in processors["processors"]:
                    bulletins = processor["bulletins"]
                    for _bulletin in bulletins:
                        # display bulletin
                        bulletin = _bulletin["bulletin"]
                        msg = (
                            f'{bulletin["level"]}: "{bulletin["message"]}" '
                            f'reported at {bulletin["timestamp"]} '
                            'by processor '
                            f'{bulletin["sourceName"]} '
                            'with id {bulletin["sourceId"]}\n'
                        )
                        sys.stderr.write(msg)
            else:
                raise HidDataTransferException(
                    f"Could not find last processor of command with id "
                    f"{process_group_id}"
                )
        except Exception as ex:
            raise HidDataTransferException(ex) from ex
        finally:
            self.__nifi_client.cancel_access_token()
