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

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List
from edgeapplications.models.application_cache_results import ApplicationCacheResults
from edgeapplications.models.application_links import ApplicationLinks
from typing import Optional, Set
from typing_extensions import Self

class ApplicationCacheGetResponse(BaseModel):
    """
    ApplicationCacheGetResponse
    """ # noqa: E501
    count: StrictInt
    total_pages: StrictInt
    schema_version: StrictInt
    links: ApplicationLinks
    results: List[ApplicationCacheResults]
    __properties: ClassVar[List[str]] = ["count", "total_pages", "schema_version", "links", "results"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ApplicationCacheGetResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
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
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationCacheGetResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "count": obj.get("count"),
            "total_pages": obj.get("total_pages"),
            "schema_version": obj.get("schema_version"),
            "links": ApplicationLinks.from_dict(obj["links"]) if obj.get("links") is not None else None,
            "results": [ApplicationCacheResults.from_dict(_item) for _item in obj["results"]] if obj.get("results") is not None else None
        })
        return _obj


