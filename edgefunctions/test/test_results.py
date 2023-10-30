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

from edgefunctions.models.results import Results  # noqa: E501

class TestResults(unittest.TestCase):
    """Results unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Results:
        """Test Results
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Results`
        """
        model = Results()  # noqa: E501
        if include_optional:
            return Results(
                id = 56,
                name = '',
                language = '',
                code = '',
                json_args = None,
                function_to_run = '',
                initiator_type = '',
                active = True,
                last_editor = '',
                modified = '',
                reference_count = 56,
                is_proprietary_code = True
            )
        else:
            return Results(
        )
        """

    def testResults(self):
        """Test Results"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()