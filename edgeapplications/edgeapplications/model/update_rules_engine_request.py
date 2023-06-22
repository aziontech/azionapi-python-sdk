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


class UpdateRulesEngineRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "behaviors",
            "criteria",
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
            
            
            class criteria(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['RulesEngineCriteria']:
                                return RulesEngineCriteria
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple['RulesEngineCriteria'], typing.List['RulesEngineCriteria']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'RulesEngineCriteria':
                            return super().__getitem__(i)
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, list, tuple, ]], typing.List[typing.Union[MetaOapg.items, list, tuple, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'criteria':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class behaviors(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['RulesEngineBehavior']:
                        return RulesEngineBehavior
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['RulesEngineBehavior'], typing.List['RulesEngineBehavior']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'behaviors':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'RulesEngineBehavior':
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "criteria": criteria,
                "behaviors": behaviors,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    behaviors: MetaOapg.properties.behaviors
    criteria: MetaOapg.properties.criteria
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["behaviors"]) -> MetaOapg.properties.behaviors: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["criteria"]) -> MetaOapg.properties.criteria: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["behaviors"], typing_extensions.Literal["criteria"], typing_extensions.Literal["name"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["behaviors"]) -> MetaOapg.properties.behaviors: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["criteria"]) -> MetaOapg.properties.criteria: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["behaviors"], typing_extensions.Literal["criteria"], typing_extensions.Literal["name"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        behaviors: typing.Union[MetaOapg.properties.behaviors, list, tuple, ],
        criteria: typing.Union[MetaOapg.properties.criteria, list, tuple, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'UpdateRulesEngineRequest':
        return super().__new__(
            cls,
            *_args,
            behaviors=behaviors,
            criteria=criteria,
            name=name,
            _configuration=_configuration,
        )

from edgeapplications.model.rules_engine_behavior import RulesEngineBehavior
from edgeapplications.model.rules_engine_criteria import RulesEngineCriteria
