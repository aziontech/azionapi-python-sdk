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
from idns.models.get_records_response_results import GetRecordsResponseResults
from idns.models.get_zones_response_links import GetZonesResponseLinks

class GetRecordsResponse(BaseModel):
    """
    Object returned by get zone record  # noqa: E501
    """
    schema_version: Optional[StrictInt] = Field(None, description="The schema version")
    count: Optional[StrictInt] = Field(None, description="Number of records")
    total_pages: Optional[StrictInt] = Field(None, description="The total pages")
    links: Optional[GetZonesResponseLinks] = None
    results: Optional[GetRecordsResponseResults] = None
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
    def from_json(cls, json_str: str) -> GetRecordsResponse:
        """Create an instance of GetRecordsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of results
        if self.results:
            _dict['results'] = self.results.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetRecordsResponse:
        """Create an instance of GetRecordsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetRecordsResponse.parse_obj(obj)

        _obj = GetRecordsResponse.parse_obj({
            "schema_version": obj.get("schema_version"),
            "count": obj.get("count"),
            "total_pages": obj.get("total_pages"),
            "links": GetZonesResponseLinks.from_dict(obj.get("links")) if obj.get("links") is not None else None,
            "results": GetRecordsResponseResults.from_dict(obj.get("results")) if obj.get("results") is not None else None
        })
        return _obj

