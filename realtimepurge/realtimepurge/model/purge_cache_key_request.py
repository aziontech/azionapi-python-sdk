# coding: utf-8

"""
    Purge API

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

from realtimepurge import schemas  # noqa: F401


class PurgeCacheKeyRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "urls",
            "method",
            "layer",
        }
        
        class properties:
            
            
            class urls(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'urls':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            method = schemas.StrSchema
            layer = schemas.StrSchema
            __annotations__ = {
                "urls": urls,
                "method": method,
                "layer": layer,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    urls: MetaOapg.properties.urls
    method: MetaOapg.properties.method
    layer: MetaOapg.properties.layer
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["urls"]) -> MetaOapg.properties.urls: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["method"]) -> MetaOapg.properties.method: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["layer"]) -> MetaOapg.properties.layer: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["urls"], typing_extensions.Literal["method"], typing_extensions.Literal["layer"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["urls"]) -> MetaOapg.properties.urls: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["method"]) -> MetaOapg.properties.method: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["layer"]) -> MetaOapg.properties.layer: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["urls"], typing_extensions.Literal["method"], typing_extensions.Literal["layer"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        urls: typing.Union[MetaOapg.properties.urls, list, tuple, ],
        method: typing.Union[MetaOapg.properties.method, str, ],
        layer: typing.Union[MetaOapg.properties.layer, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PurgeCacheKeyRequest':
        return super().__new__(
            cls,
            *_args,
            urls=urls,
            method=method,
            layer=layer,
            _configuration=_configuration,
        )
