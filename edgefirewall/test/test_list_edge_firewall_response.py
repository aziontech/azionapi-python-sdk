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

from edgefirewall.models.list_edge_firewall_response import ListEdgeFirewallResponse  # noqa: E501

class TestListEdgeFirewallResponse(unittest.TestCase):
    """ListEdgeFirewallResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListEdgeFirewallResponse:
        """Test ListEdgeFirewallResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListEdgeFirewallResponse`
        """
        model = ListEdgeFirewallResponse()  # noqa: E501
        if include_optional:
            return ListEdgeFirewallResponse(
                count = 56,
                total_pages = 56,
                schema_version = 56,
                links = {"next":"next","previous":"previous"},
                results = [
                    {"is_active":true,"last_editor":"last_editor","name":"name","waf_enabled":true,"network_protection_enabled":true,"domains":[5,5],"edge_functions_enabled":true,"id":5,"last_modified":"last_modified","debug_rules":true}
                    ]
            )
        else:
            return ListEdgeFirewallResponse(
        )
        """

    def testListEdgeFirewallResponse(self):
        """Test ListEdgeFirewallResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()