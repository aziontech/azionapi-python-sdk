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
from pydantic import BaseModel, Field, StrictInt, conlist
from edgeapplications.models.application_instances_results import ApplicationInstancesResults
from edgeapplications.models.application_links import ApplicationLinks

class ApplicationInstancesGetResponse(BaseModel):
    """
    ApplicationInstancesGetResponse
    """
    count: StrictInt = Field(...)
    total_pages: StrictInt = Field(...)
    schema_version: StrictInt = Field(...)
    links: ApplicationLinks = Field(...)
    results: conlist(ApplicationInstancesResults) = Field(...)
    __properties = ["count", "total_pages", "schema_version", "links", "results"]

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
    def from_json(cls, json_str: str) -> ApplicationInstancesGetResponse:
        """Create an instance of ApplicationInstancesGetResponse from a JSON string"""
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
    def from_dict(cls, obj: dict) -> ApplicationInstancesGetResponse:
        """Create an instance of ApplicationInstancesGetResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApplicationInstancesGetResponse.parse_obj(obj)

        _obj = ApplicationInstancesGetResponse.parse_obj({
            "count": obj.get("count"),
            "total_pages": obj.get("total_pages"),
            "schema_version": obj.get("schema_version"),
            "links": ApplicationLinks.from_dict(obj.get("links")) if obj.get("links") is not None else None,
            "results": [ApplicationInstancesResults.from_dict(_item) for _item in obj.get("results")] if obj.get("results") is not None else None
        })
        return _obj


