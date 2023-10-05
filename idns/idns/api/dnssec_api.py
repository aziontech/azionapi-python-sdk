# coding: utf-8

"""
    Intelligent DNS API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, conint

from typing import Optional

from idns.models.dns_sec import DnsSec
from idns.models.get_or_patch_dns_sec_response import GetOrPatchDnsSecResponse

from idns.api_client import ApiClient
from idns.api_response import ApiResponse
from idns.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DNSSECApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_zone_dns_sec(self, zone_id : Annotated[conint(strict=True, ge=1), Field(..., description="The hosted zone id")], **kwargs) -> GetOrPatchDnsSecResponse:  # noqa: E501
        """Retrieve the DNSSEC zone status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_zone_dns_sec(zone_id, async_req=True)
        >>> result = thread.get()

        :param zone_id: The hosted zone id (required)
        :type zone_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetOrPatchDnsSecResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_zone_dns_sec_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_zone_dns_sec_with_http_info(zone_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_zone_dns_sec_with_http_info(self, zone_id : Annotated[conint(strict=True, ge=1), Field(..., description="The hosted zone id")], **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve the DNSSEC zone status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_zone_dns_sec_with_http_info(zone_id, async_req=True)
        >>> result = thread.get()

        :param zone_id: The hosted zone id (required)
        :type zone_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetOrPatchDnsSecResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'zone_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_zone_dns_sec" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['zone_id']:
            _path_params['zone_id'] = _params['zone_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; version=3'])  # noqa: E501

        # authentication setting
        _auth_settings = ['tokenAuth']  # noqa: E501

        _response_types_map = {
            '200': "GetOrPatchDnsSecResponse",
            '400': "ErrorsResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
        }

        return self.api_client.call_api(
            '/intelligent_dns/{zone_id}/dnssec', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def put_zone_dns_sec(self, zone_id : Annotated[conint(strict=True, ge=1), Field(..., description="The hosted zone id")], dns_sec : Optional[DnsSec] = None, **kwargs) -> GetOrPatchDnsSecResponse:  # noqa: E501
        """Update the DNSSEC zone  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.put_zone_dns_sec(zone_id, dns_sec, async_req=True)
        >>> result = thread.get()

        :param zone_id: The hosted zone id (required)
        :type zone_id: int
        :param dns_sec:
        :type dns_sec: DnsSec
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetOrPatchDnsSecResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the put_zone_dns_sec_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.put_zone_dns_sec_with_http_info(zone_id, dns_sec, **kwargs)  # noqa: E501

    @validate_arguments
    def put_zone_dns_sec_with_http_info(self, zone_id : Annotated[conint(strict=True, ge=1), Field(..., description="The hosted zone id")], dns_sec : Optional[DnsSec] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Update the DNSSEC zone  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.put_zone_dns_sec_with_http_info(zone_id, dns_sec, async_req=True)
        >>> result = thread.get()

        :param zone_id: The hosted zone id (required)
        :type zone_id: int
        :param dns_sec:
        :type dns_sec: DnsSec
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetOrPatchDnsSecResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'zone_id',
            'dns_sec'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_zone_dns_sec" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['zone_id']:
            _path_params['zone_id'] = _params['zone_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['dns_sec'] is not None:
            _body_params = _params['dns_sec']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; version=3'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['tokenAuth']  # noqa: E501

        _response_types_map = {
            '200': "GetOrPatchDnsSecResponse",
            '201': "GetOrPatchDnsSecResponse",
            '400': "ErrorsResponse",
            '404': "ErrorResponse",
        }

        return self.api_client.call_api(
            '/intelligent_dns/{zone_id}/dnssec', 'PATCH',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
