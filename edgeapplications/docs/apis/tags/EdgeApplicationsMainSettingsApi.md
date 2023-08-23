<a id="__pageTop"></a>
# edgeapplications.apis.tags.edge_applications_main_settings_api.EdgeApplicationsMainSettingsApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edge_applications_get**](#edge_applications_get) | **get** /edge_applications | /edge_applications
[**edge_applications_id_delete**](#edge_applications_id_delete) | **delete** /edge_applications/{id} | /edge_applications/:id
[**edge_applications_id_get**](#edge_applications_id_get) | **get** /edge_applications/{id} | /edge_applications/:id
[**edge_applications_id_patch**](#edge_applications_id_patch) | **patch** /edge_applications/{id} | /edge_applications/:id
[**edge_applications_id_put**](#edge_applications_id_put) | **put** /edge_applications/{id} | /edge_applications/:id
[**edge_applications_post**](#edge_applications_post) | **post** /edge_applications | /edge_applications

# **edge_applications_get**
<a id="edge_applications_get"></a>
> GetApplicationsResponse edge_applications_get()

/edge_applications

### Example

* Api Key Authentication (tokenAuth):
```python
import edgeapplications
from edgeapplications.apis.tags import edge_applications_main_settings_api
from edgeapplications.model.get_applications_response import GetApplicationsResponse
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
    api_instance = edge_applications_main_settings_api.EdgeApplicationsMainSettingsApi(api_client)

    # example passing only optional values
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
        # /edge_applications
        api_response = api_instance.edge_applications_get(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsMainSettingsApi->edge_applications_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edge_applications_get.ApiResponseFor200) | Successful response
400 | [ApiResponseFor400](#edge_applications_get.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#edge_applications_get.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edge_applications_get.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#edge_applications_get.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#edge_applications_get.ApiResponseFor500) | Internal Server Error

#### edge_applications_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**GetApplicationsResponse**](../../models/GetApplicationsResponse.md) |  | 


#### edge_applications_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edge_applications_id_delete**
<a id="edge_applications_id_delete"></a>
> edge_applications_id_delete(id)

/edge_applications/:id

### Example

* Api Key Authentication (tokenAuth):
```python
import edgeapplications
from edgeapplications.apis.tags import edge_applications_main_settings_api
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
    api_instance = edge_applications_main_settings_api.EdgeApplicationsMainSettingsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    header_params = {
    }
    try:
        # /edge_applications/:id
        api_response = api_instance.edge_applications_id_delete(
            path_params=path_params,
            header_params=header_params,
        )
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsMainSettingsApi->edge_applications_id_delete: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    header_params = {
        'Accept': "application/json; version=3",
    }
    try:
        # /edge_applications/:id
        api_response = api_instance.edge_applications_id_delete(
            path_params=path_params,
            header_params=header_params,
        )
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsMainSettingsApi->edge_applications_id_delete: %s\n" % e)
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
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#edge_applications_id_delete.ApiResponseFor204) | No response
400 | [ApiResponseFor400](#edge_applications_id_delete.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#edge_applications_id_delete.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edge_applications_id_delete.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#edge_applications_id_delete.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#edge_applications_id_delete.ApiResponseFor500) | Internal Server Error

#### edge_applications_id_delete.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_id_delete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_id_delete.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_id_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_id_delete.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_id_delete.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edge_applications_id_get**
<a id="edge_applications_id_get"></a>
> GetApplicationResponse edge_applications_id_get(id)

/edge_applications/:id

### Example

* Api Key Authentication (tokenAuth):
```python
import edgeapplications
from edgeapplications.apis.tags import edge_applications_main_settings_api
from edgeapplications.model.get_application_response import GetApplicationResponse
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
    api_instance = edge_applications_main_settings_api.EdgeApplicationsMainSettingsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    header_params = {
    }
    try:
        # /edge_applications/:id
        api_response = api_instance.edge_applications_id_get(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsMainSettingsApi->edge_applications_id_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    header_params = {
        'Accept': "application/json; version=3",
    }
    try:
        # /edge_applications/:id
        api_response = api_instance.edge_applications_id_get(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsMainSettingsApi->edge_applications_id_get: %s\n" % e)
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
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edge_applications_id_get.ApiResponseFor200) | Successful response
400 | [ApiResponseFor400](#edge_applications_id_get.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#edge_applications_id_get.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edge_applications_id_get.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#edge_applications_id_get.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#edge_applications_id_get.ApiResponseFor500) | Internal Server Error

#### edge_applications_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**GetApplicationResponse**](../../models/GetApplicationResponse.md) |  | 


#### edge_applications_id_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_id_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_id_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_id_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_id_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edge_applications_id_patch**
<a id="edge_applications_id_patch"></a>
> ApplicationUpdateResponse edge_applications_id_patch(id)

/edge_applications/:id

### Example

* Api Key Authentication (tokenAuth):
```python
import edgeapplications
from edgeapplications.apis.tags import edge_applications_main_settings_api
from edgeapplications.model.application_update_request import ApplicationUpdateRequest
from edgeapplications.model.application_update_response import ApplicationUpdateResponse
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
    api_instance = edge_applications_main_settings_api.EdgeApplicationsMainSettingsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    header_params = {
    }
    try:
        # /edge_applications/:id
        api_response = api_instance.edge_applications_id_patch(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsMainSettingsApi->edge_applications_id_patch: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    header_params = {
        'Accept': "application/json; version=3",
        'Content-Type': "application/json",
    }
    body = ApplicationUpdateRequest(
        name="name_example",
        delivery_protocol="delivery_protocol_example",
        http_port=None,
        https_port=None,
        minimum_tls_version="minimum_tls_version_example",
        active=True,
        debug_rules=True,
        application_acceleration=True,
        caching=True,
        device_detection=True,
        edge_firewall=True,
        edge_functions=True,
        image_optimization=True,
        l2_caching=True,
        load_balancer=True,
        raw_logs=True,
        web_application_firewall=True,
        websocket=True,
    )
    try:
        # /edge_applications/:id
        api_response = api_instance.edge_applications_id_patch(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsMainSettingsApi->edge_applications_id_patch: %s\n" % e)
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
[**ApplicationUpdateRequest**](../../models/ApplicationUpdateRequest.md) |  | 


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
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edge_applications_id_patch.ApiResponseFor200) | Successful response
400 | [ApiResponseFor400](#edge_applications_id_patch.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#edge_applications_id_patch.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edge_applications_id_patch.ApiResponseFor404) | Not Found
405 | [ApiResponseFor405](#edge_applications_id_patch.ApiResponseFor405) | Method Not Allowed
422 | [ApiResponseFor422](#edge_applications_id_patch.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#edge_applications_id_patch.ApiResponseFor500) | Internal Server Error

#### edge_applications_id_patch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**ApplicationUpdateResponse**](../../models/ApplicationUpdateResponse.md) |  | 


#### edge_applications_id_patch.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_id_patch.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_id_patch.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_id_patch.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_id_patch.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_id_patch.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edge_applications_id_put**
<a id="edge_applications_id_put"></a>
> ApplicationPutResult edge_applications_id_put(id)

/edge_applications/:id

### Example

* Api Key Authentication (tokenAuth):
```python
import edgeapplications
from edgeapplications.apis.tags import edge_applications_main_settings_api
from edgeapplications.model.application_put_result import ApplicationPutResult
from edgeapplications.model.application_put_request import ApplicationPutRequest
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
    api_instance = edge_applications_main_settings_api.EdgeApplicationsMainSettingsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    header_params = {
    }
    try:
        # /edge_applications/:id
        api_response = api_instance.edge_applications_id_put(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsMainSettingsApi->edge_applications_id_put: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    header_params = {
        'Accept': "application/json; version=3",
        'Content-Type': "application/json",
    }
    body = ApplicationPutRequest(
        name="name_example",
        delivery_protocol="delivery_protocol_example",
        http_port=None,
        https_port=None,
        minimum_tls_version="minimum_tls_version_example",
        active=True,
        application_acceleration=True,
        caching=True,
        device_detection=True,
        edge_firewall=True,
        edge_functions=True,
        image_optimization=True,
        l2_caching=True,
        load_balancer=True,
        raw_logs=True,
        web_application_firewall=True,
        debug_rules=True,
        http3=True,
        websocket=True,
        supported_ciphers="supported_ciphers_example",
    )
    try:
        # /edge_applications/:id
        api_response = api_instance.edge_applications_id_put(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsMainSettingsApi->edge_applications_id_put: %s\n" % e)
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
[**ApplicationPutRequest**](../../models/ApplicationPutRequest.md) |  | 


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
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edge_applications_id_put.ApiResponseFor200) | Successful response
400 | [ApiResponseFor400](#edge_applications_id_put.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#edge_applications_id_put.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edge_applications_id_put.ApiResponseFor404) | Not Found
405 | [ApiResponseFor405](#edge_applications_id_put.ApiResponseFor405) | Method Not Allowed
422 | [ApiResponseFor422](#edge_applications_id_put.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#edge_applications_id_put.ApiResponseFor500) | Internal Server Error

#### edge_applications_id_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**ApplicationPutResult**](../../models/ApplicationPutResult.md) |  | 


#### edge_applications_id_put.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_id_put.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_id_put.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_id_put.ApiResponseFor405
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_id_put.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_id_put.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edge_applications_post**
<a id="edge_applications_post"></a>
> CreateApplicationResult edge_applications_post()

/edge_applications

### Example

* Api Key Authentication (tokenAuth):
```python
import edgeapplications
from edgeapplications.apis.tags import edge_applications_main_settings_api
from edgeapplications.model.create_application_result import CreateApplicationResult
from edgeapplications.model.create_application_request import CreateApplicationRequest
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
    api_instance = edge_applications_main_settings_api.EdgeApplicationsMainSettingsApi(api_client)

    # example passing only optional values
    header_params = {
        'Accept': "application/json; version=3",
        'Content-Type': "application/json",
    }
    body = CreateApplicationRequest(
        name="name_example",
        application_acceleration=True,
        delivery_protocol="delivery_protocol_example",
        origin_type="origin_type_example",
        address="address_example",
        origin_protocol_policy="origin_protocol_policy_example",
        host_header="host_header_example",
        browser_cache_settings="browser_cache_settings_example",
        cdn_cache_settings="cdn_cache_settings_example",
        browser_cache_settings_maximum_ttl=1,
        cdn_cache_settings_maximum_ttl=1,
        debug_rules=True,
        supported_ciphers="supported_ciphers_example",
        http_port=None,
        https_port=None,
        l2_caching=True,
        http3=True,
        websocket=True,
    )
    try:
        # /edge_applications
        api_response = api_instance.edge_applications_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsMainSettingsApi->edge_applications_post: %s\n" % e)
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
[**CreateApplicationRequest**](../../models/CreateApplicationRequest.md) |  | 


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
200 | [ApiResponseFor200](#edge_applications_post.ApiResponseFor200) | Successful response
201 | [ApiResponseFor201](#edge_applications_post.ApiResponseFor201) | Successful response
400 | [ApiResponseFor400](#edge_applications_post.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#edge_applications_post.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edge_applications_post.ApiResponseFor404) | Not Found
415 | [ApiResponseFor415](#edge_applications_post.ApiResponseFor415) | Unsupported Media Type
422 | [ApiResponseFor422](#edge_applications_post.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#edge_applications_post.ApiResponseFor500) | Internal Server Error

#### edge_applications_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateApplicationResult**](../../models/CreateApplicationResult.md) |  | 


#### edge_applications_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateApplicationResult**](../../models/CreateApplicationResult.md) |  | 


#### edge_applications_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_post.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

