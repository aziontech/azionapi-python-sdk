# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import edgefirewall
from edgefirewall.paths.edge_firewall_uuid import put  # noqa: E501
from edgefirewall import configuration, schemas, api_client

from .. import ApiTestMixin


class TestEdgeFirewallUuid(ApiTestMixin, unittest.TestCase):
    """
    EdgeFirewallUuid unit test stubs
        Overwrite some edge firewall attributes, like \"active\"  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = put.ApiForput(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()
