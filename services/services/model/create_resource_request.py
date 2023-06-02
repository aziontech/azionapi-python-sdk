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


class CreateResourceRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "content_type",
            "name",
            "trigger",
            "content",
        }
        
        class properties:
            content = schemas.StrSchema
            content_type = schemas.StrSchema
            name = schemas.StrSchema
            trigger = schemas.StrSchema
            __annotations__ = {
                "content": content,
                "content_type": content_type,
                "name": name,
                "trigger": trigger,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    content_type: MetaOapg.properties.content_type
    name: MetaOapg.properties.name
    trigger: MetaOapg.properties.trigger
    content: MetaOapg.properties.content
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["content_type"]) -> MetaOapg.properties.content_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trigger"]) -> MetaOapg.properties.trigger: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["content"]) -> MetaOapg.properties.content: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["content_type"], typing_extensions.Literal["name"], typing_extensions.Literal["trigger"], typing_extensions.Literal["content"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["content_type"]) -> MetaOapg.properties.content_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trigger"]) -> MetaOapg.properties.trigger: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["content"]) -> MetaOapg.properties.content: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["content_type"], typing_extensions.Literal["name"], typing_extensions.Literal["trigger"], typing_extensions.Literal["content"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        content_type: typing.Union[MetaOapg.properties.content_type, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        trigger: typing.Union[MetaOapg.properties.trigger, str, ],
        content: typing.Union[MetaOapg.properties.content, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CreateResourceRequest':
        return super().__new__(
            cls,
            *_args,
            content_type=content_type,
            name=name,
            trigger=trigger,
            content=content,
            _configuration=_configuration,
        )
