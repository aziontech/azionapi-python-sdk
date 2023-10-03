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

from edgefirewall.models.edge_firewall_response import EdgeFirewallResponse  # noqa: E501

class TestEdgeFirewallResponse(unittest.TestCase):
    """EdgeFirewallResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EdgeFirewallResponse:
        """Test EdgeFirewallResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EdgeFirewallResponse`
        """
        model = EdgeFirewallResponse()  # noqa: E501
        if include_optional:
            return EdgeFirewallResponse(
                results = {"is_active":true,"last_editor":"last_editor","name":"name","waf_enabled":true,"network_protection_enabled":true,"domains":[5,5],"edge_functions_enabled":true,"id":5,"last_modified":"last_modified","debug_rules":true},
                schema_version = 1.337
            )
        else:
            return EdgeFirewallResponse(
        )
        """

    def testEdgeFirewallResponse(self):
        """Test EdgeFirewallResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
