# coding: utf-8

"""
    Edge Application API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Optional
from pydantic import BaseModel, StrictBool, StrictStr

class ApplicationUpdateRequest(BaseModel):
    """
    ApplicationUpdateRequest
    """
    name: Optional[StrictStr] = None
    delivery_protocol: Optional[StrictStr] = None
    http_port: Optional[Any] = None
    https_port: Optional[Any] = None
    minimum_tls_version: Optional[StrictStr] = None
    active: Optional[StrictBool] = None
    debug_rules: Optional[StrictBool] = None
    application_acceleration: Optional[StrictBool] = None
    caching: Optional[StrictBool] = None
    device_detection: Optional[StrictBool] = None
    edge_firewall: Optional[StrictBool] = None
    edge_functions: Optional[StrictBool] = None
    image_optimization: Optional[StrictBool] = None
    l2_caching: Optional[StrictBool] = None
    load_balancer: Optional[StrictBool] = None
    raw_logs: Optional[StrictBool] = None
    web_application_firewall: Optional[StrictBool] = None
    websocket: Optional[StrictBool] = None
    __properties = ["name", "delivery_protocol", "http_port", "https_port", "minimum_tls_version", "active", "debug_rules", "application_acceleration", "caching", "device_detection", "edge_firewall", "edge_functions", "image_optimization", "l2_caching", "load_balancer", "raw_logs", "web_application_firewall", "websocket"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApplicationUpdateRequest:
        """Create an instance of ApplicationUpdateRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if http_port (nullable) is None
        # and __fields_set__ contains the field
        if self.http_port is None and "http_port" in self.__fields_set__:
            _dict['http_port'] = None

        # set to None if https_port (nullable) is None
        # and __fields_set__ contains the field
        if self.https_port is None and "https_port" in self.__fields_set__:
            _dict['https_port'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApplicationUpdateRequest:
        """Create an instance of ApplicationUpdateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApplicationUpdateRequest.parse_obj(obj)

        _obj = ApplicationUpdateRequest.parse_obj({
            "name": obj.get("name"),
            "delivery_protocol": obj.get("delivery_protocol"),
            "http_port": obj.get("http_port"),
            "https_port": obj.get("https_port"),
            "minimum_tls_version": obj.get("minimum_tls_version"),
            "active": obj.get("active"),
            "debug_rules": obj.get("debug_rules"),
            "application_acceleration": obj.get("application_acceleration"),
            "caching": obj.get("caching"),
            "device_detection": obj.get("device_detection"),
            "edge_firewall": obj.get("edge_firewall"),
            "edge_functions": obj.get("edge_functions"),
            "image_optimization": obj.get("image_optimization"),
            "l2_caching": obj.get("l2_caching"),
            "load_balancer": obj.get("load_balancer"),
            "raw_logs": obj.get("raw_logs"),
            "web_application_firewall": obj.get("web_application_firewall"),
            "websocket": obj.get("websocket")
        })
        return _obj


