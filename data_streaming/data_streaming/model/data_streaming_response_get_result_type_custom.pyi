# coding: utf-8

"""
    Data Streaming - OpenAPI

    The Data Streaming API allows you to manage your existing data streamings and templates. Data Streaming allows you to feed your stream processing, SIEM, and big data platforms with the event logs from your applications on Azion in real time.   # noqa: E501

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

from data_streaming import schemas  # noqa: F401


class DataStreamingResponseGetResultTypeCustom(
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
            data_source = schemas.StrSchema
            active = schemas.BoolSchema
        
            @staticmethod
            def endpoint() -> typing.Type['DataStreamingEndpointTypeKafka']:
                return DataStreamingEndpointTypeKafka
            all_domains = schemas.BoolSchema
            template_model = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "data_source": data_source,
                "active": active,
                "endpoint": endpoint,
                "all_domains": all_domains,
                "template_model": template_model,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data_source"]) -> MetaOapg.properties.data_source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endpoint"]) -> 'DataStreamingEndpointTypeKafka': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["all_domains"]) -> MetaOapg.properties.all_domains: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["template_model"]) -> MetaOapg.properties.template_model: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "data_source", "active", "endpoint", "all_domains", "template_model", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data_source"]) -> typing.Union[MetaOapg.properties.data_source, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> typing.Union[MetaOapg.properties.active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endpoint"]) -> typing.Union['DataStreamingEndpointTypeKafka', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["all_domains"]) -> typing.Union[MetaOapg.properties.all_domains, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["template_model"]) -> typing.Union[MetaOapg.properties.template_model, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "data_source", "active", "endpoint", "all_domains", "template_model", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        data_source: typing.Union[MetaOapg.properties.data_source, str, schemas.Unset] = schemas.unset,
        active: typing.Union[MetaOapg.properties.active, bool, schemas.Unset] = schemas.unset,
        endpoint: typing.Union['DataStreamingEndpointTypeKafka', schemas.Unset] = schemas.unset,
        all_domains: typing.Union[MetaOapg.properties.all_domains, bool, schemas.Unset] = schemas.unset,
        template_model: typing.Union[MetaOapg.properties.template_model, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DataStreamingResponseGetResultTypeCustom':
        return super().__new__(
            cls,
            *_args,
            id=id,
            name=name,
            data_source=data_source,
            active=active,
            endpoint=endpoint,
            all_domains=all_domains,
            template_model=template_model,
            _configuration=_configuration,
            **kwargs,
        )

from data_streaming.model.data_streaming_endpoint_type_kafka import DataStreamingEndpointTypeKafka
