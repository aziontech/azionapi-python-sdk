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

from edgefunctions.models.list_edge_function_response import ListEdgeFunctionResponse  # noqa: E501

class TestListEdgeFunctionResponse(unittest.TestCase):
    """ListEdgeFunctionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListEdgeFunctionResponse:
        """Test ListEdgeFunctionResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListEdgeFunctionResponse`
        """
        model = ListEdgeFunctionResponse()  # noqa: E501
        if include_optional:
            return ListEdgeFunctionResponse(
                count = 56,
                total_pages = 56,
                schema_version = 56,
                links = {"next":"next","previous":"previous"},
                results = [
                    {"code":"function foo() { console.log('hello world');","last_editor":"user@azion.com","name":"MyFunction","active":true,"modified":"modified","language":"javascript","json_args":"{\"a\": 1, \"b\": 2}","id":5,"function_to_run":"function_to_run","reference_count":5,"initiator_type":"edge_application"}
                    ]
            )
        else:
            return ListEdgeFunctionResponse(
        )
        """

    def testListEdgeFunctionResponse(self):
        """Test ListEdgeFunctionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()