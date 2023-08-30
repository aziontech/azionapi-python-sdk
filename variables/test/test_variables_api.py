# coding: utf-8

"""
    Variables API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

import variables
from variables.api.variables_api import VariablesApi  # noqa: E501
from variables.rest import ApiException


class TestVariablesApi(unittest.TestCase):
    """VariablesApi unit test stubs"""

    def setUp(self):
        self.api = variables.api.variables_api.VariablesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_variables_create(self):
        """Test case for api_variables_create

        /variables  # noqa: E501
        """
        pass

    def test_api_variables_destroy(self):
        """Test case for api_variables_destroy

        /variables/:uuid  # noqa: E501
        """
        pass

    def test_api_variables_list(self):
        """Test case for api_variables_list

        /variables  # noqa: E501
        """
        pass

    def test_api_variables_retrieve(self):
        """Test case for api_variables_retrieve

        /variables/:uuid  # noqa: E501
        """
        pass

    def test_api_variables_update(self):
        """Test case for api_variables_update

        /variables/:uuid  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
