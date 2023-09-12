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
from edgeapplications.models.origins_response_links import OriginsResponseLinks  # noqa: E501
from edgeapplications.rest import ApiException

class TestOriginsResponseLinks(unittest.TestCase):
    """OriginsResponseLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OriginsResponseLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OriginsResponseLinks`
        """
        model = edgeapplications.models.origins_response_links.OriginsResponseLinks()  # noqa: E501
        if include_optional :
            return OriginsResponseLinks(
                previous = '', 
                next = ''
            )
        else :
            return OriginsResponseLinks(
        )
        """

    def testOriginsResponseLinks(self):
        """Test OriginsResponseLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
