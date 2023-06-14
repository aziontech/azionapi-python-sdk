import typing_extensions

from networklist.paths import PathValues
from networklist.apis.paths.network_lists import NetworkLists
from networklist.apis.paths.network_lists_uuid import NetworkListsUuid

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.NETWORK_LISTS: NetworkLists,
        PathValues.NETWORK_LISTS_UUID: NetworkListsUuid,
    }
)

path_to_api = PathToApi(
    {
        PathValues.NETWORK_LISTS: NetworkLists,
        PathValues.NETWORK_LISTS_UUID: NetworkListsUuid,
    }
)
