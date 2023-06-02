import typing_extensions

from edgefunctions.apis.tags import TagValues
from edgefunctions.apis.tags.edge_functions_api import EdgeFunctionsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.EDGE_FUNCTIONS: EdgeFunctionsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.EDGE_FUNCTIONS: EdgeFunctionsApi,
    }
)
