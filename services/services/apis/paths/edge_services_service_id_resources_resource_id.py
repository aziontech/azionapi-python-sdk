from services.paths.edge_services_service_id_resources_resource_id.get import ApiForget
from services.paths.edge_services_service_id_resources_resource_id.delete import ApiFordelete
from services.paths.edge_services_service_id_resources_resource_id.patch import ApiForpatch


class EdgeServicesServiceIdResourcesResourceId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
