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
from edgeapplications.models.rules_engine_behavior_entry import RulesEngineBehaviorEntry
from edgeapplications.models.rules_engine_criteria import RulesEngineCriteria
from typing import Optional, Set
from typing_extensions import Self

class RulesEngineResultResponse(BaseModel):
    """
    RulesEngineResultResponse
    """ # noqa: E501
    id: StrictInt
    name: StrictStr
    description: Optional[StrictStr] = None
    phase: StrictStr
    behaviors: Optional[List[RulesEngineBehaviorEntry]] = None
    criteria: List[List[RulesEngineCriteria]]
    is_active: StrictBool
    order: StrictInt
    __properties: ClassVar[List[str]] = ["id", "name", "description", "phase", "behaviors", "criteria", "is_active", "order"]

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
        """Create an instance of RulesEngineResultResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in behaviors (list)
        _items = []
        if self.behaviors:
            for _item_behaviors in self.behaviors:
                if _item_behaviors:
                    _items.append(_item_behaviors.to_dict())
            _dict['behaviors'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in criteria (list of list)
        _items = []
        if self.criteria:
            for _item_criteria in self.criteria:
                if _item_criteria:
                    _items.append(
                         [_inner_item.to_dict() for _inner_item in _item_criteria if _inner_item is not None]
                    )
            _dict['criteria'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RulesEngineResultResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "phase": obj.get("phase"),
            "behaviors": [RulesEngineBehaviorEntry.from_dict(_item) for _item in obj["behaviors"]] if obj.get("behaviors") is not None else None,
            "criteria": [
                    [RulesEngineCriteria.from_dict(_inner_item) for _inner_item in _item]
                    for _item in obj["criteria"]
                ] if obj.get("criteria") is not None else None,
            "is_active": obj.get("is_active"),
            "order": obj.get("order")
        })
        return _obj


