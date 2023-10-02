# coding: utf-8

"""
    Web Application Firewall API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from waf.models.waf_events200 import WAFEvents200  # noqa: E501

class TestWAFEvents200(unittest.TestCase):
    """WAFEvents200 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WAFEvents200:
        """Test WAFEvents200
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WAFEvents200`
        """
        model = WAFEvents200()  # noqa: E501
        if include_optional:
            return WAFEvents200(
                results = [
                    {"hit_count":9290,"rule_id":1005,"ip_count":217,"match_zone":"cookies","path_count":798,"matches_on":"value","rule_description":"Possible SQL Injection attack: MySQL keyword (|) found in Cookies"}
                    ],
                schema_version = 3
            )
        else:
            return WAFEvents200(
        )
        """

    def testWAFEvents200(self):
        """Test WAFEvents200"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()