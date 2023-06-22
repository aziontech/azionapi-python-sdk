# coding: utf-8

"""
    Edge Functions Instances API

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

from edgefunctionsinstance_edgefirewall import schemas  # noqa: F401


class ListEdgeFunctionsInstancesResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            count = schemas.Int64Schema
            total_pages = schemas.Int64Schema
            schema_version = schemas.Int64Schema
        
            @staticmethod
            def links() -> typing.Type['Links']:
                return Links
            
            
            class results(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EdgeFunctionsInstance']:
                        return EdgeFunctionsInstance
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['EdgeFunctionsInstance'], typing.List['EdgeFunctionsInstance']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'results':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'EdgeFunctionsInstance':
                    return super().__getitem__(i)
            __annotations__ = {
                "count": count,
                "total_pages": total_pages,
                "schema_version": schema_version,
                "links": links,
                "results": results,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_pages"]) -> MetaOapg.properties.total_pages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schema_version"]) -> MetaOapg.properties.schema_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> 'Links': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["results"]) -> MetaOapg.properties.results: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["count", "total_pages", "schema_version", "links", "results", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["count"]) -> typing.Union[MetaOapg.properties.count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_pages"]) -> typing.Union[MetaOapg.properties.total_pages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schema_version"]) -> typing.Union[MetaOapg.properties.schema_version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union['Links', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["results"]) -> typing.Union[MetaOapg.properties.results, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["count", "total_pages", "schema_version", "links", "results", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        count: typing.Union[MetaOapg.properties.count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        total_pages: typing.Union[MetaOapg.properties.total_pages, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        schema_version: typing.Union[MetaOapg.properties.schema_version, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        links: typing.Union['Links', schemas.Unset] = schemas.unset,
        results: typing.Union[MetaOapg.properties.results, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ListEdgeFunctionsInstancesResponse':
        return super().__new__(
            cls,
            *_args,
            count=count,
            total_pages=total_pages,
            schema_version=schema_version,
            links=links,
            results=results,
            _configuration=_configuration,
            **kwargs,
        )

from edgefunctionsinstance_edgefirewall.model.edge_functions_instance import EdgeFunctionsInstance
from edgefunctionsinstance_edgefirewall.model.links import Links
