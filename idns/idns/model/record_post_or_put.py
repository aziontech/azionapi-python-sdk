# coding: utf-8

"""
    Intelligent DNS

    Azion Intelligent DNS API  # noqa: E501

    The version of the OpenAPI document: 3.0.0
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

from idns import schemas  # noqa: F401


class RecordPostOrPut(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.IntSchema
            entry = schemas.StrSchema
            description = schemas.StrSchema
            
            
            class answers_list(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'answers_list':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            policy = schemas.StrSchema
            weight = schemas.IntSchema
            record_type = schemas.StrSchema
            ttl = schemas.IntSchema
            __annotations__ = {
                "id": id,
                "entry": entry,
                "description": description,
                "answers_list": answers_list,
                "policy": policy,
                "weight": weight,
                "record_type": record_type,
                "ttl": ttl,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entry"]) -> MetaOapg.properties.entry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["answers_list"]) -> MetaOapg.properties.answers_list: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["policy"]) -> MetaOapg.properties.policy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weight"]) -> MetaOapg.properties.weight: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["record_type"]) -> MetaOapg.properties.record_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ttl"]) -> MetaOapg.properties.ttl: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "entry", "description", "answers_list", "policy", "weight", "record_type", "ttl", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entry"]) -> typing.Union[MetaOapg.properties.entry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["answers_list"]) -> typing.Union[MetaOapg.properties.answers_list, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["policy"]) -> typing.Union[MetaOapg.properties.policy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weight"]) -> typing.Union[MetaOapg.properties.weight, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["record_type"]) -> typing.Union[MetaOapg.properties.record_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ttl"]) -> typing.Union[MetaOapg.properties.ttl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "entry", "description", "answers_list", "policy", "weight", "record_type", "ttl", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        entry: typing.Union[MetaOapg.properties.entry, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        answers_list: typing.Union[MetaOapg.properties.answers_list, list, tuple, schemas.Unset] = schemas.unset,
        policy: typing.Union[MetaOapg.properties.policy, str, schemas.Unset] = schemas.unset,
        weight: typing.Union[MetaOapg.properties.weight, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        record_type: typing.Union[MetaOapg.properties.record_type, str, schemas.Unset] = schemas.unset,
        ttl: typing.Union[MetaOapg.properties.ttl, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RecordPostOrPut':
        return super().__new__(
            cls,
            *_args,
            id=id,
            entry=entry,
            description=description,
            answers_list=answers_list,
            policy=policy,
            weight=weight,
            record_type=record_type,
            ttl=ttl,
            _configuration=_configuration,
            **kwargs,
        )
