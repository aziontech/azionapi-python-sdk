# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from services.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    EDGE_SERVICES_ = "/edge_services/"
    EDGE_SERVICES_ID = "/edge_services/{id}"
    EDGE_SERVICES_SERVICE_ID_RESOURCES = "/edge_services/{serviceId}/resources"
    EDGE_SERVICES_SERVICE_ID_RESOURCES_RESOURCE_ID = "/edge_services/{serviceId}/resources/{resourceId}"
