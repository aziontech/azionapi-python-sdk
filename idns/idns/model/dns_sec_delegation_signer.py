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


class DnsSecDelegationSigner(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def digest_type() -> typing.Type['DnsSecDelegationSignerDigestType']:
                return DnsSecDelegationSignerDigestType
        
            @staticmethod
            def algorithm_type() -> typing.Type['DnsSecDelegationSignerDigestType']:
                return DnsSecDelegationSignerDigestType
            digest = schemas.StrSchema
            
            
            class key_tag(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 65535
                    inclusive_minimum = 1
            __annotations__ = {
                "digest_type": digest_type,
                "algorithm_type": algorithm_type,
                "digest": digest,
                "key_tag": key_tag,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["digest_type"]) -> 'DnsSecDelegationSignerDigestType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["algorithm_type"]) -> 'DnsSecDelegationSignerDigestType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["digest"]) -> MetaOapg.properties.digest: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key_tag"]) -> MetaOapg.properties.key_tag: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["digest_type", "algorithm_type", "digest", "key_tag", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["digest_type"]) -> typing.Union['DnsSecDelegationSignerDigestType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["algorithm_type"]) -> typing.Union['DnsSecDelegationSignerDigestType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["digest"]) -> typing.Union[MetaOapg.properties.digest, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key_tag"]) -> typing.Union[MetaOapg.properties.key_tag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["digest_type", "algorithm_type", "digest", "key_tag", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        digest_type: typing.Union['DnsSecDelegationSignerDigestType', schemas.Unset] = schemas.unset,
        algorithm_type: typing.Union['DnsSecDelegationSignerDigestType', schemas.Unset] = schemas.unset,
        digest: typing.Union[MetaOapg.properties.digest, str, schemas.Unset] = schemas.unset,
        key_tag: typing.Union[MetaOapg.properties.key_tag, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DnsSecDelegationSigner':
        return super().__new__(
            cls,
            *_args,
            digest_type=digest_type,
            algorithm_type=algorithm_type,
            digest=digest,
            key_tag=key_tag,
            _configuration=_configuration,
            **kwargs,
        )

from idns.model.dns_sec_delegation_signer_digest_type import DnsSecDelegationSignerDigestType
