# coding: utf-8

"""
    Object Storage

    REST API OpenAPI documentation for the Object Storage

    The version of the OpenAPI document: 1.0.0 (v1)
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from storage.models.s3_credential_create import S3CredentialCreate

class TestS3CredentialCreate(unittest.TestCase):
    """S3CredentialCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> S3CredentialCreate:
        """Test S3CredentialCreate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `S3CredentialCreate`
        """
        model = S3CredentialCreate()
        if include_optional:
            return S3CredentialCreate(
                name = 'my-s3-credential-all-permissions',
                capabilities = ["listAllBucketNames","listBuckets","listFiles","readFiles","writeFiles","deleteFiles"],
                bucket = 's3-credentials-bucket',
                expiration_date = '2025-01-31T10:57Z'
            )
        else:
            return S3CredentialCreate(
        )
        """

    def testS3CredentialCreate(self):
        """Test S3CredentialCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
