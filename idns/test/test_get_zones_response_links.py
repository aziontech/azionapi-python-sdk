# coding: utf-8

"""
    Intelligent DNS API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from idns.models.get_zones_response_links import GetZonesResponseLinks  # noqa: E501

class TestGetZonesResponseLinks(unittest.TestCase):
    """GetZonesResponseLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetZonesResponseLinks:
        """Test GetZonesResponseLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetZonesResponseLinks`
        """
        model = GetZonesResponseLinks()  # noqa: E501
        if include_optional:
            return GetZonesResponseLinks(
                previous = '',
                next = ''
            )
        else:
            return GetZonesResponseLinks(
        )
        """

    def testGetZonesResponseLinks(self):
        """Test GetZonesResponseLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()