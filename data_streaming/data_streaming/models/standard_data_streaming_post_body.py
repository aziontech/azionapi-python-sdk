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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist, validator
from data_streaming.models.data_streaming_endpoint_type_standard import DataStreamingEndpointTypeStandard

class StandardDataStreamingPostBody(BaseModel):
    """
    StandardDataStreamingPostBody
    """
    name: Optional[StrictStr] = None
    template_id: Optional[StrictInt] = Field(None, description="Options:  * `2` - Edge Applications Event Collector  * `4` - WAF Event Collector  * `86` - Edge Functions Event Collector  * `184` - Edge Applications + WAF Event Collector  * `251` - Activity History Collector ")
    data_source: Optional[StrictStr] = Field(None, description="Options:  * `http` - Edge Applications (default)  * `waf` - WAF Events  * `cells_console` - Edge Functions  * `rtm_activity` - Activity History ")
    active: Optional[StrictBool] = True
    endpoint: Optional[DataStreamingEndpointTypeStandard] = None
    domains_ids: Optional[conlist(StrictInt, min_items=1)] = Field(None, description="Note:  * Field not used with the rtm_activity data source. ")
    all_domains: Optional[StrictBool] = Field(False, description="Note:  * Field not used with the rtm_activity data source. ")
    __properties = ["name", "template_id", "data_source", "active", "endpoint", "domains_ids", "all_domains"]

    @validator('template_id')
    def template_id_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (2, 4, 86, 184, 251):
            raise ValueError("must be one of enum values (2, 4, 86, 184, 251)")
        return value

    @validator('data_source')
    def data_source_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('http', 'waf', 'cells_console', 'rtm_activity'):
            raise ValueError("must be one of enum values ('http', 'waf', 'cells_console', 'rtm_activity')")
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
    def from_json(cls, json_str: str) -> StandardDataStreamingPostBody:
        """Create an instance of StandardDataStreamingPostBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of endpoint
        if self.endpoint:
            _dict['endpoint'] = self.endpoint.to_dict()
        # set to None if data_source (nullable) is None
        # and __fields_set__ contains the field
        if self.data_source is None and "data_source" in self.__fields_set__:
            _dict['data_source'] = None

        # set to None if active (nullable) is None
        # and __fields_set__ contains the field
        if self.active is None and "active" in self.__fields_set__:
            _dict['active'] = None

        # set to None if all_domains (nullable) is None
        # and __fields_set__ contains the field
        if self.all_domains is None and "all_domains" in self.__fields_set__:
            _dict['all_domains'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StandardDataStreamingPostBody:
        """Create an instance of StandardDataStreamingPostBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StandardDataStreamingPostBody.parse_obj(obj)

        _obj = StandardDataStreamingPostBody.parse_obj({
            "name": obj.get("name"),
            "template_id": obj.get("template_id"),
            "data_source": obj.get("data_source"),
            "active": obj.get("active") if obj.get("active") is not None else True,
            "endpoint": DataStreamingEndpointTypeStandard.from_dict(obj.get("endpoint")) if obj.get("endpoint") is not None else None,
            "domains_ids": obj.get("domains_ids"),
            "all_domains": obj.get("all_domains") if obj.get("all_domains") is not None else False
        })
        return _obj

