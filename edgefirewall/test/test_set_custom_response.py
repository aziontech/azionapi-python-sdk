# coding: utf-8

"""
    Edge Firewall API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from edgefirewall.models.set_custom_response import SetCustomResponse  # noqa: E501

class TestSetCustomResponse(unittest.TestCase):
    """SetCustomResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SetCustomResponse:
        """Test SetCustomResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SetCustomResponse`
        """
        model = SetCustomResponse()  # noqa: E501
        if include_optional:
            return SetCustomResponse(
                name = 'set_custom_response',
                argument = {"status_code":200,"content_type":"application/json","content_body":"{}"}
            )
        else:
            return SetCustomResponse(
        )
        """

    def testSetCustomResponse(self):
        """Test SetCustomResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
