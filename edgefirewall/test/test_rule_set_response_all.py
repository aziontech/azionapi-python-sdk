# coding: utf-8

"""
    Edge Firewall API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from edgefirewall.models.rule_set_response_all import RuleSetResponseAll  # noqa: E501

class TestRuleSetResponseAll(unittest.TestCase):
    """RuleSetResponseAll unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RuleSetResponseAll:
        """Test RuleSetResponseAll
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RuleSetResponseAll`
        """
        model = RuleSetResponseAll()  # noqa: E501
        if include_optional:
            return RuleSetResponseAll(
                count = 0,
                total_pages = 0,
                schema_version = 56,
                links = {"next":"next","previous":"previous"},
                results = [
                    edgefirewall.models.rule_set_result_all.RuleSetResultAll(
                        id = 1, 
                        last_editor = '', 
                        last_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        is_active = True, 
                        description = '', 
                        behaviors = [
                            edgefirewall.models.behaviors.Behaviors(
                                name = 'deny', 
                                target = '', )
                            ], 
                        criteria = [
                            [
                                edgefirewall.models.ssl_verification_status_criteria.SSLVerificationStatusCriteria(
                                    variable = 'header_accept', 
                                    operator = 'is_equal', 
                                    conditional = 'if', 
                                    input_value = 'SUCCESS', )
                                ]
                            ], 
                        order = 0, )
                    ]
            )
        else:
            return RuleSetResponseAll(
        )
        """

    def testRuleSetResponseAll(self):
        """Test RuleSetResponseAll"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()