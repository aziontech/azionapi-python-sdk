# coding: utf-8

"""
    Edgenode API

    Azion Orchestration  # noqa: E501

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

from edgenode import schemas  # noqa: F401


class AuthorizeEdgeNodesResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "authorized",
            "errors",
        }
        
        class properties:
            
            
            class authorized(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.Int64Schema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'authorized':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class errors(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['UnauthorizedEdgeNodeInfo']:
                        return UnauthorizedEdgeNodeInfo
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['UnauthorizedEdgeNodeInfo'], typing.List['UnauthorizedEdgeNodeInfo']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'errors':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'UnauthorizedEdgeNodeInfo':
                    return super().__getitem__(i)
            __annotations__ = {
                "authorized": authorized,
                "errors": errors,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    authorized: MetaOapg.properties.authorized
    errors: MetaOapg.properties.errors
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authorized"]) -> MetaOapg.properties.authorized: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> MetaOapg.properties.errors: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["authorized"], typing_extensions.Literal["errors"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authorized"]) -> MetaOapg.properties.authorized: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> MetaOapg.properties.errors: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["authorized"], typing_extensions.Literal["errors"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        authorized: typing.Union[MetaOapg.properties.authorized, list, tuple, ],
        errors: typing.Union[MetaOapg.properties.errors, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'AuthorizeEdgeNodesResponse':
        return super().__new__(
            cls,
            *_args,
            authorized=authorized,
            errors=errors,
            _configuration=_configuration,
        )

from edgenode.model.unauthorized_edge_node_info import UnauthorizedEdgeNodeInfo