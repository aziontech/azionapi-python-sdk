<a id="__pageTop"></a>
# realtimepurge.apis.tags.real_time_purge_api.RealTimePurgeApi

All URIs are relative to *http://localhost:3002*

Method | HTTP request | Description
------------- | ------------- | -------------
[**purge_cache_key**](#purge_cache_key) | **post** /purge/cachekey | /purge/cachekey
[**purge_url**](#purge_url) | **post** /purge/url | /purge/url
[**purge_wildcard**](#purge_wildcard) | **post** /purge/wildcard | /purge/wildcard

# **purge_cache_key**
<a id="purge_cache_key"></a>
> purge_cache_key()

/purge/cachekey

List of Cache Keys you want to remove from the Azion Edge Servers cache.  urls (array): list of up to 50 Cache Keys to be expired from the cache, per request.  method (choice): purge method, use the “delete” value for removal.  Layer (choice): layer where the purge will be done. Use the value “edge_caching” (default value if not informed) to purge on the Edge Caching layer and the value “l2_caching” to purge on L2 Caching.

### Example

* Api Key Authentication (JWT):
```python
import realtimepurge
from realtimepurge.apis.tags import real_time_purge_api
from realtimepurge.model.purge_cache_key_request import PurgeCacheKeyRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3002
# See configuration.py for a list of all supported configuration parameters.
configuration = realtimepurge.Configuration(
    host = "http://localhost:3002"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'
# Enter a context with an instance of the API client
with realtimepurge.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = real_time_purge_api.RealTimePurgeApi(api_client)

    # example passing only optional values
    header_params = {
        'Accept': "application/json; version=3",
        'Content-Type': "application/json",
    }
    body = PurgeCacheKeyRequest(
        urls=[
            "urls_example"
        ],
        method="method_example",
        layer="layer_example",
    )
    try:
        # /purge/cachekey
        api_response = api_instance.purge_cache_key(
            header_params=header_params,
            body=body,
        )
    except realtimepurge.ApiException as e:
        print("Exception when calling RealTimePurgeApi->purge_cache_key: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PurgeCacheKeyRequest**](../../models/PurgeCacheKeyRequest.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Accept | AcceptSchema | | optional
Content-Type | ContentTypeSchema | | optional

# AcceptSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#purge_cache_key.ApiResponseFor200) | Successful response
201 | [ApiResponseFor201](#purge_cache_key.ApiResponseFor201) | Created
204 | [ApiResponseFor204](#purge_cache_key.ApiResponseFor204) | No Content
207 | [ApiResponseFor207](#purge_cache_key.ApiResponseFor207) | Multi Status
400 | [ApiResponseFor400](#purge_cache_key.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#purge_cache_key.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#purge_cache_key.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#purge_cache_key.ApiResponseFor404) | Not Found
405 | [ApiResponseFor405](#purge_cache_key.ApiResponseFor405) | Method Not Allowed
406 | [ApiResponseFor406](#purge_cache_key.ApiResponseFor406) | Not Acceptable
409 | [ApiResponseFor409](#purge_cache_key.ApiResponseFor409) | Conflict
429 | [ApiResponseFor429](#purge_cache_key.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#purge_cache_key.ApiResponseFor500) | Internal Server Error

#### purge_cache_key.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_cache_key.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_cache_key.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_cache_key.ApiResponseFor207
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_cache_key.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_cache_key.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_cache_key.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_cache_key.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_cache_key.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_cache_key.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_cache_key.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_cache_key.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_cache_key.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

[JWT](../../../README.md#JWT)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **purge_url**
<a id="purge_url"></a>
> purge_url()

/purge/url

List of URLs you want to remove from the Azion Edge Servers cache.  urls (array): list of up to 50 URLs to be expired from the cache, per request.  method (choice): purge method, use the “delete” value for removal.

### Example

* Api Key Authentication (JWT):
```python
import realtimepurge
from realtimepurge.apis.tags import real_time_purge_api
from realtimepurge.model.purge_url_request import PurgeUrlRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3002
# See configuration.py for a list of all supported configuration parameters.
configuration = realtimepurge.Configuration(
    host = "http://localhost:3002"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'
# Enter a context with an instance of the API client
with realtimepurge.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = real_time_purge_api.RealTimePurgeApi(api_client)

    # example passing only optional values
    header_params = {
        'Accept': "application/json; version=3",
        'Content-Type': "application/json",
    }
    body = PurgeUrlRequest(
        urls=[
            "urls_example"
        ],
        method="method_example",
    )
    try:
        # /purge/url
        api_response = api_instance.purge_url(
            header_params=header_params,
            body=body,
        )
    except realtimepurge.ApiException as e:
        print("Exception when calling RealTimePurgeApi->purge_url: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonVersion3, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json; version&#x3D;3' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**PurgeUrlRequest**](../../models/PurgeUrlRequest.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Accept | AcceptSchema | | optional
Content-Type | ContentTypeSchema | | optional

# AcceptSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#purge_url.ApiResponseFor200) | Successful response
201 | [ApiResponseFor201](#purge_url.ApiResponseFor201) | Created
204 | [ApiResponseFor204](#purge_url.ApiResponseFor204) | No Content
207 | [ApiResponseFor207](#purge_url.ApiResponseFor207) | Multi Status
400 | [ApiResponseFor400](#purge_url.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#purge_url.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#purge_url.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#purge_url.ApiResponseFor404) | Not Found
405 | [ApiResponseFor405](#purge_url.ApiResponseFor405) | Method Not Allowed
406 | [ApiResponseFor406](#purge_url.ApiResponseFor406) | Not Acceptable
409 | [ApiResponseFor409](#purge_url.ApiResponseFor409) | Conflict
429 | [ApiResponseFor429](#purge_url.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#purge_url.ApiResponseFor500) | Internal Server Error

#### purge_url.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_url.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_url.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_url.ApiResponseFor207
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_url.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_url.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_url.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_url.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_url.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_url.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_url.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_url.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_url.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

[JWT](../../../README.md#JWT)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **purge_wildcard**
<a id="purge_wildcard"></a>
> purge_wildcard()

/purge/wildcard

The Wildcard expression that represents the list of objects that you want to remove from the Azion Edge Servers cache.  urls (array):the Wildcard URL or Wildcard Cache Key that represents the list of objects you want to expire. You can only use one Wildcard expression per request.  method (choice): purge method, use the “delete” value for removal.

### Example

* Api Key Authentication (JWT):
```python
import realtimepurge
from realtimepurge.apis.tags import real_time_purge_api
from realtimepurge.model.purge_wildcard_request import PurgeWildcardRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3002
# See configuration.py for a list of all supported configuration parameters.
configuration = realtimepurge.Configuration(
    host = "http://localhost:3002"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'
# Enter a context with an instance of the API client
with realtimepurge.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = real_time_purge_api.RealTimePurgeApi(api_client)

    # example passing only optional values
    header_params = {
        'Accept': "application/json; version=3",
        'Content-Type': "application/json",
    }
    body = PurgeWildcardRequest(
        urls=[
            "urls_example"
        ],
        method="method_example",
    )
    try:
        # /purge/wildcard
        api_response = api_instance.purge_wildcard(
            header_params=header_params,
            body=body,
        )
    except realtimepurge.ApiException as e:
        print("Exception when calling RealTimePurgeApi->purge_wildcard: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PurgeWildcardRequest**](../../models/PurgeWildcardRequest.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Accept | AcceptSchema | | optional
Content-Type | ContentTypeSchema | | optional

# AcceptSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#purge_wildcard.ApiResponseFor200) | Successful response
201 | [ApiResponseFor201](#purge_wildcard.ApiResponseFor201) | Created
204 | [ApiResponseFor204](#purge_wildcard.ApiResponseFor204) | No Content
207 | [ApiResponseFor207](#purge_wildcard.ApiResponseFor207) | Multi Status
400 | [ApiResponseFor400](#purge_wildcard.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#purge_wildcard.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#purge_wildcard.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#purge_wildcard.ApiResponseFor404) | Not Found
405 | [ApiResponseFor405](#purge_wildcard.ApiResponseFor405) | Method Not Allowed
406 | [ApiResponseFor406](#purge_wildcard.ApiResponseFor406) | Not Acceptable
409 | [ApiResponseFor409](#purge_wildcard.ApiResponseFor409) | Conflict
429 | [ApiResponseFor429](#purge_wildcard.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#purge_wildcard.ApiResponseFor500) | Internal Server Error

#### purge_wildcard.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_wildcard.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_wildcard.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_wildcard.ApiResponseFor207
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_wildcard.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_wildcard.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_wildcard.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_wildcard.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_wildcard.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_wildcard.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_wildcard.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_wildcard.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### purge_wildcard.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

### Authorization

[JWT](../../../README.md#JWT)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

