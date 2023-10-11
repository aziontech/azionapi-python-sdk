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

from waf.models.waf_domain_list200 import WAFDomainList200  # noqa: E501

class TestWAFDomainList200(unittest.TestCase):
    """WAFDomainList200 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WAFDomainList200:
        """Test WAFDomainList200
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WAFDomainList200`
        """
        model = WAFDomainList200()  # noqa: E501
        if include_optional:
            return WAFDomainList200(
                id = 56,
                name = '',
                domain = '',
                cnames = [
                    ''
                    ]
            )
        else:
            return WAFDomainList200(
        )
        """

    def testWAFDomainList200(self):
        """Test WAFDomainList200"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()