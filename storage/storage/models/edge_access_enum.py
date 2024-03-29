# coding: utf-8

"""
    Object Storage

    REST API OpenAPI documentation for the Object Storage

    The version of the OpenAPI document: 1.0.0 (v1)
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class EdgeAccessEnum(str, Enum):
    """
    EdgeAccessEnum
    """

    """
    allowed enum values
    """
    READ_ONLY = 'read_only'
    READ_WRITE = 'read_write'
    RESTRICTED = 'restricted'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EdgeAccessEnum from a JSON string"""
        return cls(json.loads(json_str))


