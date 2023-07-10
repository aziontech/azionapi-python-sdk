import typing_extensions

from variables.paths import PathValues
from variables.apis.paths.variables import Variables
from variables.apis.paths.variables_uuid import VariablesUuid

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.VARIABLES: Variables,
        PathValues.VARIABLES_UUID: VariablesUuid,
    }
)

path_to_api = PathToApi(
    {
        PathValues.VARIABLES: Variables,
        PathValues.VARIABLES_UUID: VariablesUuid,
    }
)
