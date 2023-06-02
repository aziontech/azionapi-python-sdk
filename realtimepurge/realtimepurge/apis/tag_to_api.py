import typing_extensions

from realtimepurge.apis.tags import TagValues
from realtimepurge.apis.tags.real_time_purge_api import RealTimePurgeApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.REALTIME_PURGE: RealTimePurgeApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.REALTIME_PURGE: RealTimePurgeApi,
    }
)
