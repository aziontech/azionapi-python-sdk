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

import edgeapplications
from edgeapplications.models.application_results_create import ApplicationResultsCreate  # noqa: E501
from edgeapplications.rest import ApiException

class TestApplicationResultsCreate(unittest.TestCase):
    """ApplicationResultsCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApplicationResultsCreate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApplicationResultsCreate`
        """
        model = edgeapplications.models.application_results_create.ApplicationResultsCreate()  # noqa: E501
        if include_optional :
            return ApplicationResultsCreate(
                id = 56, 
                name = '', 
                active = True, 
                debug_rules = True, 
                http3 = True, 
                supported_ciphers = '', 
                delivery_protocol = '', 
                http_port = None, 
                https_port = None, 
                minimum_tls_version = '', 
                application_acceleration = True, 
                caching = True, 
                device_detection = True, 
                edge_firewall = True, 
                edge_functions = True, 
                image_optimization = True, 
                load_balancer = True, 
                raw_logs = True, 
                web_application_firewall = True, 
                l2_caching = True
            )
        else :
            return ApplicationResultsCreate(
                id = 56,
                name = '',
                active = True,
                debug_rules = True,
                http3 = True,
                supported_ciphers = '',
                delivery_protocol = '',
                http_port = None,
                https_port = None,
                minimum_tls_version = '',
                application_acceleration = True,
                caching = True,
                device_detection = True,
                edge_firewall = True,
                edge_functions = True,
                image_optimization = True,
                load_balancer = True,
                raw_logs = True,
                web_application_firewall = True,
        )
        """

    def testApplicationResultsCreate(self):
        """Test ApplicationResultsCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
