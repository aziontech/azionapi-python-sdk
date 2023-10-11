# coding: utf-8

"""
    Edge Firewall API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class SSLVerificationStatusOperators(str, Enum):
    """
    SSLVerificationStatusOperators
    """

    """
    allowed enum values
    """
    IS_EQUAL = 'is_equal'
    IS_NOT_EQUAL = 'is_not_equal'

    @classmethod
    def from_json(cls, json_str: str) -> SSLVerificationStatusOperators:
        """Create an instance of SSLVerificationStatusOperators from a JSON string"""
        return SSLVerificationStatusOperators(json.loads(json_str))

