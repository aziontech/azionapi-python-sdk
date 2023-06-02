# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import services
from services.paths.edge_services_id import delete  # noqa: E501
from services import configuration, schemas, api_client

from .. import ApiTestMixin


class TestEdgeServicesId(ApiTestMixin, unittest.TestCase):
    """
    EdgeServicesId unit test stubs
        Delete Service by ID  # noqa: E501
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
