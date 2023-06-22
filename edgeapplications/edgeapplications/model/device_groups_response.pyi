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


class DeviceGroupsResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "schema_version",
            "count",
            "links",
            "total_pages",
            "results",
        }
        
        class properties:
            count = schemas.Int64Schema
            total_pages = schemas.Int64Schema
            schema_version = schemas.Int64Schema
        
            @staticmethod
            def links() -> typing.Type['DeviceGroupsResponseLinks']:
                return DeviceGroupsResponseLinks
            
            
            class results(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DeviceGroupsResultResponse']:
                        return DeviceGroupsResultResponse
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['DeviceGroupsResultResponse'], typing.List['DeviceGroupsResultResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'results':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DeviceGroupsResultResponse':
                    return super().__getitem__(i)
            __annotations__ = {
                "count": count,
                "total_pages": total_pages,
                "schema_version": schema_version,
                "links": links,
                "results": results,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    schema_version: MetaOapg.properties.schema_version
    count: MetaOapg.properties.count
    links: 'DeviceGroupsResponseLinks'
    total_pages: MetaOapg.properties.total_pages
    results: MetaOapg.properties.results
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schema_version"]) -> MetaOapg.properties.schema_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> 'DeviceGroupsResponseLinks': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_pages"]) -> MetaOapg.properties.total_pages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["results"]) -> MetaOapg.properties.results: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["schema_version"], typing_extensions.Literal["count"], typing_extensions.Literal["links"], typing_extensions.Literal["total_pages"], typing_extensions.Literal["results"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schema_version"]) -> MetaOapg.properties.schema_version: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> 'DeviceGroupsResponseLinks': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_pages"]) -> MetaOapg.properties.total_pages: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["results"]) -> MetaOapg.properties.results: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["schema_version"], typing_extensions.Literal["count"], typing_extensions.Literal["links"], typing_extensions.Literal["total_pages"], typing_extensions.Literal["results"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        schema_version: typing.Union[MetaOapg.properties.schema_version, decimal.Decimal, int, ],
        count: typing.Union[MetaOapg.properties.count, decimal.Decimal, int, ],
        links: 'DeviceGroupsResponseLinks',
        total_pages: typing.Union[MetaOapg.properties.total_pages, decimal.Decimal, int, ],
        results: typing.Union[MetaOapg.properties.results, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'DeviceGroupsResponse':
        return super().__new__(
            cls,
            *_args,
            schema_version=schema_version,
            count=count,
            links=links,
            total_pages=total_pages,
            results=results,
            _configuration=_configuration,
        )

from edgeapplications.model.device_groups_response_links import DeviceGroupsResponseLinks
from edgeapplications.model.device_groups_result_response import DeviceGroupsResultResponse
