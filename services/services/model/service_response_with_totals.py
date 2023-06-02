# coding: utf-8

"""
    Services API

    Azion Services  # noqa: E501

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

from services import schemas  # noqa: F401


class ServiceResponseWithTotals(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "total",
            "services",
        }
        
        class properties:
            
            
            class services(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ServiceResponse']:
                        return ServiceResponse
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ServiceResponse'], typing.List['ServiceResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'services':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ServiceResponse':
                    return super().__getitem__(i)
            total = schemas.Int64Schema
            __annotations__ = {
                "services": services,
                "total": total,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    total: MetaOapg.properties.total
    services: MetaOapg.properties.services
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["services"]) -> MetaOapg.properties.services: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["total"], typing_extensions.Literal["services"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["services"]) -> MetaOapg.properties.services: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["total"], typing_extensions.Literal["services"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, ],
        services: typing.Union[MetaOapg.properties.services, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ServiceResponseWithTotals':
        return super().__new__(
            cls,
            *_args,
            total=total,
            services=services,
            _configuration=_configuration,
        )

from services.model.service_response import ServiceResponse
