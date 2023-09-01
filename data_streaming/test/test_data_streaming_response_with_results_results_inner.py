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
from data_streaming.models.data_streaming_response_with_results_results_inner import DataStreamingResponseWithResultsResultsInner  # noqa: E501
from data_streaming.rest import ApiException

class TestDataStreamingResponseWithResultsResultsInner(unittest.TestCase):
    """DataStreamingResponseWithResultsResultsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DataStreamingResponseWithResultsResultsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataStreamingResponseWithResultsResultsInner`
        """
        model = data_streaming.models.data_streaming_response_with_results_results_inner.DataStreamingResponseWithResultsResultsInner()  # noqa: E501
        if include_optional :
            return DataStreamingResponseWithResultsResultsInner(
                id = 56, 
                name = '', 
                template_id = 56, 
                data_source = '', 
                active = True, 
                endpoint = data_streaming.models.data_streaming_endpoint_type_kafka.DataStreamingEndpointTypeKafka(
                    endpoint_type = '', 
                    use_tls = True, 
                    kafka_topic = '', 
                    bootstrap_servers = '', ), 
                all_domains = True, 
                template_model = ''
            )
        else :
            return DataStreamingResponseWithResultsResultsInner(
        )
        """

    def testDataStreamingResponseWithResultsResultsInner(self):
        """Test DataStreamingResponseWithResultsResultsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
