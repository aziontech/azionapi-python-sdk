import typing_extensions

from personal_tokens.paths import PathValues
from personal_tokens.apis.paths.iam_personal_tokens import IamPersonalTokens
from personal_tokens.apis.paths.iam_personal_tokens_personal_token_id import IamPersonalTokensPersonalTokenId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.IAM_PERSONAL_TOKENS: IamPersonalTokens,
        PathValues.IAM_PERSONAL_TOKENS_PERSONAL_TOKEN_ID: IamPersonalTokensPersonalTokenId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.IAM_PERSONAL_TOKENS: IamPersonalTokens,
        PathValues.IAM_PERSONAL_TOKENS_PERSONAL_TOKEN_ID: IamPersonalTokensPersonalTokenId,
    }
)
