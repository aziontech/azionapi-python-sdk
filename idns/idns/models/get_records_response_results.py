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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from idns.models.record_get import RecordGet

class GetRecordsResponseResults(BaseModel):
    """
    GetRecordsResponseResults
    """
    zone_id: Optional[StrictInt] = None
    zone_domain: Optional[StrictStr] = None
    records: Optional[conlist(RecordGet)] = Field(None, description="Zone records collection")
    __properties = ["zone_id", "zone_domain", "records"]

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
    def from_json(cls, json_str: str) -> GetRecordsResponseResults:
        """Create an instance of GetRecordsResponseResults from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in records (list)
        _items = []
        if self.records:
            for _item in self.records:
                if _item:
                    _items.append(_item.to_dict())
            _dict['records'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetRecordsResponseResults:
        """Create an instance of GetRecordsResponseResults from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetRecordsResponseResults.parse_obj(obj)

        _obj = GetRecordsResponseResults.parse_obj({
            "zone_id": obj.get("zone_id"),
            "zone_domain": obj.get("zone_domain"),
            "records": [RecordGet.from_dict(_item) for _item in obj.get("records")] if obj.get("records") is not None else None
        })
        return _obj


