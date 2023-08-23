<a id="__pageTop"></a>
# data_streaming.apis.tags.data_streaming_api.DataStreamingApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_data_streaming**](#create_new_data_streaming) | **post** /data_streaming/streamings | Create a new data streaming
[**delete_data_streaming_by_id**](#delete_data_streaming_by_id) | **delete** /data_streaming/streamings/{data_streaming_id} | Delete data streaming
[**edit_data_streaming_by_id**](#edit_data_streaming_by_id) | **patch** /data_streaming/streamings/{data_streaming_id} | Edit data streaming
[**list_data_streaming_by_id**](#list_data_streaming_by_id) | **get** /data_streaming/streamings/{data_streaming_id} | Get expecific data streaming by Data Streaming ID
[**list_data_streamings**](#list_data_streamings) | **get** /data_streaming/streamings | List all exist data streamings
[**overwrite_data_streaming_by_id**](#overwrite_data_streaming_by_id) | **put** /data_streaming/streamings/{data_streaming_id} | Overwrite data streaming

# **create_new_data_streaming**
<a id="create_new_data_streaming"></a>
> bool, date, datetime, dict, float, int, list, str, none_type create_new_data_streaming(any_type)

Create a new data streaming

### Example

* Api Key Authentication (tokenAuth):
```python
import data_streaming
from data_streaming.apis.tags import data_streaming_api
from data_streaming.model.data_streaming_post_body import DataStreamingPostBody
from data_streaming.model.create_custom_data_streaming_response import CreateCustomDataStreamingResponse
from data_streaming.model.standard_data_streaming_post_body import StandardDataStreamingPostBody
from data_streaming.model.custom_data_streaming_post_body import CustomDataStreamingPostBody
from data_streaming.model.create_data_streaming_response import CreateDataStreamingResponse
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
    api_instance = data_streaming_api.DataStreamingApi(api_client)

    # example passing only required values which don't have defaults set
    body = None
    try:
        # Create a new data streaming
        api_response = api_instance.create_new_data_streaming(
            body=body,
        )
        pprint(api_response)
    except data_streaming.ApiException as e:
        print("Exception when calling DataStreamingApi->create_new_data_streaming: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[DataStreamingPostBody]({{complexTypePrefix}}DataStreamingPostBody.md) | [**DataStreamingPostBody**]({{complexTypePrefix}}DataStreamingPostBody.md) | [**DataStreamingPostBody**]({{complexTypePrefix}}DataStreamingPostBody.md) |  | 
[StandardDataStreamingPostBody]({{complexTypePrefix}}StandardDataStreamingPostBody.md) | [**StandardDataStreamingPostBody**]({{complexTypePrefix}}StandardDataStreamingPostBody.md) | [**StandardDataStreamingPostBody**]({{complexTypePrefix}}StandardDataStreamingPostBody.md) |  | 
[CustomDataStreamingPostBody]({{complexTypePrefix}}CustomDataStreamingPostBody.md) | [**CustomDataStreamingPostBody**]({{complexTypePrefix}}CustomDataStreamingPostBody.md) | [**CustomDataStreamingPostBody**]({{complexTypePrefix}}CustomDataStreamingPostBody.md) |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_new_data_streaming.ApiResponseFor201) | Created successfully
400 | [ApiResponseFor400](#create_new_data_streaming.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#create_new_data_streaming.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#create_new_data_streaming.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_new_data_streaming.ApiResponseFor404) | Not Found
406 | [ApiResponseFor406](#create_new_data_streaming.ApiResponseFor406) | Not Acceptable
429 | [ApiResponseFor429](#create_new_data_streaming.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#create_new_data_streaming.ApiResponseFor500) | Internal Server Error

#### create_new_data_streaming.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[CreateDataStreamingResponse]({{complexTypePrefix}}CreateDataStreamingResponse.md) | [**CreateDataStreamingResponse**]({{complexTypePrefix}}CreateDataStreamingResponse.md) | [**CreateDataStreamingResponse**]({{complexTypePrefix}}CreateDataStreamingResponse.md) |  | 
[CreateCustomDataStreamingResponse]({{complexTypePrefix}}CreateCustomDataStreamingResponse.md) | [**CreateCustomDataStreamingResponse**]({{complexTypePrefix}}CreateCustomDataStreamingResponse.md) | [**CreateCustomDataStreamingResponse**]({{complexTypePrefix}}CreateCustomDataStreamingResponse.md) |  | 

#### create_new_data_streaming.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_new_data_streaming.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_new_data_streaming.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_new_data_streaming.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_new_data_streaming.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_new_data_streaming.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_new_data_streaming.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_data_streaming_by_id**
<a id="delete_data_streaming_by_id"></a>
> delete_data_streaming_by_id(data_streaming_id)

Delete data streaming

Use the DELETE method to remove a data streaming from your account. 

### Example

* Api Key Authentication (tokenAuth):
```python
import data_streaming
from data_streaming.apis.tags import data_streaming_api
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
    api_instance = data_streaming_api.DataStreamingApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'data_streaming_id': 1,
    }
    try:
        # Delete data streaming
        api_response = api_instance.delete_data_streaming_by_id(
            path_params=path_params,
        )
    except data_streaming.ApiException as e:
        print("Exception when calling DataStreamingApi->delete_data_streaming_by_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
data_streaming_id | DataStreamingIdSchema | | 

# DataStreamingIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_data_streaming_by_id.ApiResponseFor204) | Successful operation
400 | [ApiResponseFor400](#delete_data_streaming_by_id.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#delete_data_streaming_by_id.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#delete_data_streaming_by_id.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_data_streaming_by_id.ApiResponseFor404) | Not Found
406 | [ApiResponseFor406](#delete_data_streaming_by_id.ApiResponseFor406) | Not Acceptable
429 | [ApiResponseFor429](#delete_data_streaming_by_id.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#delete_data_streaming_by_id.ApiResponseFor500) | Internal Server Error

#### delete_data_streaming_by_id.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_data_streaming_by_id.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_data_streaming_by_id.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_data_streaming_by_id.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_data_streaming_by_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_data_streaming_by_id.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_data_streaming_by_id.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_data_streaming_by_id.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edit_data_streaming_by_id**
<a id="edit_data_streaming_by_id"></a>
> bool, date, datetime, dict, float, int, list, str, none_type edit_data_streaming_by_id(data_streaming_idany_type)

Edit data streaming

Use the PATCH method to change only select settings of your data streaming. 

### Example

* Api Key Authentication (tokenAuth):
```python
import data_streaming
from data_streaming.apis.tags import data_streaming_api
from data_streaming.model.data_streaming_post_body import DataStreamingPostBody
from data_streaming.model.create_custom_data_streaming_response import CreateCustomDataStreamingResponse
from data_streaming.model.standard_data_streaming_post_body import StandardDataStreamingPostBody
from data_streaming.model.custom_data_streaming_post_body import CustomDataStreamingPostBody
from data_streaming.model.create_data_streaming_response import CreateDataStreamingResponse
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
    api_instance = data_streaming_api.DataStreamingApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'data_streaming_id': 1,
    }
    body = None
    try:
        # Edit data streaming
        api_response = api_instance.edit_data_streaming_by_id(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except data_streaming.ApiException as e:
        print("Exception when calling DataStreamingApi->edit_data_streaming_by_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[DataStreamingPostBody]({{complexTypePrefix}}DataStreamingPostBody.md) | [**DataStreamingPostBody**]({{complexTypePrefix}}DataStreamingPostBody.md) | [**DataStreamingPostBody**]({{complexTypePrefix}}DataStreamingPostBody.md) |  | 
[StandardDataStreamingPostBody]({{complexTypePrefix}}StandardDataStreamingPostBody.md) | [**StandardDataStreamingPostBody**]({{complexTypePrefix}}StandardDataStreamingPostBody.md) | [**StandardDataStreamingPostBody**]({{complexTypePrefix}}StandardDataStreamingPostBody.md) |  | 
[CustomDataStreamingPostBody]({{complexTypePrefix}}CustomDataStreamingPostBody.md) | [**CustomDataStreamingPostBody**]({{complexTypePrefix}}CustomDataStreamingPostBody.md) | [**CustomDataStreamingPostBody**]({{complexTypePrefix}}CustomDataStreamingPostBody.md) |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
data_streaming_id | DataStreamingIdSchema | | 

# DataStreamingIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edit_data_streaming_by_id.ApiResponseFor200) | Successful operation
400 | [ApiResponseFor400](#edit_data_streaming_by_id.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#edit_data_streaming_by_id.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#edit_data_streaming_by_id.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edit_data_streaming_by_id.ApiResponseFor404) | Not Found
406 | [ApiResponseFor406](#edit_data_streaming_by_id.ApiResponseFor406) | Not Acceptable
429 | [ApiResponseFor429](#edit_data_streaming_by_id.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#edit_data_streaming_by_id.ApiResponseFor500) | Internal Server Error

#### edit_data_streaming_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[CreateDataStreamingResponse]({{complexTypePrefix}}CreateDataStreamingResponse.md) | [**CreateDataStreamingResponse**]({{complexTypePrefix}}CreateDataStreamingResponse.md) | [**CreateDataStreamingResponse**]({{complexTypePrefix}}CreateDataStreamingResponse.md) |  | 
[CreateCustomDataStreamingResponse]({{complexTypePrefix}}CreateCustomDataStreamingResponse.md) | [**CreateCustomDataStreamingResponse**]({{complexTypePrefix}}CreateCustomDataStreamingResponse.md) | [**CreateCustomDataStreamingResponse**]({{complexTypePrefix}}CreateCustomDataStreamingResponse.md) |  | 

#### edit_data_streaming_by_id.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edit_data_streaming_by_id.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edit_data_streaming_by_id.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edit_data_streaming_by_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edit_data_streaming_by_id.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edit_data_streaming_by_id.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edit_data_streaming_by_id.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_data_streaming_by_id**
<a id="list_data_streaming_by_id"></a>
> DataStreamingsById list_data_streaming_by_id(data_streaming_id)

Get expecific data streaming by Data Streaming ID

Use the GET method and add the data streaming's ID to the URI of the request to get more data on a specific data streaming.

### Example

* Api Key Authentication (tokenAuth):
```python
import data_streaming
from data_streaming.apis.tags import data_streaming_api
from data_streaming.model.data_streamings_by_id import DataStreamingsById
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
    api_instance = data_streaming_api.DataStreamingApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'data_streaming_id': 1,
    }
    try:
        # Get expecific data streaming by Data Streaming ID
        api_response = api_instance.list_data_streaming_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except data_streaming.ApiException as e:
        print("Exception when calling DataStreamingApi->list_data_streaming_by_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
data_streaming_id | DataStreamingIdSchema | | 

# DataStreamingIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_data_streaming_by_id.ApiResponseFor200) | Successful operation
400 | [ApiResponseFor400](#list_data_streaming_by_id.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#list_data_streaming_by_id.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#list_data_streaming_by_id.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_data_streaming_by_id.ApiResponseFor404) | Not Found
406 | [ApiResponseFor406](#list_data_streaming_by_id.ApiResponseFor406) | Not Acceptable
429 | [ApiResponseFor429](#list_data_streaming_by_id.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#list_data_streaming_by_id.ApiResponseFor500) | Internal Server Error

#### list_data_streaming_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DataStreamingsById**](../../models/DataStreamingsById.md) |  | 


#### list_data_streaming_by_id.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_data_streaming_by_id.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_data_streaming_by_id.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_data_streaming_by_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_data_streaming_by_id.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_data_streaming_by_id.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_data_streaming_by_id.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_data_streamings**
<a id="list_data_streamings"></a>
> DataStreamingResponseWithResults list_data_streamings()

List all exist data streamings

Use the GET method to list all data streamings, both active and inactive, and its properties.

### Example

* Api Key Authentication (tokenAuth):
```python
import data_streaming
from data_streaming.apis.tags import data_streaming_api
from data_streaming.model.data_streaming_response_with_results import DataStreamingResponseWithResults
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
    api_instance = data_streaming_api.DataStreamingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all exist data streamings
        api_response = api_instance.list_data_streamings()
        pprint(api_response)
    except data_streaming.ApiException as e:
        print("Exception when calling DataStreamingApi->list_data_streamings: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_data_streamings.ApiResponseFor200) | Successful operation
400 | [ApiResponseFor400](#list_data_streamings.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#list_data_streamings.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#list_data_streamings.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_data_streamings.ApiResponseFor404) | Not Found
406 | [ApiResponseFor406](#list_data_streamings.ApiResponseFor406) | Not Acceptable
429 | [ApiResponseFor429](#list_data_streamings.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#list_data_streamings.ApiResponseFor500) | Internal Server Error

#### list_data_streamings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DataStreamingResponseWithResults**](../../models/DataStreamingResponseWithResults.md) |  | 


#### list_data_streamings.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_data_streamings.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_data_streamings.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_data_streamings.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_data_streamings.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_data_streamings.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_data_streamings.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **overwrite_data_streaming_by_id**
<a id="overwrite_data_streaming_by_id"></a>
> bool, date, datetime, dict, float, int, list, str, none_type overwrite_data_streaming_by_id(data_streaming_idany_type)

Overwrite data streaming

Use the PUT method to overwrite the data streaming. Although  you can change a single property using the PUT method, you must pass all fields for the request to be completed. 

### Example

* Api Key Authentication (tokenAuth):
```python
import data_streaming
from data_streaming.apis.tags import data_streaming_api
from data_streaming.model.data_streaming_post_body import DataStreamingPostBody
from data_streaming.model.create_custom_data_streaming_response import CreateCustomDataStreamingResponse
from data_streaming.model.standard_data_streaming_post_body import StandardDataStreamingPostBody
from data_streaming.model.custom_data_streaming_post_body import CustomDataStreamingPostBody
from data_streaming.model.create_data_streaming_response import CreateDataStreamingResponse
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
    api_instance = data_streaming_api.DataStreamingApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'data_streaming_id': 1,
    }
    body = None
    try:
        # Overwrite data streaming
        api_response = api_instance.overwrite_data_streaming_by_id(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except data_streaming.ApiException as e:
        print("Exception when calling DataStreamingApi->overwrite_data_streaming_by_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[DataStreamingPostBody]({{complexTypePrefix}}DataStreamingPostBody.md) | [**DataStreamingPostBody**]({{complexTypePrefix}}DataStreamingPostBody.md) | [**DataStreamingPostBody**]({{complexTypePrefix}}DataStreamingPostBody.md) |  | 
[StandardDataStreamingPostBody]({{complexTypePrefix}}StandardDataStreamingPostBody.md) | [**StandardDataStreamingPostBody**]({{complexTypePrefix}}StandardDataStreamingPostBody.md) | [**StandardDataStreamingPostBody**]({{complexTypePrefix}}StandardDataStreamingPostBody.md) |  | 
[CustomDataStreamingPostBody]({{complexTypePrefix}}CustomDataStreamingPostBody.md) | [**CustomDataStreamingPostBody**]({{complexTypePrefix}}CustomDataStreamingPostBody.md) | [**CustomDataStreamingPostBody**]({{complexTypePrefix}}CustomDataStreamingPostBody.md) |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
data_streaming_id | DataStreamingIdSchema | | 

# DataStreamingIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#overwrite_data_streaming_by_id.ApiResponseFor200) | Successful operation
400 | [ApiResponseFor400](#overwrite_data_streaming_by_id.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#overwrite_data_streaming_by_id.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#overwrite_data_streaming_by_id.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#overwrite_data_streaming_by_id.ApiResponseFor404) | Not Found
406 | [ApiResponseFor406](#overwrite_data_streaming_by_id.ApiResponseFor406) | Not Acceptable
409 | [ApiResponseFor409](#overwrite_data_streaming_by_id.ApiResponseFor409) | Conflict
429 | [ApiResponseFor429](#overwrite_data_streaming_by_id.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#overwrite_data_streaming_by_id.ApiResponseFor500) | Internal Server Error

#### overwrite_data_streaming_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[CreateDataStreamingResponse]({{complexTypePrefix}}CreateDataStreamingResponse.md) | [**CreateDataStreamingResponse**]({{complexTypePrefix}}CreateDataStreamingResponse.md) | [**CreateDataStreamingResponse**]({{complexTypePrefix}}CreateDataStreamingResponse.md) |  | 
[CreateCustomDataStreamingResponse]({{complexTypePrefix}}CreateCustomDataStreamingResponse.md) | [**CreateCustomDataStreamingResponse**]({{complexTypePrefix}}CreateCustomDataStreamingResponse.md) | [**CreateCustomDataStreamingResponse**]({{complexTypePrefix}}CreateCustomDataStreamingResponse.md) |  | 

#### overwrite_data_streaming_by_id.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### overwrite_data_streaming_by_id.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### overwrite_data_streaming_by_id.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### overwrite_data_streaming_by_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### overwrite_data_streaming_by_id.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### overwrite_data_streaming_by_id.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### overwrite_data_streaming_by_id.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### overwrite_data_streaming_by_id.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

