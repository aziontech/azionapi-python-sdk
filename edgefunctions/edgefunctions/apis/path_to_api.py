import typing_extensions

from edgefunctions.paths import PathValues
from edgefunctions.apis.paths.edge_functions import EdgeFunctions
from edgefunctions.apis.paths.edge_functions_id import EdgeFunctionsId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.EDGE_FUNCTIONS: EdgeFunctions,
        PathValues.EDGE_FUNCTIONS_ID: EdgeFunctionsId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.EDGE_FUNCTIONS: EdgeFunctions,
        PathValues.EDGE_FUNCTIONS_ID: EdgeFunctionsId,
    }
)
