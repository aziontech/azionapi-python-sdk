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
from edgeapplications.models.application_put_result import ApplicationPutResult  # noqa: E501
from edgeapplications.rest import ApiException

class TestApplicationPutResult(unittest.TestCase):
    """ApplicationPutResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApplicationPutResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApplicationPutResult`
        """
        model = edgeapplications.models.application_put_result.ApplicationPutResult()  # noqa: E501
        if include_optional :
            return ApplicationPutResult(
                results = {"load_balancer":true,"application_acceleration":true,"web_application_firewall":true,"device_detection":true,"raw_logs":true,"active":true,"http3":true,"supported_ciphers":"supported_ciphers","debug_rules":true,"delivery_protocol":"delivery_protocol","edge_firewall":true,"caching":true,"http_port":[6],"https_port":[1],"minimum_tls_version":"minimum_tls_version","name":"name","edge_functions":true,"l2_caching":true,"id":0,"image_optimization":true}, 
                schema_version = 56
            )
        else :
            return ApplicationPutResult(
                results = {"load_balancer":true,"application_acceleration":true,"web_application_firewall":true,"device_detection":true,"raw_logs":true,"active":true,"http3":true,"supported_ciphers":"supported_ciphers","debug_rules":true,"delivery_protocol":"delivery_protocol","edge_firewall":true,"caching":true,"http_port":[6],"https_port":[1],"minimum_tls_version":"minimum_tls_version","name":"name","edge_functions":true,"l2_caching":true,"id":0,"image_optimization":true},
                schema_version = 56,
        )
        """

    def testApplicationPutResult(self):
        """Test ApplicationPutResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()