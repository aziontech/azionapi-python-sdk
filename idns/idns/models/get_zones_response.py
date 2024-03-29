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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, conlist
from idns.models.get_zones_response_links import GetZonesResponseLinks
from idns.models.zone import Zone

class GetZonesResponse(BaseModel):
    """
    Object returned by get zones  # noqa: E501
    """
    schema_version: Optional[StrictInt] = Field(None, description="The schema version")
    count: Optional[StrictInt] = Field(None, description="Number of records")
    total_pages: Optional[StrictInt] = Field(None, description="The total pages")
    links: Optional[GetZonesResponseLinks] = None
    results: Optional[conlist(Zone)] = Field(None, description="Hosted zones collection")
    __properties = ["schema_version", "count", "total_pages", "links", "results"]

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
    def from_json(cls, json_str: str) -> GetZonesResponse:
        """Create an instance of GetZonesResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item in self.results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['results'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetZonesResponse:
        """Create an instance of GetZonesResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetZonesResponse.parse_obj(obj)

        _obj = GetZonesResponse.parse_obj({
            "schema_version": obj.get("schema_version"),
            "count": obj.get("count"),
            "total_pages": obj.get("total_pages"),
            "links": GetZonesResponseLinks.from_dict(obj.get("links")) if obj.get("links") is not None else None,
            "results": [Zone.from_dict(_item) for _item in obj.get("results")] if obj.get("results") is not None else None
        })
        return _obj


