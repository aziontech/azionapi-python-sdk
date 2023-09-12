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
from edgeapplications.models.origins_id_response import OriginsIdResponse  # noqa: E501
from edgeapplications.rest import ApiException

class TestOriginsIdResponse(unittest.TestCase):
    """OriginsIdResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OriginsIdResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OriginsIdResponse`
        """
        model = edgeapplications.models.origins_id_response.OriginsIdResponse()  # noqa: E501
        if include_optional :
            return OriginsIdResponse(
                results = {"timeout_between_bytes":2,"addresses":[{"address":"address","is_active":true,"weight":"weight","server_role":"server_role"},{"address":"address","is_active":true,"weight":"weight","server_role":"server_role"}],"hmac_secret_key":"hmac_secret_key","method":"method","origin_path":"origin_path","origin_protocol_policy":"origin_protocol_policy","hmac_region_name":"hmac_region_name","hmac_access_key":"hmac_access_key","origin_id":5,"is_origin_redirection_enabled":true,"origin_type":"origin_type","host_header":"host_header","origin_key":"origin_key","name":"name","connection_timeout":5,"hmac_authentication":true}, 
                schema_version = 56
            )
        else :
            return OriginsIdResponse(
                results = {"timeout_between_bytes":2,"addresses":[{"address":"address","is_active":true,"weight":"weight","server_role":"server_role"},{"address":"address","is_active":true,"weight":"weight","server_role":"server_role"}],"hmac_secret_key":"hmac_secret_key","method":"method","origin_path":"origin_path","origin_protocol_policy":"origin_protocol_policy","hmac_region_name":"hmac_region_name","hmac_access_key":"hmac_access_key","origin_id":5,"is_origin_redirection_enabled":true,"origin_type":"origin_type","host_header":"host_header","origin_key":"origin_key","name":"name","connection_timeout":5,"hmac_authentication":true},
                schema_version = 56,
        )
        """

    def testOriginsIdResponse(self):
        """Test OriginsIdResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
