<a id="__pageTop"></a>
# edgeapplications.apis.tags.edge_applications_edge_functions_instances_api.EdgeApplicationsEdgeFunctionsInstancesApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edge_applications_edge_application_id_functions_instances_functions_instances_id_delete**](#edge_applications_edge_application_id_functions_instances_functions_instances_id_delete) | **delete** /edge_applications/{edge_application_id}/functions_instances/{functions_instances_id} | /edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:
[**edge_applications_edge_application_id_functions_instances_functions_instances_id_get**](#edge_applications_edge_application_id_functions_instances_functions_instances_id_get) | **get** /edge_applications/{edge_application_id}/functions_instances/{functions_instances_id} | /edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:
[**edge_applications_edge_application_id_functions_instances_functions_instances_id_patch**](#edge_applications_edge_application_id_functions_instances_functions_instances_id_patch) | **patch** /edge_applications/{edge_application_id}/functions_instances/{functions_instances_id} | /edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:
[**edge_applications_edge_application_id_functions_instances_functions_instances_id_put**](#edge_applications_edge_application_id_functions_instances_functions_instances_id_put) | **put** /edge_applications/{edge_application_id}/functions_instances/{functions_instances_id} | /edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:
[**edge_applications_edge_application_id_functions_instances_get**](#edge_applications_edge_application_id_functions_instances_get) | **get** /edge_applications/{edge_application_id}/functions_instances | /edge_applications/:edge_application_id:/functions_instances
[**edge_applications_edge_application_id_functions_instances_post**](#edge_applications_edge_application_id_functions_instances_post) | **post** /edge_applications/{edge_application_id}/functions_instances | edge_application/:edge_application_id:/functions_instances

# **edge_applications_edge_application_id_functions_instances_functions_instances_id_delete**
<a id="edge_applications_edge_application_id_functions_instances_functions_instances_id_delete"></a>
> edge_applications_edge_application_id_functions_instances_functions_instances_id_delete(edge_application_idfunctions_instances_id)

/edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:

### Example

* Api Key Authentication (JWT):
```python
import edgeapplications
from edgeapplications.apis.tags import edge_applications_edge_functions_instances_api
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

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'
# Enter a context with an instance of the API client
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edge_applications_edge_functions_instances_api.EdgeApplicationsEdgeFunctionsInstancesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edge_application_id': "edge_application_id_example",
        'functions_instances_id': "functions_instances_id_example",
    }
    header_params = {
    }
    try:
        # /edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:
        api_response = api_instance.edge_applications_edge_application_id_functions_instances_functions_instances_id_delete(
            path_params=path_params,
            header_params=header_params,
        )
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsEdgeFunctionsInstancesApi->edge_applications_edge_application_id_functions_instances_functions_instances_id_delete: %s\n" % e)

    # example passing only optional values
    path_params = {
        'edge_application_id': "edge_application_id_example",
        'functions_instances_id': "functions_instances_id_example",
    }
    header_params = {
        'Accept': "application/json; version=3",
        'Content-Type': "application/json",
    }
    try:
        # /edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:
        api_response = api_instance.edge_applications_edge_application_id_functions_instances_functions_instances_id_delete(
            path_params=path_params,
            header_params=header_params,
        )
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsEdgeFunctionsInstancesApi->edge_applications_edge_application_id_functions_instances_functions_instances_id_delete: %s\n" % e)
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
functions_instances_id | FunctionsInstancesIdSchema | | 

# EdgeApplicationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FunctionsInstancesIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#edge_applications_edge_application_id_functions_instances_functions_instances_id_delete.ApiResponseFor204) | No response
400 | [ApiResponseFor400](#edge_applications_edge_application_id_functions_instances_functions_instances_id_delete.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#edge_applications_edge_application_id_functions_instances_functions_instances_id_delete.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edge_applications_edge_application_id_functions_instances_functions_instances_id_delete.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#edge_applications_edge_application_id_functions_instances_functions_instances_id_delete.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#edge_applications_edge_application_id_functions_instances_functions_instances_id_delete.ApiResponseFor500) | Internal Server Error

#### edge_applications_edge_application_id_functions_instances_functions_instances_id_delete.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_functions_instances_functions_instances_id_delete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_functions_instances_functions_instances_id_delete.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_functions_instances_functions_instances_id_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_functions_instances_functions_instances_id_delete.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_functions_instances_functions_instances_id_delete.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[JWT](../../../README.md#JWT)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edge_applications_edge_application_id_functions_instances_functions_instances_id_get**
<a id="edge_applications_edge_application_id_functions_instances_functions_instances_id_get"></a>
> ApplicationInstancesGetOneResponse edge_applications_edge_application_id_functions_instances_functions_instances_id_get(edge_application_idfunctions_instances_id)

/edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:

### Example

* Api Key Authentication (JWT):
```python
import edgeapplications
from edgeapplications.apis.tags import edge_applications_edge_functions_instances_api
from edgeapplications.model.application_instances_get_one_response import ApplicationInstancesGetOneResponse
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

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'
# Enter a context with an instance of the API client
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edge_applications_edge_functions_instances_api.EdgeApplicationsEdgeFunctionsInstancesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edge_application_id': 1,
        'functions_instances_id': 1,
    }
    header_params = {
    }
    try:
        # /edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:
        api_response = api_instance.edge_applications_edge_application_id_functions_instances_functions_instances_id_get(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsEdgeFunctionsInstancesApi->edge_applications_edge_application_id_functions_instances_functions_instances_id_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'edge_application_id': 1,
        'functions_instances_id': 1,
    }
    header_params = {
        'Accept': "application/json; version=3",
    }
    try:
        # /edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:
        api_response = api_instance.edge_applications_edge_application_id_functions_instances_functions_instances_id_get(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsEdgeFunctionsInstancesApi->edge_applications_edge_application_id_functions_instances_functions_instances_id_get: %s\n" % e)
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
functions_instances_id | FunctionsInstancesIdSchema | | 

# EdgeApplicationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# FunctionsInstancesIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edge_applications_edge_application_id_functions_instances_functions_instances_id_get.ApiResponseFor200) | Successful response
400 | [ApiResponseFor400](#edge_applications_edge_application_id_functions_instances_functions_instances_id_get.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#edge_applications_edge_application_id_functions_instances_functions_instances_id_get.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edge_applications_edge_application_id_functions_instances_functions_instances_id_get.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#edge_applications_edge_application_id_functions_instances_functions_instances_id_get.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#edge_applications_edge_application_id_functions_instances_functions_instances_id_get.ApiResponseFor500) | Internal Server Error

#### edge_applications_edge_application_id_functions_instances_functions_instances_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**ApplicationInstancesGetOneResponse**](../../models/ApplicationInstancesGetOneResponse.md) |  | 


#### edge_applications_edge_application_id_functions_instances_functions_instances_id_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_functions_instances_functions_instances_id_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_functions_instances_functions_instances_id_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_functions_instances_functions_instances_id_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_functions_instances_functions_instances_id_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[JWT](../../../README.md#JWT)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edge_applications_edge_application_id_functions_instances_functions_instances_id_patch**
<a id="edge_applications_edge_application_id_functions_instances_functions_instances_id_patch"></a>
> ApplicationInstanceResults edge_applications_edge_application_id_functions_instances_functions_instances_id_patch(edge_application_idfunctions_instances_id)

/edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:

### Example

* Api Key Authentication (JWT):
```python
import edgeapplications
from edgeapplications.apis.tags import edge_applications_edge_functions_instances_api
from edgeapplications.model.application_instance_results import ApplicationInstanceResults
from edgeapplications.model.application_update_instance_request import ApplicationUpdateInstanceRequest
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

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'
# Enter a context with an instance of the API client
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edge_applications_edge_functions_instances_api.EdgeApplicationsEdgeFunctionsInstancesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edge_application_id': "edge_application_id_example",
        'functions_instances_id': "functions_instances_id_example",
    }
    header_params = {
    }
    try:
        # /edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:
        api_response = api_instance.edge_applications_edge_application_id_functions_instances_functions_instances_id_patch(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsEdgeFunctionsInstancesApi->edge_applications_edge_application_id_functions_instances_functions_instances_id_patch: %s\n" % e)

    # example passing only optional values
    path_params = {
        'edge_application_id': "edge_application_id_example",
        'functions_instances_id': "functions_instances_id_example",
    }
    header_params = {
        'Accept': "application/json; version=3",
        'Content-Type': "application/json",
    }
    body = ApplicationUpdateInstanceRequest(None)
    try:
        # /edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:
        api_response = api_instance.edge_applications_edge_application_id_functions_instances_functions_instances_id_patch(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsEdgeFunctionsInstancesApi->edge_applications_edge_application_id_functions_instances_functions_instances_id_patch: %s\n" % e)
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
[**ApplicationUpdateInstanceRequest**](../../models/ApplicationUpdateInstanceRequest.md) |  | 


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
functions_instances_id | FunctionsInstancesIdSchema | | 

# EdgeApplicationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FunctionsInstancesIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edge_applications_edge_application_id_functions_instances_functions_instances_id_patch.ApiResponseFor200) | Successful response
400 | [ApiResponseFor400](#edge_applications_edge_application_id_functions_instances_functions_instances_id_patch.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#edge_applications_edge_application_id_functions_instances_functions_instances_id_patch.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edge_applications_edge_application_id_functions_instances_functions_instances_id_patch.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#edge_applications_edge_application_id_functions_instances_functions_instances_id_patch.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#edge_applications_edge_application_id_functions_instances_functions_instances_id_patch.ApiResponseFor500) | Internal Server Error

#### edge_applications_edge_application_id_functions_instances_functions_instances_id_patch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**ApplicationInstanceResults**](../../models/ApplicationInstanceResults.md) |  | 


#### edge_applications_edge_application_id_functions_instances_functions_instances_id_patch.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_functions_instances_functions_instances_id_patch.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_functions_instances_functions_instances_id_patch.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_functions_instances_functions_instances_id_patch.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_functions_instances_functions_instances_id_patch.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[JWT](../../../README.md#JWT)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edge_applications_edge_application_id_functions_instances_functions_instances_id_put**
<a id="edge_applications_edge_application_id_functions_instances_functions_instances_id_put"></a>
> ApplicationInstanceResults edge_applications_edge_application_id_functions_instances_functions_instances_id_put(edge_application_idfunctions_instances_id)

/edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:

### Example

* Api Key Authentication (JWT):
```python
import edgeapplications
from edgeapplications.apis.tags import edge_applications_edge_functions_instances_api
from edgeapplications.model.application_instance_results import ApplicationInstanceResults
from edgeapplications.model.application_put_instance_request import ApplicationPutInstanceRequest
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

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'
# Enter a context with an instance of the API client
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edge_applications_edge_functions_instances_api.EdgeApplicationsEdgeFunctionsInstancesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edge_application_id': "edge_application_id_example",
        'functions_instances_id': "functions_instances_id_example",
    }
    header_params = {
    }
    try:
        # /edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:
        api_response = api_instance.edge_applications_edge_application_id_functions_instances_functions_instances_id_put(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsEdgeFunctionsInstancesApi->edge_applications_edge_application_id_functions_instances_functions_instances_id_put: %s\n" % e)

    # example passing only optional values
    path_params = {
        'edge_application_id': "edge_application_id_example",
        'functions_instances_id': "functions_instances_id_example",
    }
    header_params = {
        'Accept': "application/json; version=3",
        'Content-Type': "application/json",
    }
    body = ApplicationPutInstanceRequest(None)
    try:
        # /edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:
        api_response = api_instance.edge_applications_edge_application_id_functions_instances_functions_instances_id_put(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsEdgeFunctionsInstancesApi->edge_applications_edge_application_id_functions_instances_functions_instances_id_put: %s\n" % e)
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
[**ApplicationPutInstanceRequest**](../../models/ApplicationPutInstanceRequest.md) |  | 


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
functions_instances_id | FunctionsInstancesIdSchema | | 

# EdgeApplicationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FunctionsInstancesIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edge_applications_edge_application_id_functions_instances_functions_instances_id_put.ApiResponseFor200) | Successful response
400 | [ApiResponseFor400](#edge_applications_edge_application_id_functions_instances_functions_instances_id_put.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#edge_applications_edge_application_id_functions_instances_functions_instances_id_put.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edge_applications_edge_application_id_functions_instances_functions_instances_id_put.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#edge_applications_edge_application_id_functions_instances_functions_instances_id_put.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#edge_applications_edge_application_id_functions_instances_functions_instances_id_put.ApiResponseFor500) | Internal Server Error

#### edge_applications_edge_application_id_functions_instances_functions_instances_id_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**ApplicationInstanceResults**](../../models/ApplicationInstanceResults.md) |  | 


#### edge_applications_edge_application_id_functions_instances_functions_instances_id_put.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_functions_instances_functions_instances_id_put.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_functions_instances_functions_instances_id_put.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_functions_instances_functions_instances_id_put.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_functions_instances_functions_instances_id_put.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[JWT](../../../README.md#JWT)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edge_applications_edge_application_id_functions_instances_get**
<a id="edge_applications_edge_application_id_functions_instances_get"></a>
> ApplicationInstancesGetResponse edge_applications_edge_application_id_functions_instances_get(edge_application_id)

/edge_applications/:edge_application_id:/functions_instances

### Example

* Api Key Authentication (JWT):
```python
import edgeapplications
from edgeapplications.apis.tags import edge_applications_edge_functions_instances_api
from edgeapplications.model.application_instances_get_response import ApplicationInstancesGetResponse
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

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'
# Enter a context with an instance of the API client
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edge_applications_edge_functions_instances_api.EdgeApplicationsEdgeFunctionsInstancesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edge_application_id': 1,
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # /edge_applications/:edge_application_id:/functions_instances
        api_response = api_instance.edge_applications_edge_application_id_functions_instances_get(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsEdgeFunctionsInstancesApi->edge_applications_edge_application_id_functions_instances_get: %s\n" % e)

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
        # /edge_applications/:edge_application_id:/functions_instances
        api_response = api_instance.edge_applications_edge_application_id_functions_instances_get(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsEdgeFunctionsInstancesApi->edge_applications_edge_application_id_functions_instances_get: %s\n" % e)
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
200 | [ApiResponseFor200](#edge_applications_edge_application_id_functions_instances_get.ApiResponseFor200) | Successful response
400 | [ApiResponseFor400](#edge_applications_edge_application_id_functions_instances_get.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#edge_applications_edge_application_id_functions_instances_get.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edge_applications_edge_application_id_functions_instances_get.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#edge_applications_edge_application_id_functions_instances_get.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#edge_applications_edge_application_id_functions_instances_get.ApiResponseFor500) | Internal Server Error

#### edge_applications_edge_application_id_functions_instances_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**ApplicationInstancesGetResponse**](../../models/ApplicationInstancesGetResponse.md) |  | 


#### edge_applications_edge_application_id_functions_instances_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_functions_instances_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_functions_instances_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_functions_instances_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_functions_instances_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[JWT](../../../README.md#JWT)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edge_applications_edge_application_id_functions_instances_post**
<a id="edge_applications_edge_application_id_functions_instances_post"></a>
> ApplicationInstanceResults edge_applications_edge_application_id_functions_instances_post(edge_application_id)

edge_application/:edge_application_id:/functions_instances

### Example

* Api Key Authentication (JWT):
```python
import edgeapplications
from edgeapplications.apis.tags import edge_applications_edge_functions_instances_api
from edgeapplications.model.application_instance_results import ApplicationInstanceResults
from edgeapplications.model.application_create_instance_request import ApplicationCreateInstanceRequest
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

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'
# Enter a context with an instance of the API client
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edge_applications_edge_functions_instances_api.EdgeApplicationsEdgeFunctionsInstancesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edge_application_id': 1,
    }
    header_params = {
    }
    try:
        # edge_application/:edge_application_id:/functions_instances
        api_response = api_instance.edge_applications_edge_application_id_functions_instances_post(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsEdgeFunctionsInstancesApi->edge_applications_edge_application_id_functions_instances_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'edge_application_id': 1,
    }
    header_params = {
        'Accept': "application/json; version=3",
        'Content-Type': "application/json",
    }
    body = ApplicationCreateInstanceRequest(None)
    try:
        # edge_application/:edge_application_id:/functions_instances
        api_response = api_instance.edge_applications_edge_application_id_functions_instances_post(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsEdgeFunctionsInstancesApi->edge_applications_edge_application_id_functions_instances_post: %s\n" % e)
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
[**ApplicationCreateInstanceRequest**](../../models/ApplicationCreateInstanceRequest.md) |  | 


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
200 | [ApiResponseFor200](#edge_applications_edge_application_id_functions_instances_post.ApiResponseFor200) | Successful response
400 | [ApiResponseFor400](#edge_applications_edge_application_id_functions_instances_post.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#edge_applications_edge_application_id_functions_instances_post.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edge_applications_edge_application_id_functions_instances_post.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#edge_applications_edge_application_id_functions_instances_post.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#edge_applications_edge_application_id_functions_instances_post.ApiResponseFor500) | Internal Server Error

#### edge_applications_edge_application_id_functions_instances_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**ApplicationInstanceResults**](../../models/ApplicationInstanceResults.md) |  | 


#### edge_applications_edge_application_id_functions_instances_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_functions_instances_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_functions_instances_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_functions_instances_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_functions_instances_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[JWT](../../../README.md#JWT)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

