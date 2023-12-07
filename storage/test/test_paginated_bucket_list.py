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

from storage.models.paginated_bucket_list import PaginatedBucketList

class TestPaginatedBucketList(unittest.TestCase):
    """PaginatedBucketList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedBucketList:
        """Test PaginatedBucketList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedBucketList`
        """
        model = PaginatedBucketList()
        if include_optional:
            return PaginatedBucketList(
                count = 123,
                next = 'http://api.example.org/accounts/?page=4',
                previous = 'http://api.example.org/accounts/?page=2',
                results = [
                    storage.models.bucket.Bucket(
                        name = '012345', 
                        edge_access = 'read_only', )
                    ]
            )
        else:
            return PaginatedBucketList(
        )
        """

    def testPaginatedBucketList(self):
        """Test PaginatedBucketList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
