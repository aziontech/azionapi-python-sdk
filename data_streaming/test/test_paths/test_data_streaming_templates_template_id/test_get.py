# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import data_streaming
from data_streaming.paths.data_streaming_templates_template_id import get  # noqa: E501
from data_streaming import configuration, schemas, api_client

from .. import ApiTestMixin


class TestDataStreamingTemplatesTemplateId(ApiTestMixin, unittest.TestCase):
    """
    DataStreamingTemplatesTemplateId unit test stubs
        Get an global Template info by template ID  # noqa: E501
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
