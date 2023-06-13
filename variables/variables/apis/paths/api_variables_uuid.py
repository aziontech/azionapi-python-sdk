from variables.paths.api_variables_uuid.get import ApiForget
from variables.paths.api_variables_uuid.put import ApiForput
from variables.paths.api_variables_uuid.delete import ApiFordelete


class ApiVariablesUuid(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
