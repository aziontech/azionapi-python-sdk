from networklist.paths.network_lists_uuid.get import ApiForget
from networklist.paths.network_lists_uuid.put import ApiForput
from networklist.paths.network_lists_uuid.delete import ApiFordelete


class NetworkListsUuid(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
