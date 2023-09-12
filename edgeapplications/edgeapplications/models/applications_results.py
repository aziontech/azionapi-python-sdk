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


from typing import List
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from edgeapplications.models.application_origins import ApplicationOrigins

class ApplicationsResults(BaseModel):
    """
    ApplicationsResults
    """
    id: StrictInt = Field(...)
    name: StrictStr = Field(...)
    debug_rules: StrictBool = Field(...)
    last_editor: StrictStr = Field(...)
    last_modified: StrictStr = Field(...)
    active: StrictBool = Field(...)
    origins: conlist(ApplicationOrigins) = Field(...)
    __properties = ["id", "name", "debug_rules", "last_editor", "last_modified", "active", "origins"]

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
    def from_json(cls, json_str: str) -> ApplicationsResults:
        """Create an instance of ApplicationsResults from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in origins (list)
        _items = []
        if self.origins:
            for _item in self.origins:
                if _item:
                    _items.append(_item.to_dict())
            _dict['origins'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApplicationsResults:
        """Create an instance of ApplicationsResults from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApplicationsResults.parse_obj(obj)

        _obj = ApplicationsResults.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "debug_rules": obj.get("debug_rules"),
            "last_editor": obj.get("last_editor"),
            "last_modified": obj.get("last_modified"),
            "active": obj.get("active"),
            "origins": [ApplicationOrigins.from_dict(_item) for _item in obj.get("origins")] if obj.get("origins") is not None else None
        })
        return _obj


