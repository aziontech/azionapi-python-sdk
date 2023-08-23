import typing_extensions

from data_streaming.apis.tags import TagValues
from data_streaming.apis.tags.data_streaming_api import DataStreamingApi
from data_streaming.apis.tags.data_streaming_domain_api import DataStreamingDomainApi
from data_streaming.apis.tags.data_streaming_templates_api import DataStreamingTemplatesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DATA_STREAMING: DataStreamingApi,
        TagValues.DATA_STREAMING_DOMAIN: DataStreamingDomainApi,
        TagValues.DATA_STREAMING_TEMPLATES: DataStreamingTemplatesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DATA_STREAMING: DataStreamingApi,
        TagValues.DATA_STREAMING_DOMAIN: DataStreamingDomainApi,
        TagValues.DATA_STREAMING_TEMPLATES: DataStreamingTemplatesApi,
    }
)
