# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Generated by: https://openapi-generator.tech
"""

from variables.paths.api_schema.get import ApiSchemaRetrieve
from variables.paths.api_variables.post import ApiVariablesCreate
from variables.paths.api_variables_uuid.delete import ApiVariablesDestroy
from variables.paths.api_variables.get import ApiVariablesList
from variables.paths.api_variables_uuid.get import ApiVariablesRetrieve
from variables.paths.api_variables_uuid.put import ApiVariablesUpdate


class ApiApi(
    ApiSchemaRetrieve,
    ApiVariablesCreate,
    ApiVariablesDestroy,
    ApiVariablesList,
    ApiVariablesRetrieve,
    ApiVariablesUpdate,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
