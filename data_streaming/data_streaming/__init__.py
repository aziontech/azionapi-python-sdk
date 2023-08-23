# coding: utf-8

# flake8: noqa

"""
    Data Streaming - OpenAPI

    The Data Streaming API allows you to manage your existing data streamings and templates. Data Streaming allows you to feed your stream processing, SIEM, and big data platforms with the event logs from your applications on Azion in real time.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

__version__ = "1.0.0"

# import ApiClient
from data_streaming.api_client import ApiClient

# import Configuration
from data_streaming.configuration import Configuration

# import exceptions
from data_streaming.exceptions import OpenApiException
from data_streaming.exceptions import ApiAttributeError
from data_streaming.exceptions import ApiTypeError
from data_streaming.exceptions import ApiValueError
from data_streaming.exceptions import ApiKeyError
from data_streaming.exceptions import ApiException