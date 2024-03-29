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


from typing import Optional
from pydantic import BaseModel, StrictStr, conint, validator

class SetRateLimitDetails(BaseModel):
    """
    SetRateLimitDetails
    """
    type: Optional[StrictStr] = None
    limit_by: Optional[StrictStr] = None
    average_rate_limit: Optional[conint(strict=True, ge=1)] = None
    maximum_burst_size: Optional[conint(strict=True, ge=1)] = None
    __properties = ["type", "limit_by", "average_rate_limit", "maximum_burst_size"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('second', 'minute'):
            raise ValueError("must be one of enum values ('second', 'minute')")
        return value

    @validator('limit_by')
    def limit_by_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('client_ip', 'global'):
            raise ValueError("must be one of enum values ('client_ip', 'global')")
        return value

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
    def from_json(cls, json_str: str) -> SetRateLimitDetails:
        """Create an instance of SetRateLimitDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SetRateLimitDetails:
        """Create an instance of SetRateLimitDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SetRateLimitDetails.parse_obj(obj)

        _obj = SetRateLimitDetails.parse_obj({
            "type": obj.get("type"),
            "limit_by": obj.get("limit_by"),
            "average_rate_limit": obj.get("average_rate_limit"),
            "maximum_burst_size": obj.get("maximum_burst_size")
        })
        return _obj


