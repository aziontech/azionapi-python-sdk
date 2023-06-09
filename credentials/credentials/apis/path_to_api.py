import typing_extensions

from credentials.paths import PathValues
from credentials.apis.paths.credentials import Credentials
from credentials.apis.paths.credentials_credential_id import CredentialsCredentialId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.CREDENTIALS: Credentials,
        PathValues.CREDENTIALS_CREDENTIAL_ID: CredentialsCredentialId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.CREDENTIALS: Credentials,
        PathValues.CREDENTIALS_CREDENTIAL_ID: CredentialsCredentialId,
    }
)
