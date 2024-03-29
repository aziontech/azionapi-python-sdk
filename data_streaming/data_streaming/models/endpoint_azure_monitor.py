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
from pydantic import BaseModel, StrictStr, constr, validator

class EndpointAzureMonitor(BaseModel):
    """
    EndpointAzureMonitor
    """
    endpoint_type: Optional[StrictStr] = None
    log_type: Optional[StrictStr] = None
    shared_key: Optional[StrictStr] = None
    time_generated_field: Optional[StrictStr] = None
    workspace_id: Optional[constr(strict=True)] = None
    __properties = ["endpoint_type", "log_type", "shared_key", "time_generated_field", "workspace_id"]

    @validator('workspace_id')
    def workspace_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{6}", value):
            raise ValueError(r"must validate the regular expression /[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{6}/")
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
    def from_json(cls, json_str: str) -> EndpointAzureMonitor:
        """Create an instance of EndpointAzureMonitor from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EndpointAzureMonitor:
        """Create an instance of EndpointAzureMonitor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EndpointAzureMonitor.parse_obj(obj)

        _obj = EndpointAzureMonitor.parse_obj({
            "endpoint_type": obj.get("endpoint_type"),
            "log_type": obj.get("log_type"),
            "shared_key": obj.get("shared_key"),
            "time_generated_field": obj.get("time_generated_field"),
            "workspace_id": obj.get("workspace_id")
        })
        return _obj


