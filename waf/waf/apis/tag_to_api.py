import typing_extensions

from waf.apis.tags import TagValues
from waf.apis.tags.waf_api import WAFApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.WAF: WAFApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.WAF: WAFApi,
    }
)
