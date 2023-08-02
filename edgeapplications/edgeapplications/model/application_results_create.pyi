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


class ApplicationResultsCreate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "load_balancer",
            "application_acceleration",
            "web_application_firewall",
            "device_detection",
            "raw_logs",
            "active",
            "delivery_protocol",
            "edge_firewall",
            "caching",
            "debug_rules",
            "http_port",
            "https_port",
            "minimum_tls_version",
            "supported_ciphers",
            "name",
            "edge_functions",
            "http3",
            "id",
            "image_optimization",
        }
        
        class properties:
            id = schemas.Int64Schema
            name = schemas.StrSchema
            active = schemas.BoolSchema
            debug_rules = schemas.BoolSchema
            http3 = schemas.BoolSchema
            supported_ciphers = schemas.StrSchema
            delivery_protocol = schemas.StrSchema
            http_port = schemas.AnyTypeSchema
            https_port = schemas.AnyTypeSchema
            minimum_tls_version = schemas.StrSchema
            application_acceleration = schemas.BoolSchema
            caching = schemas.BoolSchema
            device_detection = schemas.BoolSchema
            edge_firewall = schemas.BoolSchema
            edge_functions = schemas.BoolSchema
            image_optimization = schemas.BoolSchema
            load_balancer = schemas.BoolSchema
            raw_logs = schemas.BoolSchema
            web_application_firewall = schemas.BoolSchema
            l2_caching = schemas.BoolSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "active": active,
                "debug_rules": debug_rules,
                "http3": http3,
                "supported_ciphers": supported_ciphers,
                "delivery_protocol": delivery_protocol,
                "http_port": http_port,
                "https_port": https_port,
                "minimum_tls_version": minimum_tls_version,
                "application_acceleration": application_acceleration,
                "caching": caching,
                "device_detection": device_detection,
                "edge_firewall": edge_firewall,
                "edge_functions": edge_functions,
                "image_optimization": image_optimization,
                "load_balancer": load_balancer,
                "raw_logs": raw_logs,
                "web_application_firewall": web_application_firewall,
                "l2_caching": l2_caching,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    load_balancer: MetaOapg.properties.load_balancer
    application_acceleration: MetaOapg.properties.application_acceleration
    web_application_firewall: MetaOapg.properties.web_application_firewall
    device_detection: MetaOapg.properties.device_detection
    raw_logs: MetaOapg.properties.raw_logs
    active: MetaOapg.properties.active
    delivery_protocol: MetaOapg.properties.delivery_protocol
    edge_firewall: MetaOapg.properties.edge_firewall
    caching: MetaOapg.properties.caching
    debug_rules: MetaOapg.properties.debug_rules
    http_port: MetaOapg.properties.http_port
    https_port: MetaOapg.properties.https_port
    minimum_tls_version: MetaOapg.properties.minimum_tls_version
    supported_ciphers: MetaOapg.properties.supported_ciphers
    name: MetaOapg.properties.name
    edge_functions: MetaOapg.properties.edge_functions
    http3: MetaOapg.properties.http3
    id: MetaOapg.properties.id
    image_optimization: MetaOapg.properties.image_optimization
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["load_balancer"]) -> MetaOapg.properties.load_balancer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["application_acceleration"]) -> MetaOapg.properties.application_acceleration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["web_application_firewall"]) -> MetaOapg.properties.web_application_firewall: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_detection"]) -> MetaOapg.properties.device_detection: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["raw_logs"]) -> MetaOapg.properties.raw_logs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["delivery_protocol"]) -> MetaOapg.properties.delivery_protocol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["edge_firewall"]) -> MetaOapg.properties.edge_firewall: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caching"]) -> MetaOapg.properties.caching: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["debug_rules"]) -> MetaOapg.properties.debug_rules: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["http_port"]) -> MetaOapg.properties.http_port: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["https_port"]) -> MetaOapg.properties.https_port: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minimum_tls_version"]) -> MetaOapg.properties.minimum_tls_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supported_ciphers"]) -> MetaOapg.properties.supported_ciphers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["edge_functions"]) -> MetaOapg.properties.edge_functions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["http3"]) -> MetaOapg.properties.http3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_optimization"]) -> MetaOapg.properties.image_optimization: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["l2_caching"]) -> MetaOapg.properties.l2_caching: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["load_balancer"], typing_extensions.Literal["application_acceleration"], typing_extensions.Literal["web_application_firewall"], typing_extensions.Literal["device_detection"], typing_extensions.Literal["raw_logs"], typing_extensions.Literal["active"], typing_extensions.Literal["delivery_protocol"], typing_extensions.Literal["edge_firewall"], typing_extensions.Literal["caching"], typing_extensions.Literal["debug_rules"], typing_extensions.Literal["http_port"], typing_extensions.Literal["https_port"], typing_extensions.Literal["minimum_tls_version"], typing_extensions.Literal["supported_ciphers"], typing_extensions.Literal["name"], typing_extensions.Literal["edge_functions"], typing_extensions.Literal["http3"], typing_extensions.Literal["id"], typing_extensions.Literal["image_optimization"], typing_extensions.Literal["l2_caching"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["load_balancer"]) -> MetaOapg.properties.load_balancer: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["application_acceleration"]) -> MetaOapg.properties.application_acceleration: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["web_application_firewall"]) -> MetaOapg.properties.web_application_firewall: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_detection"]) -> MetaOapg.properties.device_detection: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["raw_logs"]) -> MetaOapg.properties.raw_logs: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["delivery_protocol"]) -> MetaOapg.properties.delivery_protocol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["edge_firewall"]) -> MetaOapg.properties.edge_firewall: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caching"]) -> MetaOapg.properties.caching: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["debug_rules"]) -> MetaOapg.properties.debug_rules: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["http_port"]) -> MetaOapg.properties.http_port: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["https_port"]) -> MetaOapg.properties.https_port: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minimum_tls_version"]) -> MetaOapg.properties.minimum_tls_version: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supported_ciphers"]) -> MetaOapg.properties.supported_ciphers: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["edge_functions"]) -> MetaOapg.properties.edge_functions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["http3"]) -> MetaOapg.properties.http3: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_optimization"]) -> MetaOapg.properties.image_optimization: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["l2_caching"]) -> typing.Union[MetaOapg.properties.l2_caching, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["load_balancer"], typing_extensions.Literal["application_acceleration"], typing_extensions.Literal["web_application_firewall"], typing_extensions.Literal["device_detection"], typing_extensions.Literal["raw_logs"], typing_extensions.Literal["active"], typing_extensions.Literal["delivery_protocol"], typing_extensions.Literal["edge_firewall"], typing_extensions.Literal["caching"], typing_extensions.Literal["debug_rules"], typing_extensions.Literal["http_port"], typing_extensions.Literal["https_port"], typing_extensions.Literal["minimum_tls_version"], typing_extensions.Literal["supported_ciphers"], typing_extensions.Literal["name"], typing_extensions.Literal["edge_functions"], typing_extensions.Literal["http3"], typing_extensions.Literal["id"], typing_extensions.Literal["image_optimization"], typing_extensions.Literal["l2_caching"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        load_balancer: typing.Union[MetaOapg.properties.load_balancer, bool, ],
        application_acceleration: typing.Union[MetaOapg.properties.application_acceleration, bool, ],
        web_application_firewall: typing.Union[MetaOapg.properties.web_application_firewall, bool, ],
        device_detection: typing.Union[MetaOapg.properties.device_detection, bool, ],
        raw_logs: typing.Union[MetaOapg.properties.raw_logs, bool, ],
        active: typing.Union[MetaOapg.properties.active, bool, ],
        delivery_protocol: typing.Union[MetaOapg.properties.delivery_protocol, str, ],
        edge_firewall: typing.Union[MetaOapg.properties.edge_firewall, bool, ],
        caching: typing.Union[MetaOapg.properties.caching, bool, ],
        debug_rules: typing.Union[MetaOapg.properties.debug_rules, bool, ],
        http_port: typing.Union[MetaOapg.properties.http_port, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        https_port: typing.Union[MetaOapg.properties.https_port, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        minimum_tls_version: typing.Union[MetaOapg.properties.minimum_tls_version, str, ],
        supported_ciphers: typing.Union[MetaOapg.properties.supported_ciphers, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        edge_functions: typing.Union[MetaOapg.properties.edge_functions, bool, ],
        http3: typing.Union[MetaOapg.properties.http3, bool, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        image_optimization: typing.Union[MetaOapg.properties.image_optimization, bool, ],
        l2_caching: typing.Union[MetaOapg.properties.l2_caching, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ApplicationResultsCreate':
        return super().__new__(
            cls,
            *_args,
            load_balancer=load_balancer,
            application_acceleration=application_acceleration,
            web_application_firewall=web_application_firewall,
            device_detection=device_detection,
            raw_logs=raw_logs,
            active=active,
            delivery_protocol=delivery_protocol,
            edge_firewall=edge_firewall,
            caching=caching,
            debug_rules=debug_rules,
            http_port=http_port,
            https_port=https_port,
            minimum_tls_version=minimum_tls_version,
            supported_ciphers=supported_ciphers,
            name=name,
            edge_functions=edge_functions,
            http3=http3,
            id=id,
            image_optimization=image_optimization,
            l2_caching=l2_caching,
            _configuration=_configuration,
        )
