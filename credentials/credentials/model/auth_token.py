# coding: utf-8

"""
    Credentials API

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

from credentials import schemas  # noqa: F401


class AuthToken(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "is_active",
            "updated_at",
            "last_editor",
            "name",
            "created_at",
            "id",
            "client_id",
            "token",
        }
        
        class properties:
            client_id = schemas.StrSchema
            created_at = schemas.DateTimeSchema
            id = schemas.Int64Schema
            is_active = schemas.BoolSchema
            last_editor = schemas.StrSchema
            name = schemas.StrSchema
            token = schemas.StrSchema
            updated_at = schemas.DateTimeSchema
            deleted_at = schemas.DateTimeSchema
            description = schemas.StrSchema
            __annotations__ = {
                "client_id": client_id,
                "created_at": created_at,
                "id": id,
                "is_active": is_active,
                "last_editor": last_editor,
                "name": name,
                "token": token,
                "updated_at": updated_at,
                "deleted_at": deleted_at,
                "description": description,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    is_active: MetaOapg.properties.is_active
    updated_at: MetaOapg.properties.updated_at
    last_editor: MetaOapg.properties.last_editor
    name: MetaOapg.properties.name
    created_at: MetaOapg.properties.created_at
    id: MetaOapg.properties.id
    client_id: MetaOapg.properties.client_id
    token: MetaOapg.properties.token
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_active"]) -> MetaOapg.properties.is_active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_editor"]) -> MetaOapg.properties.last_editor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token"]) -> MetaOapg.properties.token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleted_at"]) -> MetaOapg.properties.deleted_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["is_active"], typing_extensions.Literal["updated_at"], typing_extensions.Literal["last_editor"], typing_extensions.Literal["name"], typing_extensions.Literal["created_at"], typing_extensions.Literal["id"], typing_extensions.Literal["client_id"], typing_extensions.Literal["token"], typing_extensions.Literal["deleted_at"], typing_extensions.Literal["description"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_active"]) -> MetaOapg.properties.is_active: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_editor"]) -> MetaOapg.properties.last_editor: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token"]) -> MetaOapg.properties.token: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleted_at"]) -> typing.Union[MetaOapg.properties.deleted_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["is_active"], typing_extensions.Literal["updated_at"], typing_extensions.Literal["last_editor"], typing_extensions.Literal["name"], typing_extensions.Literal["created_at"], typing_extensions.Literal["id"], typing_extensions.Literal["client_id"], typing_extensions.Literal["token"], typing_extensions.Literal["deleted_at"], typing_extensions.Literal["description"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        is_active: typing.Union[MetaOapg.properties.is_active, bool, ],
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, ],
        last_editor: typing.Union[MetaOapg.properties.last_editor, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        client_id: typing.Union[MetaOapg.properties.client_id, str, ],
        token: typing.Union[MetaOapg.properties.token, str, ],
        deleted_at: typing.Union[MetaOapg.properties.deleted_at, str, datetime, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'AuthToken':
        return super().__new__(
            cls,
            *_args,
            is_active=is_active,
            updated_at=updated_at,
            last_editor=last_editor,
            name=name,
            created_at=created_at,
            id=id,
            client_id=client_id,
            token=token,
            deleted_at=deleted_at,
            description=description,
            _configuration=_configuration,
        )
