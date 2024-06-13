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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ApplicationCacheCreateResults(BaseModel):
    """
    ApplicationCacheCreateResults
    """ # noqa: E501
    id: StrictInt
    name: StrictStr
    browser_cache_settings: StrictStr
    browser_cache_settings_maximum_ttl: StrictInt
    cdn_cache_settings: StrictStr
    cdn_cache_settings_maximum_ttl: StrictInt
    cache_by_query_string: StrictStr
    query_string_fields: List[StrictStr]
    enable_query_string_sort: StrictBool
    cache_by_cookies: StrictStr
    cookie_names: List[StrictStr]
    adaptive_delivery_action: StrictStr
    device_group: List[StrictInt]
    enable_caching_for_post: StrictBool
    l2_caching_enabled: StrictBool
    is_slice_configuration_enabled: Optional[StrictBool] = None
    is_slice_edge_caching_enabled: Optional[StrictBool] = None
    is_slice_l2_caching_enabled: Optional[StrictBool] = None
    slice_configuration_range: Optional[StrictInt] = None
    enable_caching_for_options: Optional[StrictBool] = None
    enable_stale_cache: Optional[StrictBool] = None
    l2_region: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "name", "browser_cache_settings", "browser_cache_settings_maximum_ttl", "cdn_cache_settings", "cdn_cache_settings_maximum_ttl", "cache_by_query_string", "query_string_fields", "enable_query_string_sort", "cache_by_cookies", "cookie_names", "adaptive_delivery_action", "device_group", "enable_caching_for_post", "l2_caching_enabled", "is_slice_configuration_enabled", "is_slice_edge_caching_enabled", "is_slice_l2_caching_enabled", "slice_configuration_range", "enable_caching_for_options", "enable_stale_cache", "l2_region"]

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
        """Create an instance of ApplicationCacheCreateResults from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicationCacheCreateResults from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "browser_cache_settings": obj.get("browser_cache_settings"),
            "browser_cache_settings_maximum_ttl": obj.get("browser_cache_settings_maximum_ttl"),
            "cdn_cache_settings": obj.get("cdn_cache_settings"),
            "cdn_cache_settings_maximum_ttl": obj.get("cdn_cache_settings_maximum_ttl"),
            "cache_by_query_string": obj.get("cache_by_query_string"),
            "query_string_fields": obj.get("query_string_fields"),
            "enable_query_string_sort": obj.get("enable_query_string_sort"),
            "cache_by_cookies": obj.get("cache_by_cookies"),
            "cookie_names": obj.get("cookie_names"),
            "adaptive_delivery_action": obj.get("adaptive_delivery_action"),
            "device_group": obj.get("device_group"),
            "enable_caching_for_post": obj.get("enable_caching_for_post"),
            "l2_caching_enabled": obj.get("l2_caching_enabled"),
            "is_slice_configuration_enabled": obj.get("is_slice_configuration_enabled"),
            "is_slice_edge_caching_enabled": obj.get("is_slice_edge_caching_enabled"),
            "is_slice_l2_caching_enabled": obj.get("is_slice_l2_caching_enabled"),
            "slice_configuration_range": obj.get("slice_configuration_range"),
            "enable_caching_for_options": obj.get("enable_caching_for_options"),
            "enable_stale_cache": obj.get("enable_stale_cache"),
            "l2_region": obj.get("l2_region")
        })
        return _obj


