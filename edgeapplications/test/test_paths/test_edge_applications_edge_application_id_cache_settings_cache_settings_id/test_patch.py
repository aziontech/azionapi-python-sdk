# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import edgeapplications
from edgeapplications.paths.edge_applications_edge_application_id_cache_settings_cache_settings_id import patch  # noqa: E501
from edgeapplications import configuration, schemas, api_client

from .. import ApiTestMixin


class TestEdgeApplicationsEdgeApplicationIdCacheSettingsCacheSettingsId(ApiTestMixin, unittest.TestCase):
    """
    EdgeApplicationsEdgeApplicationIdCacheSettingsCacheSettingsId unit test stubs
        /edge_applications/:edge_application_id:/cache_settings/:cache_settings_id:  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = patch.ApiForpatch(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
