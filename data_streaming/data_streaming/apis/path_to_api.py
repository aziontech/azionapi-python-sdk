import typing_extensions

from data_streaming.paths import PathValues
from data_streaming.apis.paths.data_streaming_streamings import DataStreamingStreamings
from data_streaming.apis.paths.data_streaming_domains import DataStreamingDomains
from data_streaming.apis.paths.data_streaming_streamings_data_streaming_id import DataStreamingStreamingsDataStreamingId
from data_streaming.apis.paths.data_streaming_templates import DataStreamingTemplates
from data_streaming.apis.paths.data_streaming_templates_template_id import DataStreamingTemplatesTemplateId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.DATA_STREAMING_STREAMINGS: DataStreamingStreamings,
        PathValues.DATA_STREAMING_DOMAINS: DataStreamingDomains,
        PathValues.DATA_STREAMING_STREAMINGS_DATA_STREAMING_ID: DataStreamingStreamingsDataStreamingId,
        PathValues.DATA_STREAMING_TEMPLATES: DataStreamingTemplates,
        PathValues.DATA_STREAMING_TEMPLATES_TEMPLATE_ID: DataStreamingTemplatesTemplateId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.DATA_STREAMING_STREAMINGS: DataStreamingStreamings,
        PathValues.DATA_STREAMING_DOMAINS: DataStreamingDomains,
        PathValues.DATA_STREAMING_STREAMINGS_DATA_STREAMING_ID: DataStreamingStreamingsDataStreamingId,
        PathValues.DATA_STREAMING_TEMPLATES: DataStreamingTemplates,
        PathValues.DATA_STREAMING_TEMPLATES_TEMPLATE_ID: DataStreamingTemplatesTemplateId,
    }
)
