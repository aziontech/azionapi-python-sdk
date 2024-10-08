# coding: utf-8

"""
    Object Storage

    REST API OpenAPI documentation for the Object Storage

    The version of the OpenAPI document: 1.0.0 (v1)
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from storage.models.paginated_s3_credential_list import PaginatedS3CredentialList

class TestPaginatedS3CredentialList(unittest.TestCase):
    """PaginatedS3CredentialList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedS3CredentialList:
        """Test PaginatedS3CredentialList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedS3CredentialList`
        """
        model = PaginatedS3CredentialList()
        if include_optional:
            return PaginatedS3CredentialList(
                count = 123,
                next = 'http://api.example.org/accounts/?page=4',
                previous = 'http://api.example.org/accounts/?page=2',
                results = [
                    storage.models.s3_credential.S3Credential(
                        name = 'my-s3-credential-all-permissions', 
                        access_key = 's3_credential_access_key', 
                        secret_key = 's3_credential_secret_key', 
                        capabilities = ["listAllBucketNames","listBuckets","listFiles","readFiles","writeFiles","deleteFiles"], 
                        bucket = 's3-credentials-bucket', 
                        expiration_date = '2025-01-31T10:57Z', 
                        created_at = '2024-03-04T16:54:14.782211Z', )
                    ]
            )
        else:
            return PaginatedS3CredentialList(
        )
        """

    def testPaginatedS3CredentialList(self):
        """Test PaginatedS3CredentialList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
