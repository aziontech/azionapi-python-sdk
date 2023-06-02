# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import edgefunctions
from edgefunctions.paths.edge_functions_id import delete  # noqa: E501
from edgefunctions import configuration, schemas, api_client

from .. import ApiTestMixin


class TestEdgeFunctionsId(ApiTestMixin, unittest.TestCase):
    """
    EdgeFunctionsId unit test stubs
        edge_functions  # noqa: E501
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
