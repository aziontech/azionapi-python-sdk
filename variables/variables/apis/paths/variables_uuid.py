from variables.paths.variables_uuid.get import ApiForget
from variables.paths.variables_uuid.put import ApiForput
from variables.paths.variables_uuid.delete import ApiFordelete


class VariablesUuid(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
