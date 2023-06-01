from edgenode.paths.edge_nodes_edgenode_id.get import ApiForget
from edgenode.paths.edge_nodes_edgenode_id.delete import ApiFordelete
from edgenode.paths.edge_nodes_edgenode_id.patch import ApiForpatch


class EdgeNodesEdgenodeId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
