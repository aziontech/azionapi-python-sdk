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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ApplicationResults(BaseModel):
    """
    ApplicationResults
    """ # noqa: E501
    id: StrictInt
    name: StrictStr
    active: StrictBool
    debug_rules: StrictBool
    http3: StrictBool
    supported_ciphers: StrictStr
    delivery_protocol: StrictStr
    http_port: Optional[Any]
    https_port: Optional[Any]
    minimum_tls_version: StrictStr
    application_acceleration: StrictBool
    caching: StrictBool
    device_detection: StrictBool
    edge_firewall: StrictBool
    edge_functions: StrictBool
    image_optimization: StrictBool
    l2_caching: StrictBool
    load_balancer: StrictBool
    raw_logs: StrictBool
    web_application_firewall: StrictBool
    __properties: ClassVar[List[str]] = ["id", "name", "active", "debug_rules", "http3", "supported_ciphers", "delivery_protocol", "http_port", "https_port", "minimum_tls_version", "application_acceleration", "caching", "device_detection", "edge_firewall", "edge_functions", "image_optimization", "l2_caching", "load_balancer", "raw_logs", "web_application_firewall"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ApplicationResults from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if http_port (nullable) is None
        # and model_fields_set contains the field
        if self.http_port is None and "http_port" in self.model_fields_set:
            _dict['http_port'] = None

        # set to None if https_port (nullable) is None
        # and model_fields_set contains the field
        if self.https_port is None and "https_port" in self.model_fields_set:
            _dict['https_port'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ApplicationResults from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "active": obj.get("active"),
            "debug_rules": obj.get("debug_rules"),
            "http3": obj.get("http3"),
            "supported_ciphers": obj.get("supported_ciphers"),
            "delivery_protocol": obj.get("delivery_protocol"),
            "http_port": obj.get("http_port"),
            "https_port": obj.get("https_port"),
            "minimum_tls_version": obj.get("minimum_tls_version"),
            "application_acceleration": obj.get("application_acceleration"),
            "caching": obj.get("caching"),
            "device_detection": obj.get("device_detection"),
            "edge_firewall": obj.get("edge_firewall"),
            "edge_functions": obj.get("edge_functions"),
            "image_optimization": obj.get("image_optimization"),
            "l2_caching": obj.get("l2_caching"),
            "load_balancer": obj.get("load_balancer"),
            "raw_logs": obj.get("raw_logs"),
            "web_application_firewall": obj.get("web_application_firewall")
        })
        return _obj


