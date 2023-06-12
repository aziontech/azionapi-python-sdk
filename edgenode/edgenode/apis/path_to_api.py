import typing_extensions

from edgenode.paths import PathValues
from edgenode.apis.paths.edge_nodes import EdgeNodes
from edgenode.apis.paths.edge_nodes_edgenode_id import EdgeNodesEdgenodeId
from edgenode.apis.paths.edge_nodes_edgenode_id_services import EdgeNodesEdgenodeIdServices
from edgenode.apis.paths.edge_nodes_edgenode_id_services_bind_id import EdgeNodesEdgenodeIdServicesBindId
from edgenode.apis.paths.edge_nodes_authorize import EdgeNodesAuthorize
from edgenode.apis.paths.edge_nodes_groups import EdgeNodesGroups

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.EDGE_NODES: EdgeNodes,
        PathValues.EDGE_NODES_EDGENODE_ID: EdgeNodesEdgenodeId,
        PathValues.EDGE_NODES_EDGENODE_ID_SERVICES: EdgeNodesEdgenodeIdServices,
        PathValues.EDGE_NODES_EDGENODE_ID_SERVICES_BIND_ID: EdgeNodesEdgenodeIdServicesBindId,
        PathValues.EDGE_NODES_AUTHORIZE: EdgeNodesAuthorize,
        PathValues.EDGE_NODES_GROUPS: EdgeNodesGroups,
    }
)

path_to_api = PathToApi(
    {
        PathValues.EDGE_NODES: EdgeNodes,
        PathValues.EDGE_NODES_EDGENODE_ID: EdgeNodesEdgenodeId,
        PathValues.EDGE_NODES_EDGENODE_ID_SERVICES: EdgeNodesEdgenodeIdServices,
        PathValues.EDGE_NODES_EDGENODE_ID_SERVICES_BIND_ID: EdgeNodesEdgenodeIdServicesBindId,
        PathValues.EDGE_NODES_AUTHORIZE: EdgeNodesAuthorize,
        PathValues.EDGE_NODES_GROUPS: EdgeNodesGroups,
    }
)
