# coding: utf-8

"""
    Web Application Firewall API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from waf.api.waf_api import WAFApi  # noqa: E501


class TestWAFApi(unittest.TestCase):
    """WAFApi unit test stubs"""

    def setUp(self) -> None:
        self.api = WAFApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_create_new_waf_ruleset(self) -> None:
        """Test case for create_new_waf_ruleset

        Create a new WAF Rule Set in an account.  # noqa: E501
        """
        pass

    def test_delete_waf_ruleset(self) -> None:
        """Test case for delete_waf_ruleset

        Remove an WAF Rule Set from an account. Warning: this action cannot be undone.  # noqa: E501
        """
        pass

    def test_get_waf_domains(self) -> None:
        """Test case for get_waf_domains

        List all domains attached to a Web Application Firewall (WAF) in an account.  # noqa: E501
        """
        pass

    def test_get_waf_events(self) -> None:
        """Test case for get_waf_events

        Find WAF log events  # noqa: E501
        """
        pass

    def test_get_waf_ruleset(self) -> None:
        """Test case for get_waf_ruleset

        List a specific Rule Set associated to a Web Application Firewall (WAF) in an account.  # noqa: E501
        """
        pass

    def test_list_all_waf(self) -> None:
        """Test case for list_all_waf

        List all Web Application Firewalls (WAFs) created in an account  # noqa: E501
        """
        pass

    def test_list_all_waf_rulesets(self) -> None:
        """Test case for list_all_waf_rulesets

        list all Rule Sets associated to a Web Application Firewall (WAF) in an account.  # noqa: E501
        """
        pass

    def test_update_waf_ruleset(self) -> None:
        """Test case for update_waf_ruleset

        Change only select settings of a WAF Rule Set  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
