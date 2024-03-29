# coding: utf-8

"""
    Edge Firewall API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from edgefirewall.models.simple_argument_behavior import SimpleArgumentBehavior  # noqa: E501

class TestSimpleArgumentBehavior(unittest.TestCase):
    """SimpleArgumentBehavior unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SimpleArgumentBehavior:
        """Test SimpleArgumentBehavior
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SimpleArgumentBehavior`
        """
        model = SimpleArgumentBehavior()  # noqa: E501
        if include_optional:
            return SimpleArgumentBehavior(
                name = 'run_function',
                argument = None
            )
        else:
            return SimpleArgumentBehavior(
        )
        """

    def testSimpleArgumentBehavior(self):
        """Test SimpleArgumentBehavior"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
