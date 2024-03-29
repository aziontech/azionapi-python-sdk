# coding: utf-8

"""
    Variables API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from variables.paths.variables.post import ApiVariablesCreate
from variables.paths.variables_uuid.delete import ApiVariablesDestroy
from variables.paths.variables.get import ApiVariablesList
from variables.paths.variables_uuid.get import ApiVariablesRetrieve
from variables.paths.variables_uuid.put import ApiVariablesUpdate


class VariablesApi(
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
