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
from pydantic import BaseModel, StrictBool, StrictStr

class DataStreamingEndpointTypeKafka(BaseModel):
    """
    DataStreamingEndpointTypeKafka
    """
    endpoint_type: Optional[StrictStr] = None
    use_tls: Optional[StrictBool] = None
    kafka_topic: Optional[StrictStr] = None
    bootstrap_servers: Optional[StrictStr] = None
    __properties = ["endpoint_type", "use_tls", "kafka_topic", "bootstrap_servers"]

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
    def from_json(cls, json_str: str) -> DataStreamingEndpointTypeKafka:
        """Create an instance of DataStreamingEndpointTypeKafka from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DataStreamingEndpointTypeKafka:
        """Create an instance of DataStreamingEndpointTypeKafka from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DataStreamingEndpointTypeKafka.parse_obj(obj)

        _obj = DataStreamingEndpointTypeKafka.parse_obj({
            "endpoint_type": obj.get("endpoint_type"),
            "use_tls": obj.get("use_tls"),
            "kafka_topic": obj.get("kafka_topic"),
            "bootstrap_servers": obj.get("bootstrap_servers")
        })
        return _obj

