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
from pydantic import BaseModel, StrictStr, validator
from edgefirewall.models.set_custom_response_argument import SetCustomResponseArgument

class SetCustomResponse(BaseModel):
    """
    SetCustomResponse
    """
    name: Optional[StrictStr] = None
    argument: Optional[SetCustomResponseArgument] = None
    __properties = ["name", "argument"]

    @validator('name')
    def name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('set_custom_response'):
            raise ValueError("must be one of enum values ('set_custom_response')")
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
    def from_json(cls, json_str: str) -> SetCustomResponse:
        """Create an instance of SetCustomResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of argument
        if self.argument:
            _dict['argument'] = self.argument.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SetCustomResponse:
        """Create an instance of SetCustomResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SetCustomResponse.parse_obj(obj)

        _obj = SetCustomResponse.parse_obj({
            "name": obj.get("name"),
            "argument": SetCustomResponseArgument.from_dict(obj.get("argument")) if obj.get("argument") is not None else None
        })
        return _obj


