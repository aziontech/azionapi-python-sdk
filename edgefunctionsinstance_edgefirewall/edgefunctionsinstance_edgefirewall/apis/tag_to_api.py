import typing_extensions

from edgefunctionsinstance_edgefirewall.apis.tags import TagValues
from edgefunctionsinstance_edgefirewall.apis.tags.default_api import DefaultApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DEFAULT: DefaultApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DEFAULT: DefaultApi,
    }
)
