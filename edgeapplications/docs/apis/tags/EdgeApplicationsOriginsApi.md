<a id="__pageTop"></a>
# edgeapplications.apis.tags.edge_applications_origins_api.EdgeApplicationsOriginsApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edge_applications_edge_application_id_origins_get**](#edge_applications_edge_application_id_origins_get) | **get** /edge_applications/{edge_application_id}/origins | /edge_applications/{edge_application_id}/origins
[**edge_applications_edge_application_id_origins_origin_key_delete**](#edge_applications_edge_application_id_origins_origin_key_delete) | **delete** /edge_applications/{edge_application_id}/origins/{origin_key} | /edge_applications/{edge_application_id}/origins/{origin_id}
[**edge_applications_edge_application_id_origins_origin_key_get**](#edge_applications_edge_application_id_origins_origin_key_get) | **get** /edge_applications/{edge_application_id}/origins/{origin_key} | /edge_applications/{edge_application_id}/origins/{origin_key}
[**edge_applications_edge_application_id_origins_origin_key_patch**](#edge_applications_edge_application_id_origins_origin_key_patch) | **patch** /edge_applications/{edge_application_id}/origins/{origin_key} | /edge_applications/:edge_application_id:/origins/:origin_id:
[**edge_applications_edge_application_id_origins_origin_key_put**](#edge_applications_edge_application_id_origins_origin_key_put) | **put** /edge_applications/{edge_application_id}/origins/{origin_key} | /edge_applications/{edge_application_id}/origins/{origin_id}
[**edge_applications_edge_application_id_origins_post**](#edge_applications_edge_application_id_origins_post) | **post** /edge_applications/{edge_application_id}/origins | /edge_applications/{edge_application_id}/origins

# **edge_applications_edge_application_id_origins_get**
<a id="edge_applications_edge_application_id_origins_get"></a>
> OriginsResponse edge_applications_edge_application_id_origins_get(edge_application_id)

/edge_applications/{edge_application_id}/origins

### Example

* Api Key Authentication (tokenAuth):
```python
import edgeapplications
from edgeapplications.apis.tags import edge_applications_origins_api
from edgeapplications.model.origins_response import OriginsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgeapplications.Configuration(
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
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edge_applications_origins_api.EdgeApplicationsOriginsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edge_application_id': 1,
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # /edge_applications/{edge_application_id}/origins
        api_response = api_instance.edge_applications_edge_application_id_origins_get(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsOriginsApi->edge_applications_edge_application_id_origins_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'edge_application_id': 1,
    }
    query_params = {
        'page': 1,
        'page_size': 1,
        'filter': "filter_example",
        'order_by': "order_by_example",
        'sort': "sort_example",
    }
    header_params = {
        'Accept': "application/json; version=3",
    }
    try:
        # /edge_applications/{edge_application_id}/origins
        api_response = api_instance.edge_applications_edge_application_id_origins_get(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsOriginsApi->edge_applications_edge_application_id_origins_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page | PageSchema | | optional
page_size | PageSizeSchema | | optional
filter | FilterSchema | | optional
order_by | OrderBySchema | | optional
sort | SortSchema | | optional


# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# FilterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrderBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Accept | AcceptSchema | | optional

# AcceptSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
edge_application_id | EdgeApplicationIdSchema | | 

# EdgeApplicationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edge_applications_edge_application_id_origins_get.ApiResponseFor200) | Successful response
400 | [ApiResponseFor400](#edge_applications_edge_application_id_origins_get.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#edge_applications_edge_application_id_origins_get.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edge_applications_edge_application_id_origins_get.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#edge_applications_edge_application_id_origins_get.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#edge_applications_edge_application_id_origins_get.ApiResponseFor500) | Internal Server Error

#### edge_applications_edge_application_id_origins_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**OriginsResponse**](../../models/OriginsResponse.md) |  | 


#### edge_applications_edge_application_id_origins_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_origins_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_origins_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_origins_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_origins_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edge_applications_edge_application_id_origins_origin_key_delete**
<a id="edge_applications_edge_application_id_origins_origin_key_delete"></a>
> edge_applications_edge_application_id_origins_origin_key_delete(edge_application_idorigin_key)

/edge_applications/{edge_application_id}/origins/{origin_id}

### Example

* Api Key Authentication (tokenAuth):
```python
import edgeapplications
from edgeapplications.apis.tags import edge_applications_origins_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgeapplications.Configuration(
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
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edge_applications_origins_api.EdgeApplicationsOriginsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edge_application_id': 1,
        'origin_key': "origin_key_example",
    }
    header_params = {
    }
    try:
        # /edge_applications/{edge_application_id}/origins/{origin_id}
        api_response = api_instance.edge_applications_edge_application_id_origins_origin_key_delete(
            path_params=path_params,
            header_params=header_params,
        )
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsOriginsApi->edge_applications_edge_application_id_origins_origin_key_delete: %s\n" % e)

    # example passing only optional values
    path_params = {
        'edge_application_id': 1,
        'origin_key': "origin_key_example",
    }
    header_params = {
        'Accept': "application/json; version=3",
    }
    try:
        # /edge_applications/{edge_application_id}/origins/{origin_id}
        api_response = api_instance.edge_applications_edge_application_id_origins_origin_key_delete(
            path_params=path_params,
            header_params=header_params,
        )
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsOriginsApi->edge_applications_edge_application_id_origins_origin_key_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Accept | AcceptSchema | | optional

# AcceptSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
edge_application_id | EdgeApplicationIdSchema | | 
origin_key | OriginKeySchema | | 

# EdgeApplicationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# OriginKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#edge_applications_edge_application_id_origins_origin_key_delete.ApiResponseFor204) | No response
400 | [ApiResponseFor400](#edge_applications_edge_application_id_origins_origin_key_delete.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#edge_applications_edge_application_id_origins_origin_key_delete.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edge_applications_edge_application_id_origins_origin_key_delete.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#edge_applications_edge_application_id_origins_origin_key_delete.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#edge_applications_edge_application_id_origins_origin_key_delete.ApiResponseFor500) | Internal Server Error

#### edge_applications_edge_application_id_origins_origin_key_delete.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_origins_origin_key_delete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_origins_origin_key_delete.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_origins_origin_key_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_origins_origin_key_delete.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_origins_origin_key_delete.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edge_applications_edge_application_id_origins_origin_key_get**
<a id="edge_applications_edge_application_id_origins_origin_key_get"></a>
> OriginsIdResponse edge_applications_edge_application_id_origins_origin_key_get(edge_application_idorigin_key)

/edge_applications/{edge_application_id}/origins/{origin_key}

### Example

* Api Key Authentication (tokenAuth):
```python
import edgeapplications
from edgeapplications.apis.tags import edge_applications_origins_api
from edgeapplications.model.origins_id_response import OriginsIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgeapplications.Configuration(
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
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edge_applications_origins_api.EdgeApplicationsOriginsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edge_application_id': 1,
        'origin_key': "origin_key_example",
    }
    header_params = {
    }
    try:
        # /edge_applications/{edge_application_id}/origins/{origin_key}
        api_response = api_instance.edge_applications_edge_application_id_origins_origin_key_get(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsOriginsApi->edge_applications_edge_application_id_origins_origin_key_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'edge_application_id': 1,
        'origin_key': "origin_key_example",
    }
    header_params = {
        'Accept': "application/json; version=3",
    }
    try:
        # /edge_applications/{edge_application_id}/origins/{origin_key}
        api_response = api_instance.edge_applications_edge_application_id_origins_origin_key_get(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsOriginsApi->edge_applications_edge_application_id_origins_origin_key_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Accept | AcceptSchema | | optional

# AcceptSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
edge_application_id | EdgeApplicationIdSchema | | 
origin_key | OriginKeySchema | | 

# EdgeApplicationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# OriginKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edge_applications_edge_application_id_origins_origin_key_get.ApiResponseFor200) | Successful response
400 | [ApiResponseFor400](#edge_applications_edge_application_id_origins_origin_key_get.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#edge_applications_edge_application_id_origins_origin_key_get.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edge_applications_edge_application_id_origins_origin_key_get.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#edge_applications_edge_application_id_origins_origin_key_get.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#edge_applications_edge_application_id_origins_origin_key_get.ApiResponseFor500) | Internal Server Error

#### edge_applications_edge_application_id_origins_origin_key_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**OriginsIdResponse**](../../models/OriginsIdResponse.md) |  | 


#### edge_applications_edge_application_id_origins_origin_key_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_origins_origin_key_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_origins_origin_key_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_origins_origin_key_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_origins_origin_key_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edge_applications_edge_application_id_origins_origin_key_patch**
<a id="edge_applications_edge_application_id_origins_origin_key_patch"></a>
> OriginsIdResponse edge_applications_edge_application_id_origins_origin_key_patch(edge_application_idorigin_key)

/edge_applications/:edge_application_id:/origins/:origin_id:

### Example

* Api Key Authentication (tokenAuth):
```python
import edgeapplications
from edgeapplications.apis.tags import edge_applications_origins_api
from edgeapplications.model.patch_origins_request import PatchOriginsRequest
from edgeapplications.model.origins_id_response import OriginsIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgeapplications.Configuration(
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
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edge_applications_origins_api.EdgeApplicationsOriginsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edge_application_id': 1,
        'origin_key': "origin_key_example",
    }
    header_params = {
    }
    try:
        # /edge_applications/:edge_application_id:/origins/:origin_id:
        api_response = api_instance.edge_applications_edge_application_id_origins_origin_key_patch(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsOriginsApi->edge_applications_edge_application_id_origins_origin_key_patch: %s\n" % e)

    # example passing only optional values
    path_params = {
        'edge_application_id': 1,
        'origin_key': "origin_key_example",
    }
    header_params = {
        'Accept': "application/json; version=3",
        'Content-Type': "application/json",
    }
    body = PatchOriginsRequest(
        name="name_example",
        origin_type="origin_type_example",
        addresses=[
            CreateOriginsRequestAddresses(
                address="address_example",
            )
        ],
        origin_protocol_policy="origin_protocol_policy_example",
        host_header="host_header_example",
        origin_path="origin_path_example",
        hmac_authentication=True,
        hmac_region_name="hmac_region_name_example",
        hmac_access_key="hmac_access_key_example",
        hmac_secret_key="hmac_secret_key_example",
    )
    try:
        # /edge_applications/:edge_application_id:/origins/:origin_id:
        api_response = api_instance.edge_applications_edge_application_id_origins_origin_key_patch(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsOriginsApi->edge_applications_edge_application_id_origins_origin_key_patch: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonVersion3, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json; version&#x3D;3' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**PatchOriginsRequest**](../../models/PatchOriginsRequest.md) |  | 


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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
edge_application_id | EdgeApplicationIdSchema | | 
origin_key | OriginKeySchema | | 

# EdgeApplicationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# OriginKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edge_applications_edge_application_id_origins_origin_key_patch.ApiResponseFor200) | Successful response
400 | [ApiResponseFor400](#edge_applications_edge_application_id_origins_origin_key_patch.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#edge_applications_edge_application_id_origins_origin_key_patch.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edge_applications_edge_application_id_origins_origin_key_patch.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#edge_applications_edge_application_id_origins_origin_key_patch.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#edge_applications_edge_application_id_origins_origin_key_patch.ApiResponseFor500) | Internal Server Error

#### edge_applications_edge_application_id_origins_origin_key_patch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**OriginsIdResponse**](../../models/OriginsIdResponse.md) |  | 


#### edge_applications_edge_application_id_origins_origin_key_patch.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_origins_origin_key_patch.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_origins_origin_key_patch.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_origins_origin_key_patch.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_origins_origin_key_patch.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edge_applications_edge_application_id_origins_origin_key_put**
<a id="edge_applications_edge_application_id_origins_origin_key_put"></a>
> OriginsIdResponse edge_applications_edge_application_id_origins_origin_key_put(edge_application_idorigin_key)

/edge_applications/{edge_application_id}/origins/{origin_id}

### Example

* Api Key Authentication (tokenAuth):
```python
import edgeapplications
from edgeapplications.apis.tags import edge_applications_origins_api
from edgeapplications.model.update_origins_request import UpdateOriginsRequest
from edgeapplications.model.origins_id_response import OriginsIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgeapplications.Configuration(
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
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edge_applications_origins_api.EdgeApplicationsOriginsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edge_application_id': 1,
        'origin_key': "origin_key_example",
    }
    header_params = {
    }
    try:
        # /edge_applications/{edge_application_id}/origins/{origin_id}
        api_response = api_instance.edge_applications_edge_application_id_origins_origin_key_put(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsOriginsApi->edge_applications_edge_application_id_origins_origin_key_put: %s\n" % e)

    # example passing only optional values
    path_params = {
        'edge_application_id': 1,
        'origin_key': "origin_key_example",
    }
    header_params = {
        'Accept': "application/json; version=3",
        'Content-Type': "application/json",
    }
    body = UpdateOriginsRequest(
        name="name_example",
        origin_type="origin_type_example",
        addresses=[
            CreateOriginsRequestAddresses(
                address="address_example",
            )
        ],
        origin_protocol_policy="origin_protocol_policy_example",
        host_header="host_header_example",
        origin_path="origin_path_example",
        hmac_authentication=True,
        hmac_region_name="hmac_region_name_example",
        hmac_access_key="hmac_access_key_example",
        hmac_secret_key="hmac_secret_key_example",
    )
    try:
        # /edge_applications/{edge_application_id}/origins/{origin_id}
        api_response = api_instance.edge_applications_edge_application_id_origins_origin_key_put(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsOriginsApi->edge_applications_edge_application_id_origins_origin_key_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonVersion3, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json; version&#x3D;3' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateOriginsRequest**](../../models/UpdateOriginsRequest.md) |  | 


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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
edge_application_id | EdgeApplicationIdSchema | | 
origin_key | OriginKeySchema | | 

# EdgeApplicationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# OriginKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edge_applications_edge_application_id_origins_origin_key_put.ApiResponseFor200) | Successful response
400 | [ApiResponseFor400](#edge_applications_edge_application_id_origins_origin_key_put.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#edge_applications_edge_application_id_origins_origin_key_put.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edge_applications_edge_application_id_origins_origin_key_put.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#edge_applications_edge_application_id_origins_origin_key_put.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#edge_applications_edge_application_id_origins_origin_key_put.ApiResponseFor500) | Internal Server Error

#### edge_applications_edge_application_id_origins_origin_key_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**OriginsIdResponse**](../../models/OriginsIdResponse.md) |  | 


#### edge_applications_edge_application_id_origins_origin_key_put.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_origins_origin_key_put.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_origins_origin_key_put.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_origins_origin_key_put.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_origins_origin_key_put.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edge_applications_edge_application_id_origins_post**
<a id="edge_applications_edge_application_id_origins_post"></a>
> OriginsIdResponse edge_applications_edge_application_id_origins_post(edge_application_id)

/edge_applications/{edge_application_id}/origins

### Example

* Api Key Authentication (tokenAuth):
```python
import edgeapplications
from edgeapplications.apis.tags import edge_applications_origins_api
from edgeapplications.model.create_origins_request import CreateOriginsRequest
from edgeapplications.model.origins_id_response import OriginsIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgeapplications.Configuration(
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
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edge_applications_origins_api.EdgeApplicationsOriginsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edge_application_id': 1,
    }
    header_params = {
    }
    try:
        # /edge_applications/{edge_application_id}/origins
        api_response = api_instance.edge_applications_edge_application_id_origins_post(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsOriginsApi->edge_applications_edge_application_id_origins_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'edge_application_id': 1,
    }
    header_params = {
        'Accept': "application/json; version=3",
        'Content-Type': "application/json",
    }
    body = CreateOriginsRequest(
        name="name_example",
        origin_type="origin_type_example",
        addresses=[
            CreateOriginsRequestAddresses(
                address="address_example",
            )
        ],
        origin_protocol_policy="origin_protocol_policy_example",
        host_header="host_header_example",
        origin_path="origin_path_example",
        hmac_authentication=True,
        hmac_region_name="hmac_region_name_example",
        hmac_access_key="hmac_access_key_example",
        hmac_secret_key="hmac_secret_key_example",
    )
    try:
        # /edge_applications/{edge_application_id}/origins
        api_response = api_instance.edge_applications_edge_application_id_origins_post(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsOriginsApi->edge_applications_edge_application_id_origins_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonVersion3, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json; version&#x3D;3' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateOriginsRequest**](../../models/CreateOriginsRequest.md) |  | 


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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
edge_application_id | EdgeApplicationIdSchema | | 

# EdgeApplicationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edge_applications_edge_application_id_origins_post.ApiResponseFor200) | Successful response
400 | [ApiResponseFor400](#edge_applications_edge_application_id_origins_post.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#edge_applications_edge_application_id_origins_post.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edge_applications_edge_application_id_origins_post.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#edge_applications_edge_application_id_origins_post.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#edge_applications_edge_application_id_origins_post.ApiResponseFor500) | Internal Server Error

#### edge_applications_edge_application_id_origins_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**OriginsIdResponse**](../../models/OriginsIdResponse.md) |  | 


#### edge_applications_edge_application_id_origins_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_origins_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_origins_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_origins_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_origins_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

