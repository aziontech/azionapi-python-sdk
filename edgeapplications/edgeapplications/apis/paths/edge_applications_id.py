from edgeapplications.paths.edge_applications_id.get import ApiForget
from edgeapplications.paths.edge_applications_id.put import ApiForput
from edgeapplications.paths.edge_applications_id.delete import ApiFordelete
from edgeapplications.paths.edge_applications_id.patch import ApiForpatch


class EdgeApplicationsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
