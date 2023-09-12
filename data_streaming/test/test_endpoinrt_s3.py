# coding: utf-8

"""
    Data Streaming - OpenAPI

    The Data Streaming API allows you to manage your existing data streamings and templates. Data Streaming allows you to feed your stream processing, SIEM, and big data platforms with the event logs from your applications on Azion in real time. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import data_streaming
from data_streaming.models.endpoinrt_s3 import EndpoinrtS3  # noqa: E501
from data_streaming.rest import ApiException

class TestEndpoinrtS3(unittest.TestCase):
    """EndpoinrtS3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EndpoinrtS3
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EndpoinrtS3`
        """
        model = data_streaming.models.endpoinrt_s3.EndpoinrtS3()  # noqa: E501
        if include_optional :
            return EndpoinrtS3(
                endpoint_type = 's3', 
                access_key = '', 
                region = '', 
                object_key_prefix = '', 
                bucket_name = '', 
                content_type = '', 
                host_url = '', 
                secret_key = ''
            )
        else :
            return EndpoinrtS3(
        )
        """

    def testEndpoinrtS3(self):
        """Test EndpoinrtS3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
