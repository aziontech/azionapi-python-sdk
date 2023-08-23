<a id="__pageTop"></a>
# data_streaming.apis.tags.data_streaming_domain_api.DataStreamingDomainApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_data_streaming**](#list_data_streaming) | **get** /data_streaming/domains | List all domains used on data streaming

# **list_data_streaming**
<a id="list_data_streaming"></a>
> DataStreamingsDomainResponse list_data_streaming()

List all domains used on data streaming

Use the GET method to list all available domains that can be used on Data Streaming operations.

### Example

* Api Key Authentication (tokenAuth):
```python
import data_streaming
from data_streaming.apis.tags import data_streaming_domain_api
from data_streaming.model.data_streamings_domain_response import DataStreamingsDomainResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = data_streaming.Configuration(
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
with data_streaming.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_streaming_domain_api.DataStreamingDomainApi(api_client)

    # example passing only optional values
    query_params = {
        'name': "name_example",
        'streaming_id': 1,
        'selected': True,
    }
    try:
        # List all domains used on data streaming
        api_response = api_instance.list_data_streaming(
            query_params=query_params,
        )
        pprint(api_response)
    except data_streaming.ApiException as e:
        print("Exception when calling DataStreamingDomainApi->list_data_streaming: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | optional
streaming_id | StreamingIdSchema | | optional
selected | SelectedSchema | | optional


# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StreamingIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# SelectedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_data_streaming.ApiResponseFor200) | Successful operation
400 | [ApiResponseFor400](#list_data_streaming.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#list_data_streaming.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#list_data_streaming.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_data_streaming.ApiResponseFor404) | Not Found
406 | [ApiResponseFor406](#list_data_streaming.ApiResponseFor406) | Not Acceptable
429 | [ApiResponseFor429](#list_data_streaming.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#list_data_streaming.ApiResponseFor500) | Internal Server Error

#### list_data_streaming.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DataStreamingsDomainResponse**](../../models/DataStreamingsDomainResponse.md) |  | 


#### list_data_streaming.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_data_streaming.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_data_streaming.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_data_streaming.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_data_streaming.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_data_streaming.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_data_streaming.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

