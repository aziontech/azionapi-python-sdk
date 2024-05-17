# coding: utf-8

"""
    Domain API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from domains.models.domain_data_response import DomainDataResponse

class TestDomainDataResponse(unittest.TestCase):
    """DomainDataResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DomainDataResponse:
        """Test DomainDataResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DomainDataResponse`
        """
        model = DomainDataResponse()
        if include_optional:
            return DomainDataResponse(
                name = 'L0',
                cnames = [
                    ''
                    ],
                cname_access_only = True,
                is_active = True,
                edge_application_id = 1,
                digital_certificate_id = 1,
                environment = 'production',
                is_mtls_enabled = True,
                mtls_trusted_ca_certificate_id = 56,
                edge_firewall_id = 56,
                mtls_verification = 'enforce',
                crl_list = [
                    56
                    ]
            )
        else:
            return DomainDataResponse(
        )
        """

    def testDomainDataResponse(self):
        """Test DomainDataResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
