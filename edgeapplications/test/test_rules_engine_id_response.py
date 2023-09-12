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
from edgeapplications.models.rules_engine_id_response import RulesEngineIdResponse  # noqa: E501
from edgeapplications.rest import ApiException

class TestRulesEngineIdResponse(unittest.TestCase):
    """RulesEngineIdResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RulesEngineIdResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RulesEngineIdResponse`
        """
        model = edgeapplications.models.rules_engine_id_response.RulesEngineIdResponse()  # noqa: E501
        if include_optional :
            return RulesEngineIdResponse(
                results = {"phase":"phase","is_active":true,"behavior":[{"name":"name","target":"target"}],"criteria":[[{"conditional":"conditional","variable":"variable","input_value":"input_value","operator":"operator"},{"conditional":"conditional","variable":"variable","input_value":"input_value","operator":"operator"}],[{"conditional":"conditional","variable":"variable","input_value":"input_value","operator":"operator"},{"conditional":"conditional","variable":"variable","input_value":"input_value","operator":"operator"}]],"name":"name","id":5,"order":5}, 
                schema_version = 56
            )
        else :
            return RulesEngineIdResponse(
                results = {"phase":"phase","is_active":true,"behavior":[{"name":"name","target":"target"}],"criteria":[[{"conditional":"conditional","variable":"variable","input_value":"input_value","operator":"operator"},{"conditional":"conditional","variable":"variable","input_value":"input_value","operator":"operator"}],[{"conditional":"conditional","variable":"variable","input_value":"input_value","operator":"operator"},{"conditional":"conditional","variable":"variable","input_value":"input_value","operator":"operator"}]],"name":"name","id":5,"order":5},
                schema_version = 56,
        )
        """

    def testRulesEngineIdResponse(self):
        """Test RulesEngineIdResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()