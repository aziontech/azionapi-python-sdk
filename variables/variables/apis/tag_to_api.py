import typing_extensions

from variables.apis.tags import TagValues
from variables.apis.tags.api_api import ApiApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.API: ApiApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.API: ApiApi,
    }
)
