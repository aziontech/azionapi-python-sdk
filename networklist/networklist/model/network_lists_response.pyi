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


class NetworkListsResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def results() -> typing.Type['NetworkLists']:
                return NetworkLists
            schema_version = schemas.NumberSchema
            __annotations__ = {
                "results": results,
                "schema_version": schema_version,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["results"]) -> 'NetworkLists': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schema_version"]) -> MetaOapg.properties.schema_version: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["results", "schema_version", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["results"]) -> typing.Union['NetworkLists', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schema_version"]) -> typing.Union[MetaOapg.properties.schema_version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["results", "schema_version", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        results: typing.Union['NetworkLists', schemas.Unset] = schemas.unset,
        schema_version: typing.Union[MetaOapg.properties.schema_version, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NetworkListsResponse':
        return super().__new__(
            cls,
            *_args,
            results=results,
            schema_version=schema_version,
            _configuration=_configuration,
            **kwargs,
        )

from networklist.model.network_lists import NetworkLists
