# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import personal_tokens
from personal_tokens.paths.iam_personal_tokens_personal_token_id import get  # noqa: E501
from personal_tokens import configuration, schemas, api_client

from .. import ApiTestMixin


class TestIamPersonalTokensPersonalTokenId(ApiTestMixin, unittest.TestCase):
    """
    IamPersonalTokensPersonalTokenId unit test stubs
        Get a personal token info  # noqa: E501
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