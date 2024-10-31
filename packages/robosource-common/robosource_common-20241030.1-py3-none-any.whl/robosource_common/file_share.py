from azure.storage.fileshare import ShareDirectoryClient, ShareFileClient
from typing import Iterator, Union
import os, logging

logger=logging.getLogger('azure.core.pipeline.policies.http_logging_policy')
logger.setLevel(logging.WARNING)

class FileShare:
    def __init__(self, share_name: str, connection_string: str):
        self.__share_name = share_name
        self.__connection_string = connection_string

    def read_file(self, file_path: str) -> str:
        file_client = ShareFileClient.from_connection_string(
            conn_str=self.__connection_string,
            share_name=self.__share_name,
            file_path=file_path
        )

        return file_client.download_file().readall()

    def list_files(
            self,
            dir_path: str,
            include_properties: bool = False,
            recursive: bool = True
    ) -> Iterator[Union[str, dict]]:
        dir_client = ShareDirectoryClient.from_connection_string(
            conn_str=self.__connection_string,
            share_name=self.__share_name,
            directory_path=dir_path
        )

        # Listing files from current directory path:
        for file in dir_client.list_directories_and_files():
            name, is_directory = file['name'], file['is_directory']
            path = os.path.join(dir_path, name)

            if is_directory:
                if recursive:
                    # Listing files recursively:
                    childrens = self.list_files(
                        dir_path=path,
                        include_properties=include_properties,
                        recursive=recursive
                    )

                    for child in childrens:
                        yield child
            else:
                if include_properties:
                    file_client = ShareFileClient.from_connection_string(
                        conn_str=self.__connection_string,
                        share_name=self.__share_name,
                        file_path=path
                    )

                    yield file_client.get_file_properties()
                else:
                    yield path