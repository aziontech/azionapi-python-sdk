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
from edgeapplications.models.application_cache_patch_response import ApplicationCachePatchResponse  # noqa: E501
from edgeapplications.rest import ApiException

class TestApplicationCachePatchResponse(unittest.TestCase):
    """ApplicationCachePatchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApplicationCachePatchResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApplicationCachePatchResponse`
        """
        model = edgeapplications.models.application_cache_patch_response.ApplicationCachePatchResponse()  # noqa: E501
        if include_optional :
            return ApplicationCachePatchResponse(
                results = {"id":0,"name":"name","browser_cache_settings":"browser_cache_settings","browser_cache_settings_maximum_ttl":6,"cdn_cache_settings":"cdn_cache_settings","cdn_cache_settings_maximum_ttl":1,"cache_by_query_string":"cache_by_query_string","query_string_fields":["query_string_fields","query_string_fields"],"enable_query_string_sort":true,"cache_by_cookies":"cache_by_cookies","cookie_names":["cookie_names","cookie_names"],"adaptive_delivery_action":"adaptive_delivery_action","device_group":[1,2],"enable_caching_for_post":true,"l2_caching_enabled":true,"is_slice_configuration_enabled":true,"is_slice_edge_caching_enabled":true,"is_slice_l2_caching_enabled":true,"slice_configuration_range":1024,"enable_caching_for_options":true,"enable_stale_cache":true,"l2_region":"l2_region"}, 
                schema_version = 56
            )
        else :
            return ApplicationCachePatchResponse(
        )
        """

    def testApplicationCachePatchResponse(self):
        """Test ApplicationCachePatchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
