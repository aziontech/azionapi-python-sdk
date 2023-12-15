# coding: utf-8

"""
    Object Storage

    REST API OpenAPI documentation for the Object Storage

    The version of the OpenAPI document: 1.0.0 (v1)
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from storage.models.bucket_object import BucketObject

class TestBucketObject(unittest.TestCase):
    """BucketObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BucketObject:
        """Test BucketObject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BucketObject`
        """
        model = BucketObject()
        if include_optional:
            return BucketObject(
                key = '',
                last_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                size = 56,
                etag = ''
            )
        else:
            return BucketObject(
                key = '',
                last_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                size = 56,
                etag = '',
        )
        """

    def testBucketObject(self):
        """Test BucketObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
