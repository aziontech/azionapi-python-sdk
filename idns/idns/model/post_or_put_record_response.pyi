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


class PostOrPutRecordResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Object returned by create or update zone record
    """


    class MetaOapg:
        
        class properties:
            schema_version = schemas.IntSchema
        
            @staticmethod
            def results() -> typing.Type['RecordPostOrPut']:
                return RecordPostOrPut
            __annotations__ = {
                "schema_version": schema_version,
                "results": results,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schema_version"]) -> MetaOapg.properties.schema_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["results"]) -> 'RecordPostOrPut': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["schema_version", "results", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schema_version"]) -> typing.Union[MetaOapg.properties.schema_version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["results"]) -> typing.Union['RecordPostOrPut', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["schema_version", "results", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        schema_version: typing.Union[MetaOapg.properties.schema_version, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        results: typing.Union['RecordPostOrPut', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PostOrPutRecordResponse':
        return super().__new__(
            cls,
            *_args,
            schema_version=schema_version,
            results=results,
            _configuration=_configuration,
            **kwargs,
        )

from idns.model.record_post_or_put import RecordPostOrPut
