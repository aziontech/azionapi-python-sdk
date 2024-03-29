# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import digital_certificates
from digital_certificates.paths.digital_certificates_digital_certificate_id import delete  # noqa: E501
from digital_certificates import configuration, schemas, api_client

from .. import ApiTestMixin


class TestDigitalCertificatesDigitalCertificateId(ApiTestMixin, unittest.TestCase):
    """
    DigitalCertificatesDigitalCertificateId unit test stubs
        Remove a digital certificate or CSR from your account  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
