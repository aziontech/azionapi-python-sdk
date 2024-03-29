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


class ApplicationUpdateRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            name = schemas.StrSchema
            delivery_protocol = schemas.StrSchema
            http_port = schemas.AnyTypeSchema
            https_port = schemas.AnyTypeSchema
            minimum_tls_version = schemas.StrSchema
            active = schemas.BoolSchema
            debug_rules = schemas.BoolSchema
            application_acceleration = schemas.BoolSchema
            caching = schemas.BoolSchema
            device_detection = schemas.BoolSchema
            edge_firewall = schemas.BoolSchema
            edge_functions = schemas.BoolSchema
            image_optimization = schemas.BoolSchema
            l2_caching = schemas.BoolSchema
            load_balancer = schemas.BoolSchema
            raw_logs = schemas.BoolSchema
            web_application_firewall = schemas.BoolSchema
            websocket = schemas.BoolSchema
            __annotations__ = {
                "name": name,
                "delivery_protocol": delivery_protocol,
                "http_port": http_port,
                "https_port": https_port,
                "minimum_tls_version": minimum_tls_version,
                "active": active,
                "debug_rules": debug_rules,
                "application_acceleration": application_acceleration,
                "caching": caching,
                "device_detection": device_detection,
                "edge_firewall": edge_firewall,
                "edge_functions": edge_functions,
                "image_optimization": image_optimization,
                "l2_caching": l2_caching,
                "load_balancer": load_balancer,
                "raw_logs": raw_logs,
                "web_application_firewall": web_application_firewall,
                "websocket": websocket,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["delivery_protocol"]) -> MetaOapg.properties.delivery_protocol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["http_port"]) -> MetaOapg.properties.http_port: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["https_port"]) -> MetaOapg.properties.https_port: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minimum_tls_version"]) -> MetaOapg.properties.minimum_tls_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["debug_rules"]) -> MetaOapg.properties.debug_rules: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["application_acceleration"]) -> MetaOapg.properties.application_acceleration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["caching"]) -> MetaOapg.properties.caching: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_detection"]) -> MetaOapg.properties.device_detection: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["edge_firewall"]) -> MetaOapg.properties.edge_firewall: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["edge_functions"]) -> MetaOapg.properties.edge_functions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_optimization"]) -> MetaOapg.properties.image_optimization: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["l2_caching"]) -> MetaOapg.properties.l2_caching: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["load_balancer"]) -> MetaOapg.properties.load_balancer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["raw_logs"]) -> MetaOapg.properties.raw_logs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["web_application_firewall"]) -> MetaOapg.properties.web_application_firewall: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["websocket"]) -> MetaOapg.properties.websocket: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name"], typing_extensions.Literal["delivery_protocol"], typing_extensions.Literal["http_port"], typing_extensions.Literal["https_port"], typing_extensions.Literal["minimum_tls_version"], typing_extensions.Literal["active"], typing_extensions.Literal["debug_rules"], typing_extensions.Literal["application_acceleration"], typing_extensions.Literal["caching"], typing_extensions.Literal["device_detection"], typing_extensions.Literal["edge_firewall"], typing_extensions.Literal["edge_functions"], typing_extensions.Literal["image_optimization"], typing_extensions.Literal["l2_caching"], typing_extensions.Literal["load_balancer"], typing_extensions.Literal["raw_logs"], typing_extensions.Literal["web_application_firewall"], typing_extensions.Literal["websocket"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["delivery_protocol"]) -> typing.Union[MetaOapg.properties.delivery_protocol, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["http_port"]) -> typing.Union[MetaOapg.properties.http_port, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["https_port"]) -> typing.Union[MetaOapg.properties.https_port, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minimum_tls_version"]) -> typing.Union[MetaOapg.properties.minimum_tls_version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> typing.Union[MetaOapg.properties.active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["debug_rules"]) -> typing.Union[MetaOapg.properties.debug_rules, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["application_acceleration"]) -> typing.Union[MetaOapg.properties.application_acceleration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["caching"]) -> typing.Union[MetaOapg.properties.caching, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_detection"]) -> typing.Union[MetaOapg.properties.device_detection, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["edge_firewall"]) -> typing.Union[MetaOapg.properties.edge_firewall, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["edge_functions"]) -> typing.Union[MetaOapg.properties.edge_functions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_optimization"]) -> typing.Union[MetaOapg.properties.image_optimization, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["l2_caching"]) -> typing.Union[MetaOapg.properties.l2_caching, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["load_balancer"]) -> typing.Union[MetaOapg.properties.load_balancer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["raw_logs"]) -> typing.Union[MetaOapg.properties.raw_logs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["web_application_firewall"]) -> typing.Union[MetaOapg.properties.web_application_firewall, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["websocket"]) -> typing.Union[MetaOapg.properties.websocket, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name"], typing_extensions.Literal["delivery_protocol"], typing_extensions.Literal["http_port"], typing_extensions.Literal["https_port"], typing_extensions.Literal["minimum_tls_version"], typing_extensions.Literal["active"], typing_extensions.Literal["debug_rules"], typing_extensions.Literal["application_acceleration"], typing_extensions.Literal["caching"], typing_extensions.Literal["device_detection"], typing_extensions.Literal["edge_firewall"], typing_extensions.Literal["edge_functions"], typing_extensions.Literal["image_optimization"], typing_extensions.Literal["l2_caching"], typing_extensions.Literal["load_balancer"], typing_extensions.Literal["raw_logs"], typing_extensions.Literal["web_application_firewall"], typing_extensions.Literal["websocket"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        delivery_protocol: typing.Union[MetaOapg.properties.delivery_protocol, str, schemas.Unset] = schemas.unset,
        http_port: typing.Union[MetaOapg.properties.http_port, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        https_port: typing.Union[MetaOapg.properties.https_port, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        minimum_tls_version: typing.Union[MetaOapg.properties.minimum_tls_version, str, schemas.Unset] = schemas.unset,
        active: typing.Union[MetaOapg.properties.active, bool, schemas.Unset] = schemas.unset,
        debug_rules: typing.Union[MetaOapg.properties.debug_rules, bool, schemas.Unset] = schemas.unset,
        application_acceleration: typing.Union[MetaOapg.properties.application_acceleration, bool, schemas.Unset] = schemas.unset,
        caching: typing.Union[MetaOapg.properties.caching, bool, schemas.Unset] = schemas.unset,
        device_detection: typing.Union[MetaOapg.properties.device_detection, bool, schemas.Unset] = schemas.unset,
        edge_firewall: typing.Union[MetaOapg.properties.edge_firewall, bool, schemas.Unset] = schemas.unset,
        edge_functions: typing.Union[MetaOapg.properties.edge_functions, bool, schemas.Unset] = schemas.unset,
        image_optimization: typing.Union[MetaOapg.properties.image_optimization, bool, schemas.Unset] = schemas.unset,
        l2_caching: typing.Union[MetaOapg.properties.l2_caching, bool, schemas.Unset] = schemas.unset,
        load_balancer: typing.Union[MetaOapg.properties.load_balancer, bool, schemas.Unset] = schemas.unset,
        raw_logs: typing.Union[MetaOapg.properties.raw_logs, bool, schemas.Unset] = schemas.unset,
        web_application_firewall: typing.Union[MetaOapg.properties.web_application_firewall, bool, schemas.Unset] = schemas.unset,
        websocket: typing.Union[MetaOapg.properties.websocket, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ApplicationUpdateRequest':
        return super().__new__(
            cls,
            *_args,
            name=name,
            delivery_protocol=delivery_protocol,
            http_port=http_port,
            https_port=https_port,
            minimum_tls_version=minimum_tls_version,
            active=active,
            debug_rules=debug_rules,
            application_acceleration=application_acceleration,
            caching=caching,
            device_detection=device_detection,
            edge_firewall=edge_firewall,
            edge_functions=edge_functions,
            image_optimization=image_optimization,
            l2_caching=l2_caching,
            load_balancer=load_balancer,
            raw_logs=raw_logs,
            web_application_firewall=web_application_firewall,
            websocket=websocket,
            _configuration=_configuration,
        )
