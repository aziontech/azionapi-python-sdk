# coding: utf-8

"""
    Edge Firewall API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, conlist

class UpdateEdgeFirewallRequest(BaseModel):
    """
    UpdateEdgeFirewallRequest
    """
    name: Optional[StrictStr] = None
    domains: Optional[conlist(StrictInt)] = None
    is_active: Optional[StrictBool] = None
    edge_functions_enabled: Optional[StrictBool] = None
    network_protection_enabled: Optional[StrictBool] = None
    waf_enabled: Optional[StrictBool] = None
    __properties = ["name", "domains", "is_active", "edge_functions_enabled", "network_protection_enabled", "waf_enabled"]

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
    def from_json(cls, json_str: str) -> UpdateEdgeFirewallRequest:
        """Create an instance of UpdateEdgeFirewallRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateEdgeFirewallRequest:
        """Create an instance of UpdateEdgeFirewallRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdateEdgeFirewallRequest.parse_obj(obj)

        _obj = UpdateEdgeFirewallRequest.parse_obj({
            "name": obj.get("name"),
            "domains": obj.get("domains"),
            "is_active": obj.get("is_active"),
            "edge_functions_enabled": obj.get("edge_functions_enabled"),
            "network_protection_enabled": obj.get("network_protection_enabled"),
            "waf_enabled": obj.get("waf_enabled")
        })
        return _obj

