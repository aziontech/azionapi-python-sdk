# coding: utf-8

"""
    Edge Application API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import edgeapplications
from edgeapplications.models.application_cache_results import ApplicationCacheResults  # noqa: E501
from edgeapplications.rest import ApiException

class TestApplicationCacheResults(unittest.TestCase):
    """ApplicationCacheResults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApplicationCacheResults
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApplicationCacheResults`
        """
        model = edgeapplications.models.application_cache_results.ApplicationCacheResults()  # noqa: E501
        if include_optional :
            return ApplicationCacheResults(
                id = 56, 
                name = '', 
                browser_cache_settings = '', 
                browser_cache_settings_maximum_ttl = 56, 
                cdn_cache_settings = '', 
                cdn_cache_settings_maximum_ttl = 56, 
                cache_by_query_string = '', 
                query_string_fields = [
                    ''
                    ], 
                enable_query_string_sort = True, 
                cache_by_cookies = '', 
                cookie_names = [
                    ''
                    ], 
                adaptive_delivery_action = '', 
                device_group = [
                    56
                    ], 
                enable_caching_for_post = True, 
                l2_caching_enabled = True, 
                is_slice_configuration_enabled = True, 
                is_slice_edge_caching_enabled = True, 
                is_slice_l2_caching_enabled = True, 
                slice_configuration_range = 56, 
                enable_caching_for_options = True, 
                enable_stale_cache = True, 
                l2_region = ''
            )
        else :
            return ApplicationCacheResults(
                id = 56,
                name = '',
                browser_cache_settings = '',
                browser_cache_settings_maximum_ttl = 56,
                cdn_cache_settings = '',
                cdn_cache_settings_maximum_ttl = 56,
                cache_by_query_string = '',
                query_string_fields = [
                    ''
                    ],
                enable_query_string_sort = True,
                cache_by_cookies = '',
                cookie_names = [
                    ''
                    ],
                adaptive_delivery_action = '',
                device_group = [
                    56
                    ],
                enable_caching_for_post = True,
                l2_caching_enabled = True,
                enable_caching_for_options = True,
                enable_stale_cache = True,
                l2_region = '',
        )
        """

    def testApplicationCacheResults(self):
        """Test ApplicationCacheResults"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
