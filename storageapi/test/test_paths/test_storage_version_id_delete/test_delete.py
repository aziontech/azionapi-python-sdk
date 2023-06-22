# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import storageapi
from storageapi.paths.storage_version_id_delete import delete  # noqa: E501
from storageapi import configuration, schemas, api_client

from .. import ApiTestMixin


class TestStorageVersionIdDelete(ApiTestMixin, unittest.TestCase):
    """
    StorageVersionIdDelete unit test stubs
        /domains/:version_id  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
