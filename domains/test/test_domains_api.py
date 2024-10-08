# coding: utf-8

"""
    Domain API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from domains.api.domains_api import DomainsApi


class TestDomainsApi(unittest.TestCase):
    """DomainsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DomainsApi()

    def tearDown(self) -> None:
        pass

    def test_create_domain(self) -> None:
        """Test case for create_domain

        /domains
        """
        pass

    def test_del_domain(self) -> None:
        """Test case for del_domain

        /domains/:id
        """
        pass

    def test_get_domain(self) -> None:
        """Test case for get_domain

        /domains/:id
        """
        pass

    def test_get_domains(self) -> None:
        """Test case for get_domains

        /domains
        """
        pass

    def test_put_domain(self) -> None:
        """Test case for put_domain

        /domains:/:id
        """
        pass

    def test_update_domain(self) -> None:
        """Test case for update_domain

        /domains/:id
        """
        pass


if __name__ == '__main__':
    unittest.main()
