<a id="__pageTop"></a>
# credentials.apis.tags.default_api.DefaultApi

All URIs are relative to *http://localhost:3007*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_credential**](#create_credential) | **post** /credentials | Create credential
[**delete_credential**](#delete_credential) | **delete** /credentials/{credentialId} | Delete the Credential
[**find_all**](#find_all) | **get** /credentials | Return all credentials
[**load_credential**](#load_credential) | **get** /credentials/{credentialId} | Load the Credential
[**update_credential**](#update_credential) | **patch** /credentials/{credentialId} | Update the Credential

# **create_credential**
<a id="create_credential"></a>
> AuthToken create_credential(create_credential_request)

Create credential

### Example

* Api Key Authentication (bearerAuth):
```python
import credentials
from credentials.apis.tags import default_api
from credentials.model.auth_token import AuthToken
from credentials.model.create_credential_request import CreateCredentialRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3007
# See configuration.py for a list of all supported configuration parameters.
configuration = credentials.Configuration(
    host = "http://localhost:3007"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'
# Enter a context with an instance of the API client
with credentials.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    body = CreateCredentialRequest(
        description="description_example",
        name="name_example",
        status=True,
    )
    try:
        # Create credential
        api_response = api_instance.create_credential(
            body=body,
        )
        pprint(api_response)
    except credentials.ApiException as e:
        print("Exception when calling DefaultApi->create_credential: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonVersion3] | required |
content_type | str | optional, default is 'application/json; version&#x3D;3' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateCredentialRequest**](../../models/CreateCredentialRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_credential.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_credential.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#create_credential.ApiResponseFor403) | Forbidden
422 | [ApiResponseFor422](#create_credential.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#create_credential.ApiResponseFor500) | Internal Server Error

#### create_credential.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthToken**](../../models/AuthToken.md) |  | 


#### create_credential.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_credential.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_credential.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_credential.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_credential**
<a id="delete_credential"></a>
> delete_credential(credential_id)

Delete the Credential

### Example

* Api Key Authentication (bearerAuth):
```python
import credentials
from credentials.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3007
# See configuration.py for a list of all supported configuration parameters.
configuration = credentials.Configuration(
    host = "http://localhost:3007"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'
# Enter a context with an instance of the API client
with credentials.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'credentialId': 1,
    }
    try:
        # Delete the Credential
        api_response = api_instance.delete_credential(
            path_params=path_params,
        )
    except credentials.ApiException as e:
        print("Exception when calling DefaultApi->delete_credential: %s\n" % e)
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
credentialId | CredentialIdSchema | | 

# CredentialIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_credential.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_credential.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#delete_credential.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_credential.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#delete_credential.ApiResponseFor500) | Internal Server Error

#### delete_credential.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_credential.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_credential.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_credential.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_credential.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **find_all**
<a id="find_all"></a>
> ResponseWithTotal find_all()

Return all credentials

### Example

* Api Key Authentication (bearerAuth):
```python
import credentials
from credentials.apis.tags import default_api
from credentials.model.response_with_total import ResponseWithTotal
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3007
# See configuration.py for a list of all supported configuration parameters.
configuration = credentials.Configuration(
    host = "http://localhost:3007"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'
# Enter a context with an instance of the API client
with credentials.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only optional values
    query_params = {
        'filter': "filter_example",
        'page': 1,
        'page_size': 1,
        'sort': "sort_example",
        'order_by': "order_by_example",
    }
    try:
        # Return all credentials
        api_response = api_instance.find_all(
            query_params=query_params,
        )
        pprint(api_response)
    except credentials.ApiException as e:
        print("Exception when calling DefaultApi->find_all: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
filter | FilterSchema | | optional
page | PageSchema | | optional
page_size | PageSizeSchema | | optional
sort | SortSchema | | optional
order_by | OrderBySchema | | optional


# FilterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrderBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#find_all.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#find_all.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#find_all.ApiResponseFor500) | Internal Server Error

#### find_all.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**ResponseWithTotal**](../../models/ResponseWithTotal.md) |  | 


#### find_all.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### find_all.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **load_credential**
<a id="load_credential"></a>
> Response load_credential(credential_id)

Load the Credential

### Example

* Api Key Authentication (bearerAuth):
```python
import credentials
from credentials.apis.tags import default_api
from credentials.model.response import Response
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3007
# See configuration.py for a list of all supported configuration parameters.
configuration = credentials.Configuration(
    host = "http://localhost:3007"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'
# Enter a context with an instance of the API client
with credentials.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'credentialId': 1,
    }
    try:
        # Load the Credential
        api_response = api_instance.load_credential(
            path_params=path_params,
        )
        pprint(api_response)
    except credentials.ApiException as e:
        print("Exception when calling DefaultApi->load_credential: %s\n" % e)
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
credentialId | CredentialIdSchema | | 

# CredentialIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#load_credential.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#load_credential.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#load_credential.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#load_credential.ApiResponseFor500) | Internal Server Error

#### load_credential.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**Response**](../../models/Response.md) |  | 


#### load_credential.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### load_credential.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### load_credential.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_credential**
<a id="update_credential"></a>
> Response update_credential(credential_idupdate_credential_request)

Update the Credential

### Example

* Api Key Authentication (bearerAuth):
```python
import credentials
from credentials.apis.tags import default_api
from credentials.model.response import Response
from credentials.model.update_credential_request import UpdateCredentialRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3007
# See configuration.py for a list of all supported configuration parameters.
configuration = credentials.Configuration(
    host = "http://localhost:3007"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'
# Enter a context with an instance of the API client
with credentials.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'credentialId': 1,
    }
    body = UpdateCredentialRequest(
        description="description_example",
        name="name_example",
        status=True,
    )
    try:
        # Update the Credential
        api_response = api_instance.update_credential(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except credentials.ApiException as e:
        print("Exception when calling DefaultApi->update_credential: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonVersion3] | required |
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
[**UpdateCredentialRequest**](../../models/UpdateCredentialRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
credentialId | CredentialIdSchema | | 

# CredentialIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_credential.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#update_credential.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#update_credential.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_credential.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#update_credential.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#update_credential.ApiResponseFor500) | Internal Server Error

#### update_credential.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**Response**](../../models/Response.md) |  | 


#### update_credential.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_credential.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_credential.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_credential.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_credential.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

