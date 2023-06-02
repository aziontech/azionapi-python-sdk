from edgefunctions.paths.edge_functions_id.get import ApiForget
from edgefunctions.paths.edge_functions_id.put import ApiForput
from edgefunctions.paths.edge_functions_id.delete import ApiFordelete
from edgefunctions.paths.edge_functions_id.patch import ApiForpatch


class EdgeFunctionsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
