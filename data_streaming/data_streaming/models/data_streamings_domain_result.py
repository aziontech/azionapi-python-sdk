# coding: utf-8

"""
    Data Streaming - OpenAPI

    The Data Streaming API allows you to manage your existing data streamings and templates. Data Streaming allows you to feed your stream processing, SIEM, and big data platforms with the event logs from your applications on Azion in real time. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr

class DataStreamingsDomainResult(BaseModel):
    """
    DataStreamingsDomainResult
    """
    domain_id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    selected: Optional[StrictBool] = None
    __properties = ["domain_id", "name", "selected"]

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
    def from_json(cls, json_str: str) -> DataStreamingsDomainResult:
        """Create an instance of DataStreamingsDomainResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if selected (nullable) is None
        # and __fields_set__ contains the field
        if self.selected is None and "selected" in self.__fields_set__:
            _dict['selected'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DataStreamingsDomainResult:
        """Create an instance of DataStreamingsDomainResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DataStreamingsDomainResult.parse_obj(obj)

        _obj = DataStreamingsDomainResult.parse_obj({
            "domain_id": obj.get("domain_id"),
            "name": obj.get("name"),
            "selected": obj.get("selected")
        })
        return _obj


