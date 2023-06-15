import typing_extensions

from variables.apis.tags import TagValues
from variables.apis.tags.variables_api import VariablesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.VARIABLES: VariablesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.VARIABLES: VariablesApi,
    }
)
