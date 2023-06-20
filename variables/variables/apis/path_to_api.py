import typing_extensions

from variables.paths import PathValues
from variables.apis.paths.api_variables import ApiVariables
from variables.apis.paths.api_variables_uuid import ApiVariablesUuid

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_VARIABLES: ApiVariables,
        PathValues.API_VARIABLES_UUID: ApiVariablesUuid,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_VARIABLES: ApiVariables,
        PathValues.API_VARIABLES_UUID: ApiVariablesUuid,
    }
)
