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

from edgefirewall.models.ssl_verification_status_criteria import SSLVerificationStatusCriteria  # noqa: E501

class TestSSLVerificationStatusCriteria(unittest.TestCase):
    """SSLVerificationStatusCriteria unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SSLVerificationStatusCriteria:
        """Test SSLVerificationStatusCriteria
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SSLVerificationStatusCriteria`
        """
        model = SSLVerificationStatusCriteria()  # noqa: E501
        if include_optional:
            return SSLVerificationStatusCriteria(
                variable = 'header_accept',
                operator = 'is_equal',
                conditional = 'if',
                input_value = 'SUCCESS'
            )
        else:
            return SSLVerificationStatusCriteria(
        )
        """

    def testSSLVerificationStatusCriteria(self):
        """Test SSLVerificationStatusCriteria"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
