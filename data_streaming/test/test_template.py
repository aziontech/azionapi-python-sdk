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
from data_streaming.models.template import Template  # noqa: E501
from data_streaming.rest import ApiException

class TestTemplate(unittest.TestCase):
    """Template unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Template
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Template`
        """
        model = data_streaming.models.template.Template()  # noqa: E501
        if include_optional :
            return Template(
                id = 56, 
                name = '', 
                template_model = ''
            )
        else :
            return Template(
        )
        """

    def testTemplate(self):
        """Test Template"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
