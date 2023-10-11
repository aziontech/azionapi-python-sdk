# coding: utf-8

"""
    Intelligent DNS API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictInt
from idns.models.zone import Zone

class GetZoneResponse(BaseModel):
    """
    Object returned by get zone  # noqa: E501
    """
    schema_version: Optional[StrictInt] = Field(None, description="The schema version")
    results: Optional[Zone] = None
    __properties = ["schema_version", "results"]

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
    def from_json(cls, json_str: str) -> GetZoneResponse:
        """Create an instance of GetZoneResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of results
        if self.results:
            _dict['results'] = self.results.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetZoneResponse:
        """Create an instance of GetZoneResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetZoneResponse.parse_obj(obj)

        _obj = GetZoneResponse.parse_obj({
            "schema_version": obj.get("schema_version"),
            "results": Zone.from_dict(obj.get("results")) if obj.get("results") is not None else None
        })
        return _obj

