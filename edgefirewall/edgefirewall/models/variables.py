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





class Variables(str, Enum):
    """
    Variables
    """

    """
    allowed enum values
    """
    HEADER_ACCEPT = 'header_accept'
    HEADER_ACCEPT_ENCODING = 'header_accept_encoding'
    HEADER_ACCEPT_LANGUAGE = 'header_accept_language'
    HEADER_COOKIE = 'header_cookie'
    HEADER_ORIGIN = 'header_origin'
    HEADER_REFERER = 'header_referer'
    HEADER_USER_AGENT = 'header_user_agent'
    HOST = 'host'
    NETWORK = 'network'
    REQUEST_ARGS = 'request_args'
    REQUEST_METHOD = 'request_method'
    REQUEST_URI = 'request_uri'
    SCHEME = 'scheme'
    CLIENT_CERTIFICATE_VALIDATION = 'client_certificate_validation'

    @classmethod
    def from_json(cls, json_str: str) -> Variables:
        """Create an instance of Variables from a JSON string"""
        return Variables(json.loads(json_str))


