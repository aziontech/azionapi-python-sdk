# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import data_streaming
from data_streaming.paths.data_streaming_streamings_data_streaming_id import get  # noqa: E501
from data_streaming import configuration, schemas, api_client

from .. import ApiTestMixin


class TestDataStreamingStreamingsDataStreamingId(ApiTestMixin, unittest.TestCase):
    """
    DataStreamingStreamingsDataStreamingId unit test stubs
        Get expecific data streaming by Data Streaming ID  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
