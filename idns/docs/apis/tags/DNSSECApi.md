<a id="__pageTop"></a>
# idns.apis.tags.dnssec_api.DNSSECApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_zone_dns_sec**](#get_zone_dns_sec) | **get** /intelligent_dns/{zone_id}/dnssec | Retrieve the DNSSEC zone status
[**put_zone_dns_sec**](#put_zone_dns_sec) | **patch** /intelligent_dns/{zone_id}/dnssec | Update the DNSSEC zone

# **get_zone_dns_sec**
<a id="get_zone_dns_sec"></a>
> GetOrPatchDnsSecResponse get_zone_dns_sec(zone_id)

Retrieve the DNSSEC zone status

### Example

* Api Key Authentication (tokenAuth):
```python
import idns
from idns.apis.tags import dnssec_api
from idns.model.error_response import ErrorResponse
from idns.model.errors_response import ErrorsResponse
from idns.model.get_or_patch_dns_sec_response import GetOrPatchDnsSecResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = idns.Configuration(
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
with idns.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dnssec_api.DNSSECApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'zone_id': 1,
    }
    try:
        # Retrieve the DNSSEC zone status
        api_response = api_instance.get_zone_dns_sec(
            path_params=path_params,
        )
        pprint(api_response)
    except idns.ApiException as e:
        print("Exception when calling DNSSECApi->get_zone_dns_sec: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
zone_id | ZoneIdSchema | | 

# ZoneIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_zone_dns_sec.ApiResponseFor200) | DNSSEC status retrieved
400 | [ApiResponseFor400](#get_zone_dns_sec.ApiResponseFor400) | Error
404 | [ApiResponseFor404](#get_zone_dns_sec.ApiResponseFor404) | Zone not found
500 | [ApiResponseFor500](#get_zone_dns_sec.ApiResponseFor500) | Error

#### get_zone_dns_sec.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**GetOrPatchDnsSecResponse**](../../models/GetOrPatchDnsSecResponse.md) |  | 


#### get_zone_dns_sec.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorsResponse**](../../models/ErrorsResponse.md) |  | 


#### get_zone_dns_sec.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_zone_dns_sec.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **put_zone_dns_sec**
<a id="put_zone_dns_sec"></a>
> GetOrPatchDnsSecResponse put_zone_dns_sec(zone_id)

Update the DNSSEC zone

### Example

* Api Key Authentication (tokenAuth):
```python
import idns
from idns.apis.tags import dnssec_api
from idns.model.error_response import ErrorResponse
from idns.model.errors_response import ErrorsResponse
from idns.model.get_or_patch_dns_sec_response import GetOrPatchDnsSecResponse
from idns.model.dns_sec import DnsSec
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = idns.Configuration(
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
with idns.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dnssec_api.DNSSECApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'zone_id': 1,
    }
    try:
        # Update the DNSSEC zone
        api_response = api_instance.put_zone_dns_sec(
            path_params=path_params,
        )
        pprint(api_response)
    except idns.ApiException as e:
        print("Exception when calling DNSSECApi->put_zone_dns_sec: %s\n" % e)

    # example passing only optional values
    path_params = {
        'zone_id': 1,
    }
    body = DnsSec(
        is_enabled=True,
        status="unconfigured",
        delegation_signer=DnsSecDelegationSigner(
            digest_type=DnsSecDelegationSignerDigestType(
                id=1,
                slug="slug_example",
            ),
,
            digest="digest_example",
            key_tag=1,
        ),
    )
    try:
        # Update the DNSSEC zone
        api_response = api_instance.put_zone_dns_sec(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except idns.ApiException as e:
        print("Exception when calling DNSSECApi->put_zone_dns_sec: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DnsSec**](../../models/DnsSec.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
zone_id | ZoneIdSchema | | 

# ZoneIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#put_zone_dns_sec.ApiResponseFor200) | DNSSEC status updated
201 | [ApiResponseFor201](#put_zone_dns_sec.ApiResponseFor201) | Zone updated
400 | [ApiResponseFor400](#put_zone_dns_sec.ApiResponseFor400) | Zone update error
404 | [ApiResponseFor404](#put_zone_dns_sec.ApiResponseFor404) | Zone not found

#### put_zone_dns_sec.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**GetOrPatchDnsSecResponse**](../../models/GetOrPatchDnsSecResponse.md) |  | 


#### put_zone_dns_sec.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**GetOrPatchDnsSecResponse**](../../models/GetOrPatchDnsSecResponse.md) |  | 


#### put_zone_dns_sec.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorsResponse**](../../models/ErrorsResponse.md) |  | 


#### put_zone_dns_sec.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

