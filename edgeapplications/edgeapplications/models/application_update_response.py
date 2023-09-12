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



from pydantic import BaseModel, Field, StrictInt
from edgeapplications.models.application_update_results import ApplicationUpdateResults

class ApplicationUpdateResponse(BaseModel):
    """
    ApplicationUpdateResponse
    """
    results: ApplicationUpdateResults = Field(...)
    schema_version: StrictInt = Field(...)
    __properties = ["results", "schema_version"]

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
    def from_json(cls, json_str: str) -> ApplicationUpdateResponse:
        """Create an instance of ApplicationUpdateResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of results
        if self.results:
            _dict['results'] = self.results.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApplicationUpdateResponse:
        """Create an instance of ApplicationUpdateResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApplicationUpdateResponse.parse_obj(obj)

        _obj = ApplicationUpdateResponse.parse_obj({
            "results": ApplicationUpdateResults.from_dict(obj.get("results")) if obj.get("results") is not None else None,
            "schema_version": obj.get("schema_version")
        })
        return _obj


