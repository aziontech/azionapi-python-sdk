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
from pydantic import BaseModel, Field, StrictStr

class DataStreamingEndpointTypeStandardHeadersExample(BaseModel):
    """
    DataStreamingEndpointTypeStandardHeadersExample
    """
    header_name_1: Optional[StrictStr] = Field(None, alias="header-name-1")
    header_name_2: Optional[StrictStr] = Field(None, alias="header-name-2")
    header_name_3: Optional[StrictStr] = Field(None, alias="header-name-3")
    __properties = ["header-name-1", "header-name-2", "header-name-3"]

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
    def from_json(cls, json_str: str) -> DataStreamingEndpointTypeStandardHeadersExample:
        """Create an instance of DataStreamingEndpointTypeStandardHeadersExample from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if header_name_1 (nullable) is None
        # and __fields_set__ contains the field
        if self.header_name_1 is None and "header_name_1" in self.__fields_set__:
            _dict['header-name-1'] = None

        # set to None if header_name_2 (nullable) is None
        # and __fields_set__ contains the field
        if self.header_name_2 is None and "header_name_2" in self.__fields_set__:
            _dict['header-name-2'] = None

        # set to None if header_name_3 (nullable) is None
        # and __fields_set__ contains the field
        if self.header_name_3 is None and "header_name_3" in self.__fields_set__:
            _dict['header-name-3'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DataStreamingEndpointTypeStandardHeadersExample:
        """Create an instance of DataStreamingEndpointTypeStandardHeadersExample from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DataStreamingEndpointTypeStandardHeadersExample.parse_obj(obj)

        _obj = DataStreamingEndpointTypeStandardHeadersExample.parse_obj({
            "header_name_1": obj.get("header-name-1"),
            "header_name_2": obj.get("header-name-2"),
            "header_name_3": obj.get("header-name-3")
        })
        return _obj

