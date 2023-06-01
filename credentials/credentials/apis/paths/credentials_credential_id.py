from credentials.paths.credentials_credential_id.get import ApiForget
from credentials.paths.credentials_credential_id.delete import ApiFordelete
from credentials.paths.credentials_credential_id.patch import ApiForpatch


class CredentialsCredentialId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
