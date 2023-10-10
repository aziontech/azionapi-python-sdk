# coding: utf-8

"""
    Edge Functions Instances API

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
from pydantic import BaseModel, StrictInt, conlist
from edgefunctionsinstance_edgefirewall.models.edge_functions_instance import EdgeFunctionsInstance
from edgefunctionsinstance_edgefirewall.models.links import Links

class ListEdgeFunctionsInstancesResponse(BaseModel):
    """
    ListEdgeFunctionsInstancesResponse
    """
    count: Optional[StrictInt] = None
    total_pages: Optional[StrictInt] = None
    schema_version: Optional[StrictInt] = None
    links: Optional[Links] = None
    results: Optional[conlist(EdgeFunctionsInstance)] = None
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
    def from_json(cls, json_str: str) -> ListEdgeFunctionsInstancesResponse:
        """Create an instance of ListEdgeFunctionsInstancesResponse from a JSON string"""
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
    def from_dict(cls, obj: dict) -> ListEdgeFunctionsInstancesResponse:
        """Create an instance of ListEdgeFunctionsInstancesResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListEdgeFunctionsInstancesResponse.parse_obj(obj)

        _obj = ListEdgeFunctionsInstancesResponse.parse_obj({
            "count": obj.get("count"),
            "total_pages": obj.get("total_pages"),
            "schema_version": obj.get("schema_version"),
            "links": Links.from_dict(obj.get("links")) if obj.get("links") is not None else None,
            "results": [EdgeFunctionsInstance.from_dict(_item) for _item in obj.get("results")] if obj.get("results") is not None else None
        })
        return _obj


