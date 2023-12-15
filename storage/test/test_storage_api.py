# coding: utf-8

"""
    Object Storage

    REST API OpenAPI documentation for the Object Storage

    The version of the OpenAPI document: 1.0.0 (v1)
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from storage.api.storage_api import StorageApi


class TestStorageApi(unittest.TestCase):
    """StorageApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StorageApi()

    def tearDown(self) -> None:
        pass

    def test_storage_api_buckets_create(self) -> None:
        """Test case for storage_api_buckets_create

        Create a new bucket
        """
        pass

    def test_storage_api_buckets_destroy(self) -> None:
        """Test case for storage_api_buckets_destroy

        Delete a bucket
        """
        pass

    def test_storage_api_buckets_list(self) -> None:
        """Test case for storage_api_buckets_list

        List buckets
        """
        pass

    def test_storage_api_buckets_objects_create(self) -> None:
        """Test case for storage_api_buckets_objects_create

        Create new object key
        """
        pass

    def test_storage_api_buckets_objects_destroy(self) -> None:
        """Test case for storage_api_buckets_objects_destroy

        Delete object key
        """
        pass

    def test_storage_api_buckets_objects_list(self) -> None:
        """Test case for storage_api_buckets_objects_list

        List buckets objects
        """
        pass

    def test_storage_api_buckets_objects_retrieve(self) -> None:
        """Test case for storage_api_buckets_objects_retrieve

        Download object
        """
        pass

    def test_storage_api_buckets_objects_update(self) -> None:
        """Test case for storage_api_buckets_objects_update

        Update the object key
        """
        pass

    def test_storage_api_buckets_partial_update(self) -> None:
        """Test case for storage_api_buckets_partial_update

        Update bucket info
        """
        pass


if __name__ == '__main__':
    unittest.main()