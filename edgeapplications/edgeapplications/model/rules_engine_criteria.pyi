# coding: utf-8

"""
    Edge Application API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from edgeapplications import schemas  # noqa: F401


class RulesEngineCriteria(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "conditional",
            "variable",
            "operator",
        }
        
        class properties:
            conditional = schemas.StrSchema
            variable = schemas.StrSchema
            operator = schemas.StrSchema
            input_value = schemas.StrSchema
            __annotations__ = {
                "conditional": conditional,
                "variable": variable,
                "operator": operator,
                "input_value": input_value,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    conditional: MetaOapg.properties.conditional
    variable: MetaOapg.properties.variable
    operator: MetaOapg.properties.operator
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conditional"]) -> MetaOapg.properties.conditional: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["variable"]) -> MetaOapg.properties.variable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operator"]) -> MetaOapg.properties.operator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["input_value"]) -> MetaOapg.properties.input_value: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["conditional"], typing_extensions.Literal["variable"], typing_extensions.Literal["operator"], typing_extensions.Literal["input_value"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conditional"]) -> MetaOapg.properties.conditional: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["variable"]) -> MetaOapg.properties.variable: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operator"]) -> MetaOapg.properties.operator: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["input_value"]) -> typing.Union[MetaOapg.properties.input_value, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["conditional"], typing_extensions.Literal["variable"], typing_extensions.Literal["operator"], typing_extensions.Literal["input_value"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        conditional: typing.Union[MetaOapg.properties.conditional, str, ],
        variable: typing.Union[MetaOapg.properties.variable, str, ],
        operator: typing.Union[MetaOapg.properties.operator, str, ],
        input_value: typing.Union[MetaOapg.properties.input_value, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'RulesEngineCriteria':
        return super().__new__(
            cls,
            *_args,
            conditional=conditional,
            variable=variable,
            operator=operator,
            input_value=input_value,
            _configuration=_configuration,
        )
