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


class EndpointAzureMonitor(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            endpoint_type = schemas.StrSchema
            log_type = schemas.StrSchema
            shared_key = schemas.StrSchema
            time_generated_field = schemas.StrSchema
            
            
            class workspace_id(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{6}',  # noqa: E501
                    }]
            __annotations__ = {
                "endpoint_type": endpoint_type,
                "log_type": log_type,
                "shared_key": shared_key,
                "time_generated_field": time_generated_field,
                "workspace_id": workspace_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endpoint_type"]) -> MetaOapg.properties.endpoint_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["log_type"]) -> MetaOapg.properties.log_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shared_key"]) -> MetaOapg.properties.shared_key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time_generated_field"]) -> MetaOapg.properties.time_generated_field: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workspace_id"]) -> MetaOapg.properties.workspace_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["endpoint_type", "log_type", "shared_key", "time_generated_field", "workspace_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endpoint_type"]) -> typing.Union[MetaOapg.properties.endpoint_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["log_type"]) -> typing.Union[MetaOapg.properties.log_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shared_key"]) -> typing.Union[MetaOapg.properties.shared_key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time_generated_field"]) -> typing.Union[MetaOapg.properties.time_generated_field, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workspace_id"]) -> typing.Union[MetaOapg.properties.workspace_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["endpoint_type", "log_type", "shared_key", "time_generated_field", "workspace_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        endpoint_type: typing.Union[MetaOapg.properties.endpoint_type, str, schemas.Unset] = schemas.unset,
        log_type: typing.Union[MetaOapg.properties.log_type, str, schemas.Unset] = schemas.unset,
        shared_key: typing.Union[MetaOapg.properties.shared_key, str, schemas.Unset] = schemas.unset,
        time_generated_field: typing.Union[MetaOapg.properties.time_generated_field, str, schemas.Unset] = schemas.unset,
        workspace_id: typing.Union[MetaOapg.properties.workspace_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EndpointAzureMonitor':
        return super().__new__(
            cls,
            *_args,
            endpoint_type=endpoint_type,
            log_type=log_type,
            shared_key=shared_key,
            time_generated_field=time_generated_field,
            workspace_id=workspace_id,
            _configuration=_configuration,
            **kwargs,
        )
