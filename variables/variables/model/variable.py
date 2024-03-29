# coding: utf-8

"""
    Variables API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
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

from variables import schemas  # noqa: F401


class Variable(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "updated_at",
            "last_editor",
            "created_at",
            "secret",
            "uuid",
            "value",
            "key",
        }
        
        class properties:
            uuid = schemas.UUIDSchema
            
            
            class key(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
                    min_length = 1
            
            
            class value(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 32768
                    min_length = 1
            secret = schemas.BoolSchema
            last_editor = schemas.StrSchema
            created_at = schemas.DateTimeSchema
            updated_at = schemas.DateTimeSchema
            __annotations__ = {
                "uuid": uuid,
                "key": key,
                "value": value,
                "secret": secret,
                "last_editor": last_editor,
                "created_at": created_at,
                "updated_at": updated_at,
            }
    
    updated_at: MetaOapg.properties.updated_at
    last_editor: MetaOapg.properties.last_editor
    created_at: MetaOapg.properties.created_at
    secret: MetaOapg.properties.secret
    uuid: MetaOapg.properties.uuid
    value: MetaOapg.properties.value
    key: MetaOapg.properties.key
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secret"]) -> MetaOapg.properties.secret: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_editor"]) -> MetaOapg.properties.last_editor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["uuid", "key", "value", "secret", "last_editor", "created_at", "updated_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secret"]) -> MetaOapg.properties.secret: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_editor"]) -> MetaOapg.properties.last_editor: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["uuid", "key", "value", "secret", "last_editor", "created_at", "updated_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, ],
        last_editor: typing.Union[MetaOapg.properties.last_editor, str, ],
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, ],
        secret: typing.Union[MetaOapg.properties.secret, bool, ],
        uuid: typing.Union[MetaOapg.properties.uuid, str, uuid.UUID, ],
        value: typing.Union[MetaOapg.properties.value, str, ],
        key: typing.Union[MetaOapg.properties.key, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Variable':
        return super().__new__(
            cls,
            *_args,
            updated_at=updated_at,
            last_editor=last_editor,
            created_at=created_at,
            secret=secret,
            uuid=uuid,
            value=value,
            key=key,
            _configuration=_configuration,
            **kwargs,
        )
