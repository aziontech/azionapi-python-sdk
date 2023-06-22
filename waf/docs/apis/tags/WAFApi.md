<a id="__pageTop"></a>
# waf.apis.tags.waf_api.WAFApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_waf_domains**](#get_waf_domains) | **get** /waf/{wafId}/domains | Find domains attached to a WAF
[**get_waf_events**](#get_waf_events) | **get** /waf/{wafId}/waf_events | Find WAF log events

# **get_waf_domains**
<a id="get_waf_domains"></a>
> WAFDomains200 get_waf_domains(waf_id)

Find domains attached to a WAF

### Example

* Api Key Authentication (tokenAuth):
```python
import waf
from waf.apis.tags import waf_api
from waf.model.waf_domains200 import WAFDomains200
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = waf.Configuration(
    host = "https://api.azionapi.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'
# Enter a context with an instance of the API client
with waf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = waf_api.WAFApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'wafId': 1,
    }
    query_params = {
    }
    try:
        # Find domains attached to a WAF
        api_response = api_instance.get_waf_domains(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except waf.ApiException as e:
        print("Exception when calling WAFApi->get_waf_domains: %s\n" % e)

    # example passing only optional values
    path_params = {
        'wafId': 1,
    }
    query_params = {
        'name': "name_example",
    }
    try:
        # Find domains attached to a WAF
        api_response = api_instance.get_waf_domains(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except waf.ApiException as e:
        print("Exception when calling WAFApi->get_waf_domains: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | optional


# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
wafId | WafIdSchema | | 

# WafIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_waf_domains.ApiResponseFor200) | successful operation

#### get_waf_domains.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**WAFDomains200**](../../models/WAFDomains200.md) |  | 


### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_waf_events**
<a id="get_waf_events"></a>
> WAFEvents200 get_waf_events(waf_idhour_rangedomains_ids)

Find WAF log events

### Example

* Api Key Authentication (tokenAuth):
```python
import waf
from waf.apis.tags import waf_api
from waf.model.waf_events401 import WAFEvents401
from waf.model.waf_events400 import WAFEvents400
from waf.model.waf_events200 import WAFEvents200
from waf.model.waf_events404 import WAFEvents404
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = waf.Configuration(
    host = "https://api.azionapi.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'
# Enter a context with an instance of the API client
with waf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = waf_api.WAFApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'wafId': 1,
    }
    query_params = {
        'hour_range': 1,
        'domains_ids': "domains_ids_example",
    }
    try:
        # Find WAF log events
        api_response = api_instance.get_waf_events(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except waf.ApiException as e:
        print("Exception when calling WAFApi->get_waf_events: %s\n" % e)

    # example passing only optional values
    path_params = {
        'wafId': 1,
    }
    query_params = {
        'hour_range': 1,
        'network_list_id': 1,
        'domains_ids': "domains_ids_example",
    }
    try:
        # Find WAF log events
        api_response = api_instance.get_waf_events(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except waf.ApiException as e:
        print("Exception when calling WAFApi->get_waf_events: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
hour_range | HourRangeSchema | | 
network_list_id | NetworkListIdSchema | | optional
domains_ids | DomainsIdsSchema | | 


# HourRangeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# NetworkListIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# DomainsIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
wafId | WafIdSchema | | 

# WafIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_waf_events.ApiResponseFor200) | successful operation
400 | [ApiResponseFor400](#get_waf_events.ApiResponseFor400) | Bad request
404 | [ApiResponseFor404](#get_waf_events.ApiResponseFor404) | data not found
401 | [ApiResponseFor401](#get_waf_events.ApiResponseFor401) | unauthorized operation

#### get_waf_events.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**WAFEvents200**](../../models/WAFEvents200.md) |  | 


#### get_waf_events.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**WAFEvents400**](../../models/WAFEvents400.md) |  | 


#### get_waf_events.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**WAFEvents404**](../../models/WAFEvents404.md) |  | 


#### get_waf_events.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**WAFEvents401**](../../models/WAFEvents401.md) |  | 


### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

