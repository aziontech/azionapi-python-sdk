import typing_extensions

from realtimepurge.paths import PathValues
from realtimepurge.apis.paths.purge_url import PurgeUrl
from realtimepurge.apis.paths.purge_cachekey import PurgeCachekey
from realtimepurge.apis.paths.purge_wildcard import PurgeWildcard

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.PURGE_URL: PurgeUrl,
        PathValues.PURGE_CACHEKEY: PurgeCachekey,
        PathValues.PURGE_WILDCARD: PurgeWildcard,
    }
)

path_to_api = PathToApi(
    {
        PathValues.PURGE_URL: PurgeUrl,
        PathValues.PURGE_CACHEKEY: PurgeCachekey,
        PathValues.PURGE_WILDCARD: PurgeWildcard,
    }
)
