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
from data_streaming.models.create_custom_data_streaming_response import CreateCustomDataStreamingResponse  # noqa: E501
from data_streaming.rest import ApiException

class TestCreateCustomDataStreamingResponse(unittest.TestCase):
    """CreateCustomDataStreamingResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateCustomDataStreamingResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateCustomDataStreamingResponse`
        """
        model = data_streaming.models.create_custom_data_streaming_response.CreateCustomDataStreamingResponse()  # noqa: E501
        if include_optional :
            return CreateCustomDataStreamingResponse(
                results = [
                    data_streaming.models.post_custom_data_streaming_response.PostCustomDataStreamingResponse(
                        id = 56, 
                        name = '', 
                        data_source = 'http', 
                        template_model = '"{\"custom_template_field\":\"$custom_value\", \"status\":\"$status\"}"
 
', 
                        active = True, 
                        endpoint = '', 
                        all_domains = True, )
                    ], 
                schema_version = 1.337
            )
        else :
            return CreateCustomDataStreamingResponse(
        )
        """

    def testCreateCustomDataStreamingResponse(self):
        """Test CreateCustomDataStreamingResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
