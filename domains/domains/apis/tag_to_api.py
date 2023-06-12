import typing_extensions

from domains.apis.tags import TagValues
from domains.apis.tags.domains_api import DomainsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DOMAINS: DomainsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DOMAINS: DomainsApi,
    }
)
