# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import idns
from idns.paths.intelligent_dns_zone_id_records import get  # noqa: E501
from idns import configuration, schemas, api_client

from .. import ApiTestMixin


class TestIntelligentDnsZoneIdRecords(ApiTestMixin, unittest.TestCase):
    """
    IntelligentDnsZoneIdRecords unit test stubs
        Get a collection of Intelligent DNS zone records  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
