# coding: utf-8

"""
    Edge Function API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from edgefunctions.models.create_edge_function_request import CreateEdgeFunctionRequest  # noqa: E501

class TestCreateEdgeFunctionRequest(unittest.TestCase):
    """CreateEdgeFunctionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateEdgeFunctionRequest:
        """Test CreateEdgeFunctionRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateEdgeFunctionRequest`
        """
        model = CreateEdgeFunctionRequest()  # noqa: E501
        if include_optional:
            return CreateEdgeFunctionRequest(
                name = '',
                language = '',
                code = '',
                json_args = None,
                initiator_type = 'edge_application',
                active = True,
                is_proprietary_code = True
            )
        else:
            return CreateEdgeFunctionRequest(
        )
        """

    def testCreateEdgeFunctionRequest(self):
        """Test CreateEdgeFunctionRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()