# coding: utf-8

"""
    Domain API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from domains.models.domain_links import DomainLinks

class TestDomainLinks(unittest.TestCase):
    """DomainLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DomainLinks:
        """Test DomainLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DomainLinks`
        """
        model = DomainLinks()
        if include_optional:
            return DomainLinks(
                previous = '',
                next = ''
            )
        else:
            return DomainLinks(
                previous = '',
                next = '',
        )
        """

    def testDomainLinks(self):
        """Test DomainLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
