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


class CreateDeviceGroupsRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "addresses",
            "user_agent",
        }
        
        class properties:
            user_agent = schemas.StrSchema
            addresses = schemas.StrSchema
            name = schemas.StrSchema
            __annotations__ = {
                "user_agent": user_agent,
                "addresses": addresses,
                "name": name,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    addresses: MetaOapg.properties.addresses
    user_agent: MetaOapg.properties.user_agent
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addresses"]) -> MetaOapg.properties.addresses: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_agent"]) -> MetaOapg.properties.user_agent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["addresses"], typing_extensions.Literal["user_agent"], typing_extensions.Literal["name"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addresses"]) -> MetaOapg.properties.addresses: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_agent"]) -> MetaOapg.properties.user_agent: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["addresses"], typing_extensions.Literal["user_agent"], typing_extensions.Literal["name"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        addresses: typing.Union[MetaOapg.properties.addresses, str, ],
        user_agent: typing.Union[MetaOapg.properties.user_agent, str, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CreateDeviceGroupsRequest':
        return super().__new__(
            cls,
            *_args,
            addresses=addresses,
            user_agent=user_agent,
            name=name,
            _configuration=_configuration,
        )
