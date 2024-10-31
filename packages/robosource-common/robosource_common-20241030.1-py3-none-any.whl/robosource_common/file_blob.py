from azure.storage.blob import BlobClient, ContainerClient
from typing import Iterator
import logging

logger=logging.getLogger('azure.core.pipeline.policies.http_logging_policy')
logger.setLevel(logging.WARNING)

class FileBlob:
    def __init__(self, container_name: str, connection_string: str):
        self.__container_name = container_name
        self.__connection_string = connection_string
    
    def write_file(self, file_path: str, content: bytes):
        blob_client = BlobClient.from_connection_string(
            conn_str=self.__connection_string,
            container_name=self.__container_name,
            blob_name=file_path
        )
        
        blob_client.upload_blob(content)

    def file_exists(self, file_path: str) -> bool:
        blob_client = BlobClient.from_connection_string(
            conn_str=self.__connection_string,
            container_name=self.__container_name,
            blob_name=file_path
        )

        return blob_client.exists()

    def list_files(self, dir_path: str) -> Iterator[str]:
        container_client = ContainerClient.from_connection_string(
            conn_str=self.__connection_string,
            container_name=self.__container_name
        )

        blobs = container_client.list_blobs(name_starts_with=dir_path)
        for blob in blobs:
            yield blob.name

    def read_file(self, file_path: str) -> bytes:
        blob_client = BlobClient.from_connection_string(
            conn_str=self.__connection_string,
            container_name=self.__container_name,
            blob_name=file_path
        )

        return blob_client.download_blob().readall()