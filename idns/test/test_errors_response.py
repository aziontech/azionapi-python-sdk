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

from idns.models.errors_response import ErrorsResponse  # noqa: E501

class TestErrorsResponse(unittest.TestCase):
    """ErrorsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ErrorsResponse:
        """Test ErrorsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ErrorsResponse`
        """
        model = ErrorsResponse()  # noqa: E501
        if include_optional:
            return ErrorsResponse(
                errors = [
                    ''
                    ]
            )
        else:
            return ErrorsResponse(
        )
        """

    def testErrorsResponse(self):
        """Test ErrorsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
