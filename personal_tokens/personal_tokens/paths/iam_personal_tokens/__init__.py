# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from personal_tokens.paths.iam_personal_tokens import Api

from personal_tokens.paths import PathValues

path = PathValues.IAM_PERSONAL_TOKENS