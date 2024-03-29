# coding: utf-8

"""
    Network Lists API

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

from networklist import schemas  # noqa: F401


class NetworkLists(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.Int64Schema
            last_editor = schemas.StrSchema
            last_modified = schemas.StrSchema
            list_type = schemas.StrSchema
            name = schemas.StrSchema
            
            
            class country_list(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'country_list':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class ip_list(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ip_list':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "id": id,
                "last_editor": last_editor,
                "last_modified": last_modified,
                "list_type": list_type,
                "name": name,
                "country_list": country_list,
                "ip_list": ip_list,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_editor"]) -> MetaOapg.properties.last_editor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_modified"]) -> MetaOapg.properties.last_modified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["list_type"]) -> MetaOapg.properties.list_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country_list"]) -> MetaOapg.properties.country_list: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ip_list"]) -> MetaOapg.properties.ip_list: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "last_editor", "last_modified", "list_type", "name", "country_list", "ip_list", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_editor"]) -> typing.Union[MetaOapg.properties.last_editor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_modified"]) -> typing.Union[MetaOapg.properties.last_modified, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["list_type"]) -> typing.Union[MetaOapg.properties.list_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country_list"]) -> typing.Union[MetaOapg.properties.country_list, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ip_list"]) -> typing.Union[MetaOapg.properties.ip_list, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "last_editor", "last_modified", "list_type", "name", "country_list", "ip_list", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        last_editor: typing.Union[MetaOapg.properties.last_editor, str, schemas.Unset] = schemas.unset,
        last_modified: typing.Union[MetaOapg.properties.last_modified, str, schemas.Unset] = schemas.unset,
        list_type: typing.Union[MetaOapg.properties.list_type, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        country_list: typing.Union[MetaOapg.properties.country_list, list, tuple, schemas.Unset] = schemas.unset,
        ip_list: typing.Union[MetaOapg.properties.ip_list, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NetworkLists':
        return super().__new__(
            cls,
            *_args,
            id=id,
            last_editor=last_editor,
            last_modified=last_modified,
            list_type=list_type,
            name=name,
            country_list=country_list,
            ip_list=ip_list,
            _configuration=_configuration,
            **kwargs,
        )
