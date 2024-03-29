# coding: utf-8

"""
    Edge Firewall API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from edgefirewall.api.default_api import DefaultApi  # noqa: E501


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_edge_firewall_edge_firewall_id_rules_engine_get(self) -> None:
        """Test case for edge_firewall_edge_firewall_id_rules_engine_get

        List all rule sets.  # noqa: E501
        """
        pass

    def test_edge_firewall_edge_firewall_id_rules_engine_post(self) -> None:
        """Test case for edge_firewall_edge_firewall_id_rules_engine_post

        Create rule set.  # noqa: E501
        """
        pass

    def test_edge_firewall_edge_firewall_id_rules_engine_rule_set_id_delete(self) -> None:
        """Test case for edge_firewall_edge_firewall_id_rules_engine_rule_set_id_delete

        Delete rule set.  # noqa: E501
        """
        pass

    def test_edge_firewall_edge_firewall_id_rules_engine_rule_set_id_get(self) -> None:
        """Test case for edge_firewall_edge_firewall_id_rules_engine_rule_set_id_get

        Retrieve rule set by ID.  # noqa: E501
        """
        pass

    def test_edge_firewall_edge_firewall_id_rules_engine_rule_set_id_patch(self) -> None:
        """Test case for edge_firewall_edge_firewall_id_rules_engine_rule_set_id_patch

        Edit rule set.  # noqa: E501
        """
        pass

    def test_edge_firewall_edge_firewall_id_rules_engine_rule_set_id_put(self) -> None:
        """Test case for edge_firewall_edge_firewall_id_rules_engine_rule_set_id_put

        Overwrite rule set  # noqa: E501
        """
        pass

    def test_edge_firewall_get(self) -> None:
        """Test case for edge_firewall_get

        List all user edge firewall  # noqa: E501
        """
        pass

    def test_edge_firewall_post(self) -> None:
        """Test case for edge_firewall_post

        Create a edge firewall  # noqa: E501
        """
        pass

    def test_edge_firewall_uuid_delete(self) -> None:
        """Test case for edge_firewall_uuid_delete

        Delete an edge firewall by uuid  # noqa: E501
        """
        pass

    def test_edge_firewall_uuid_get(self) -> None:
        """Test case for edge_firewall_uuid_get

        Retrieve an edge firewall set by uuid  # noqa: E501
        """
        pass

    def test_edge_firewall_uuid_patch(self) -> None:
        """Test case for edge_firewall_uuid_patch

        Update some edge firewall attributes, like \"active\"  # noqa: E501
        """
        pass

    def test_edge_firewall_uuid_put(self) -> None:
        """Test case for edge_firewall_uuid_put

        Overwrite some edge firewall attributes, like \"active\"  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
