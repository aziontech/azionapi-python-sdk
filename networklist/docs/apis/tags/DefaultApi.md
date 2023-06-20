<a id="__pageTop"></a>
# networklist.apis.tags.default_api.DefaultApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**network_lists_get**](#network_lists_get) | **get** /network_lists | List all user Network Lists
[**network_lists_post**](#network_lists_post) | **post** /network_lists | Create a Network Lists
[**network_lists_uuid_get**](#network_lists_uuid_get) | **get** /network_lists/{uuid} | Retrieve a Network Lists set by uuid
[**network_lists_uuid_put**](#network_lists_uuid_put) | **put** /network_lists/{uuid} | Overwrite some Network Lists attributes

# **network_lists_get**
<a id="network_lists_get"></a>
> ListNetworkListsResponse network_lists_get()

List all user Network Lists

### Example

```python
import networklist
from networklist.apis.tags import default_api
from networklist.model.list_network_lists_response import ListNetworkListsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = networklist.Configuration(
    host = "https://api.azionapi.net"
)

# Enter a context with an instance of the API client
with networklist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only optional values
    query_params = {
        'page': 1,
    }
    try:
        # List all user Network Lists
        api_response = api_instance.network_lists_get(
            query_params=query_params,
        )
        pprint(api_response)
    except networklist.ApiException as e:
        print("Exception when calling DefaultApi->network_lists_get: %s\n" % e)
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
page | PageSchema | | optional


# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#network_lists_get.ApiResponseFor200) | A list of Network Lists

#### network_lists_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListNetworkListsResponse**](../../models/ListNetworkListsResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **network_lists_post**
<a id="network_lists_post"></a>
> network_lists_post(create_network_lists_request)

Create a Network Lists

### Example

```python
import networklist
from networklist.apis.tags import default_api
from networklist.model.error_model import ErrorModel
from networklist.model.create_network_lists_request import CreateNetworkListsRequest
from networklist.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = networklist.Configuration(
    host = "https://api.azionapi.net"
)

# Enter a context with an instance of the API client
with networklist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    body = CreateNetworkListsRequest(
        name="Network List created using the API",
        items_values=["192.168.0.1"],
        list_type="ip_cidr",
    )
    try:
        # Create a Network Lists
        api_response = api_instance.network_lists_post(
            body=body,
        )
    except networklist.ApiException as e:
        print("Exception when calling DefaultApi->network_lists_post: %s\n" % e)
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
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateNetworkListsRequest**](../../models/CreateNetworkListsRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#network_lists_post.ApiResponseFor201) | Network Lists created
400 | [ApiResponseFor400](#network_lists_post.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#network_lists_post.ApiResponseFor500) | Internal Server Error

#### network_lists_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### network_lists_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestResponse**](../../models/BadRequestResponse.md) |  | 


#### network_lists_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **network_lists_uuid_get**
<a id="network_lists_uuid_get"></a>
> NetworkListsResponse network_lists_uuid_get(uuid)

Retrieve a Network Lists set by uuid

### Example

```python
import networklist
from networklist.apis.tags import default_api
from networklist.model.network_lists_response import NetworkListsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = networklist.Configuration(
    host = "https://api.azionapi.net"
)

# Enter a context with an instance of the API client
with networklist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'uuid': "uuid_example",
    }
    try:
        # Retrieve a Network Lists set by uuid
        api_response = api_instance.network_lists_uuid_get(
            path_params=path_params,
        )
        pprint(api_response)
    except networklist.ApiException as e:
        print("Exception when calling DefaultApi->network_lists_uuid_get: %s\n" % e)
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
uuid | UuidSchema | | 

# UuidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#network_lists_uuid_get.ApiResponseFor200) | A Network Lists object

#### network_lists_uuid_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NetworkListsResponse**](../../models/NetworkListsResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **network_lists_uuid_put**
<a id="network_lists_uuid_put"></a>
> ListNetworkListsResponse network_lists_uuid_put(uuidupdate_network_lists_request)

Overwrite some Network Lists attributes

### Example

```python
import networklist
from networklist.apis.tags import default_api
from networklist.model.list_network_lists_response import ListNetworkListsResponse
from networklist.model.error_model import ErrorModel
from networklist.model.update_network_lists_request import UpdateNetworkListsRequest
from networklist.model.bad_request_response import BadRequestResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = networklist.Configuration(
    host = "https://api.azionapi.net"
)

# Enter a context with an instance of the API client
with networklist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'uuid': "uuid_example",
    }
    body = UpdateNetworkListsRequest(
        name="Network List created using the API",
        items_values=["192.168.0.1"],
        list_type="ip_cidr",
    )
    try:
        # Overwrite some Network Lists attributes
        api_response = api_instance.network_lists_uuid_put(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except networklist.ApiException as e:
        print("Exception when calling DefaultApi->network_lists_uuid_put: %s\n" % e)
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
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateNetworkListsRequest**](../../models/UpdateNetworkListsRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
uuid | UuidSchema | | 

# UuidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#network_lists_uuid_put.ApiResponseFor200) | Successfully updated
400 | [ApiResponseFor400](#network_lists_uuid_put.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#network_lists_uuid_put.ApiResponseFor500) | Internal Server Error

#### network_lists_uuid_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListNetworkListsResponse**](../../models/ListNetworkListsResponse.md) |  | 


#### network_lists_uuid_put.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestResponse**](../../models/BadRequestResponse.md) |  | 


#### network_lists_uuid_put.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)
