# coding: utf-8

"""
    Intelligent DNS API

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

from idns import schemas  # noqa: F401


class Zone(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.IntSchema
            name = schemas.StrSchema
            domain = schemas.StrSchema
            is_active = schemas.BoolSchema
            
            
            class retry(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'retry':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class nx_ttl(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'nx_ttl':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class soa_ttl(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'soa_ttl':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class refresh(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'refresh':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class expiry(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'expiry':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class nameservers(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'nameservers':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "id": id,
                "name": name,
                "domain": domain,
                "is_active": is_active,
                "retry": retry,
                "nx_ttl": nx_ttl,
                "soa_ttl": soa_ttl,
                "refresh": refresh,
                "expiry": expiry,
                "nameservers": nameservers,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["domain"]) -> MetaOapg.properties.domain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_active"]) -> MetaOapg.properties.is_active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["retry"]) -> MetaOapg.properties.retry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nx_ttl"]) -> MetaOapg.properties.nx_ttl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["soa_ttl"]) -> MetaOapg.properties.soa_ttl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refresh"]) -> MetaOapg.properties.refresh: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiry"]) -> MetaOapg.properties.expiry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nameservers"]) -> MetaOapg.properties.nameservers: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "domain", "is_active", "retry", "nx_ttl", "soa_ttl", "refresh", "expiry", "nameservers", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["domain"]) -> typing.Union[MetaOapg.properties.domain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_active"]) -> typing.Union[MetaOapg.properties.is_active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["retry"]) -> typing.Union[MetaOapg.properties.retry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nx_ttl"]) -> typing.Union[MetaOapg.properties.nx_ttl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["soa_ttl"]) -> typing.Union[MetaOapg.properties.soa_ttl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refresh"]) -> typing.Union[MetaOapg.properties.refresh, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiry"]) -> typing.Union[MetaOapg.properties.expiry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nameservers"]) -> typing.Union[MetaOapg.properties.nameservers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "domain", "is_active", "retry", "nx_ttl", "soa_ttl", "refresh", "expiry", "nameservers", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        domain: typing.Union[MetaOapg.properties.domain, str, schemas.Unset] = schemas.unset,
        is_active: typing.Union[MetaOapg.properties.is_active, bool, schemas.Unset] = schemas.unset,
        retry: typing.Union[MetaOapg.properties.retry, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        nx_ttl: typing.Union[MetaOapg.properties.nx_ttl, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        soa_ttl: typing.Union[MetaOapg.properties.soa_ttl, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        refresh: typing.Union[MetaOapg.properties.refresh, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        expiry: typing.Union[MetaOapg.properties.expiry, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        nameservers: typing.Union[MetaOapg.properties.nameservers, list, tuple, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Zone':
        return super().__new__(
            cls,
            *_args,
            id=id,
            name=name,
            domain=domain,
            is_active=is_active,
            retry=retry,
            nx_ttl=nx_ttl,
            soa_ttl=soa_ttl,
            refresh=refresh,
            expiry=expiry,
            nameservers=nameservers,
            _configuration=_configuration,
            **kwargs,
        )
