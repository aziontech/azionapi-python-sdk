import typing_extensions

from services.paths import PathValues
from services.apis.paths.edge_services import EdgeServices
from services.apis.paths.edge_services_id import EdgeServicesId
from services.apis.paths.edge_services_service_id_resources import EdgeServicesServiceIdResources
from services.apis.paths.edge_services_service_id_resources_resource_id import EdgeServicesServiceIdResourcesResourceId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.EDGE_SERVICES: EdgeServices,
        PathValues.EDGE_SERVICES_ID: EdgeServicesId,
        PathValues.EDGE_SERVICES_SERVICE_ID_RESOURCES: EdgeServicesServiceIdResources,
        PathValues.EDGE_SERVICES_SERVICE_ID_RESOURCES_RESOURCE_ID: EdgeServicesServiceIdResourcesResourceId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.EDGE_SERVICES: EdgeServices,
        PathValues.EDGE_SERVICES_ID: EdgeServicesId,
        PathValues.EDGE_SERVICES_SERVICE_ID_RESOURCES: EdgeServicesServiceIdResources,
        PathValues.EDGE_SERVICES_SERVICE_ID_RESOURCES_RESOURCE_ID: EdgeServicesServiceIdResourcesResourceId,
    }
)
