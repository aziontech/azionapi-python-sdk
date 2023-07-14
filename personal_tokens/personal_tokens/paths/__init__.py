# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from personal_tokens.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    IAM_PERSONAL_TOKENS = "/iam/personal_tokens"
    IAM_PERSONAL_TOKENS_PERSONAL_TOKEN_ID = "/iam/personal_tokens/{personalTokenId}"
