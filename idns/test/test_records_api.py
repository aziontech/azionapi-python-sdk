# coding: utf-8

"""
    Intelligent DNS API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from idns.api.records_api import RecordsApi  # noqa: E501


class TestRecordsApi(unittest.TestCase):
    """RecordsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RecordsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_delete_zone_record(self) -> None:
        """Test case for delete_zone_record

        Remove an Intelligent DNS zone record  # noqa: E501
        """
        pass

    def test_get_zone_records(self) -> None:
        """Test case for get_zone_records

        Get a collection of Intelligent DNS zone records  # noqa: E501
        """
        pass

    def test_post_zone_record(self) -> None:
        """Test case for post_zone_record

        Create a new Intelligent DNS zone record  # noqa: E501
        """
        pass

    def test_put_zone_record(self) -> None:
        """Test case for put_zone_record

        Update an Intelligent DNS zone record  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
