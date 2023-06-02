from services.paths.edge_services_id.get import ApiForget
from services.paths.edge_services_id.delete import ApiFordelete
from services.paths.edge_services_id.patch import ApiForpatch


class EdgeServicesId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
