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


class NetworkListUuidResponseEntryInt(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            last_editor = schemas.StrSchema
            last_modified = schemas.StrSchema
            list_type = schemas.StrSchema
            name = schemas.StrSchema
            
            
            class items_values(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.IntSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'items_values':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "last_editor": last_editor,
                "last_modified": last_modified,
                "list_type": list_type,
                "name": name,
                "items_values": items_values,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_editor"]) -> MetaOapg.properties.last_editor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_modified"]) -> MetaOapg.properties.last_modified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["list_type"]) -> MetaOapg.properties.list_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["items_values"]) -> MetaOapg.properties.items_values: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["last_editor", "last_modified", "list_type", "name", "items_values", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_editor"]) -> typing.Union[MetaOapg.properties.last_editor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_modified"]) -> typing.Union[MetaOapg.properties.last_modified, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["list_type"]) -> typing.Union[MetaOapg.properties.list_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["items_values"]) -> typing.Union[MetaOapg.properties.items_values, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["last_editor", "last_modified", "list_type", "name", "items_values", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        last_editor: typing.Union[MetaOapg.properties.last_editor, str, schemas.Unset] = schemas.unset,
        last_modified: typing.Union[MetaOapg.properties.last_modified, str, schemas.Unset] = schemas.unset,
        list_type: typing.Union[MetaOapg.properties.list_type, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        items_values: typing.Union[MetaOapg.properties.items_values, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NetworkListUuidResponseEntryInt':
        return super().__new__(
            cls,
            *_args,
            last_editor=last_editor,
            last_modified=last_modified,
            list_type=list_type,
            name=name,
            items_values=items_values,
            _configuration=_configuration,
            **kwargs,
        )
