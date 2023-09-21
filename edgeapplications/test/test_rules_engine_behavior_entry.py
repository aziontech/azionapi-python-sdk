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

from edgeapplications.models.rules_engine_behavior_entry import RulesEngineBehaviorEntry  # noqa: E501

class TestRulesEngineBehaviorEntry(unittest.TestCase):
    """RulesEngineBehaviorEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RulesEngineBehaviorEntry:
        """Test RulesEngineBehaviorEntry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RulesEngineBehaviorEntry`
        """
        model = RulesEngineBehaviorEntry()  # noqa: E501
        if include_optional:
            return RulesEngineBehaviorEntry(
                name = '',
                target = edgeapplications.models.rules_engine_behavior_object_target.RulesEngineBehaviorObject_target(
                    captured_array = '', 
                    subject = '', 
                    regex = '', )
            )
        else:
            return RulesEngineBehaviorEntry(
                name = '',
                target = edgeapplications.models.rules_engine_behavior_object_target.RulesEngineBehaviorObject_target(
                    captured_array = '', 
                    subject = '', 
                    regex = '', ),
        )
        """

    def testRulesEngineBehaviorEntry(self):
        """Test RulesEngineBehaviorEntry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
