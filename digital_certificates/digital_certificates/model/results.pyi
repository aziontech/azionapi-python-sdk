# coding: utf-8

"""
    Digital Certificates API

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

from digital_certificates import schemas  # noqa: F401


class Results(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        
        class items(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    id = schemas.IntSchema
                    name = schemas.StrSchema
                    
                    
                    class subject_name(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            items = schemas.StrSchema
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'subject_name':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    
                    
                    class validity(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'validity':
                            return super().__new__(
                                cls,
                                *_args,
                                _configuration=_configuration,
                            )
                    status = schemas.StrSchema
                    
                    
                    class certificate_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def EDGE_CERTIFICATE(cls):
                            return cls("edge_certificate")
                        
                        @schemas.classproperty
                        def TRUSTED_CA_CERTIFICATE(cls):
                            return cls("trusted_ca_certificate")
                    managed = schemas.BoolSchema
                    
                    
                    class issuer(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'issuer':
                            return super().__new__(
                                cls,
                                *_args,
                                _configuration=_configuration,
                            )
                    azion_information = schemas.StrSchema
                    __annotations__ = {
                        "id": id,
                        "name": name,
                        "subject_name": subject_name,
                        "validity": validity,
                        "status": status,
                        "certificate_type": certificate_type,
                        "managed": managed,
                        "issuer": issuer,
                        "azion_information": azion_information,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["subject_name"]) -> MetaOapg.properties.subject_name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["validity"]) -> MetaOapg.properties.validity: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["certificate_type"]) -> MetaOapg.properties.certificate_type: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["managed"]) -> MetaOapg.properties.managed: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["issuer"]) -> MetaOapg.properties.issuer: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["azion_information"]) -> MetaOapg.properties.azion_information: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "subject_name", "validity", "status", "certificate_type", "managed", "issuer", "azion_information", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["subject_name"]) -> typing.Union[MetaOapg.properties.subject_name, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["validity"]) -> typing.Union[MetaOapg.properties.validity, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["certificate_type"]) -> typing.Union[MetaOapg.properties.certificate_type, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["managed"]) -> typing.Union[MetaOapg.properties.managed, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["issuer"]) -> typing.Union[MetaOapg.properties.issuer, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["azion_information"]) -> typing.Union[MetaOapg.properties.azion_information, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "subject_name", "validity", "status", "certificate_type", "managed", "issuer", "azion_information", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                subject_name: typing.Union[MetaOapg.properties.subject_name, list, tuple, schemas.Unset] = schemas.unset,
                validity: typing.Union[MetaOapg.properties.validity, None, str, schemas.Unset] = schemas.unset,
                status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
                certificate_type: typing.Union[MetaOapg.properties.certificate_type, str, schemas.Unset] = schemas.unset,
                managed: typing.Union[MetaOapg.properties.managed, bool, schemas.Unset] = schemas.unset,
                issuer: typing.Union[MetaOapg.properties.issuer, None, str, schemas.Unset] = schemas.unset,
                azion_information: typing.Union[MetaOapg.properties.azion_information, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'items':
                return super().__new__(
                    cls,
                    *_args,
                    id=id,
                    name=name,
                    subject_name=subject_name,
                    validity=validity,
                    status=status,
                    certificate_type=certificate_type,
                    managed=managed,
                    issuer=issuer,
                    azion_information=azion_information,
                    _configuration=_configuration,
                    **kwargs,
                )

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'Results':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
