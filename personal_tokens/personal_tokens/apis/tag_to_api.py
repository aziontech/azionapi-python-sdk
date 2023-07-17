import typing_extensions

from personal_tokens.apis.tags import TagValues
from personal_tokens.apis.tags.personal_token_api import PersonalTokenApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PERSONAL_TOKEN: PersonalTokenApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PERSONAL_TOKEN: PersonalTokenApi,
    }
)
