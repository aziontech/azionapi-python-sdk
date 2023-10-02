# coding: utf-8

"""
    Edge Firewall API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel
from edgefirewall.models.conditionals import Conditionals
from edgefirewall.models.ssl_verification_status_arguments import SSLVerificationStatusArguments
from edgefirewall.models.ssl_verification_status_operators import SSLVerificationStatusOperators
from edgefirewall.models.variables import Variables

class SSLVerificationStatusCriteria(BaseModel):
    """
    SSLVerificationStatusCriteria
    """
    variable: Optional[Variables] = None
    operator: Optional[SSLVerificationStatusOperators] = None
    conditional: Optional[Conditionals] = None
    input_value: Optional[SSLVerificationStatusArguments] = None
    __properties = ["variable", "operator", "conditional", "input_value"]

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
    def from_json(cls, json_str: str) -> SSLVerificationStatusCriteria:
        """Create an instance of SSLVerificationStatusCriteria from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SSLVerificationStatusCriteria:
        """Create an instance of SSLVerificationStatusCriteria from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SSLVerificationStatusCriteria.parse_obj(obj)

        _obj = SSLVerificationStatusCriteria.parse_obj({
            "variable": obj.get("variable"),
            "operator": obj.get("operator"),
            "conditional": obj.get("conditional"),
            "input_value": obj.get("input_value")
        })
        return _obj


