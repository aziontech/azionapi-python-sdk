# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from edgenode.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    EDGE_NODES = "/edge_nodes"
    EDGE_NODES_EDGENODE_ID = "/edge_nodes/{edgenodeId}"
    EDGE_NODES_EDGENODE_ID_SERVICES = "/edge_nodes/{edgenodeId}/services"
    EDGE_NODES_EDGENODE_ID_SERVICES_BIND_ID = "/edge_nodes/{edgenodeId}/services/{bindId}"
    EDGE_NODES_AUTHORIZE = "/edge_nodes/authorize"
    EDGE_NODES_GROUPS = "/edge_nodes/groups"
