<a id="__pageTop"></a>
# personal_tokens.apis.tags.personal_token_api.PersonalTokenApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_personal_token**](#create_personal_token) | **post** /iam/personal_tokens | Create a new personal token
[**delete_personal_token**](#delete_personal_token) | **delete** /iam/personal_tokens/{personalTokenId} | Delete a personal token by id
[**get_personal_token**](#get_personal_token) | **get** /iam/personal_tokens/{personalTokenId} | Get a personal token info
[**list_personal_token**](#list_personal_token) | **get** /iam/personal_tokens | List all existing personal token

# **create_personal_token**
<a id="create_personal_token"></a>
> CreatePersonalTokenResponse create_personal_token(create_personal_token_request)

Create a new personal token

Create a new personal token

### Example

* Api Key Authentication (tokenAuth):
```python
import personal_tokens
from personal_tokens.apis.tags import personal_token_api
from personal_tokens.model.create_personal_token_request import CreatePersonalTokenRequest
from personal_tokens.model.create_personal_token_response import CreatePersonalTokenResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = personal_tokens.Configuration(
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
with personal_tokens.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = personal_token_api.PersonalTokenApi(api_client)

    # example passing only required values which don't have defaults set
    body = CreatePersonalTokenRequest(
        name="name_example",
        expires_at="1970-01-01T00:00:00.00Z",
        description="description_example",
    )
    try:
        # Create a new personal token
        api_response = api_instance.create_personal_token(
            body=body,
        )
        pprint(api_response)
    except personal_tokens.ApiException as e:
        print("Exception when calling PersonalTokenApi->create_personal_token: %s\n" % e)
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
[**CreatePersonalTokenRequest**](../../models/CreatePersonalTokenRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_personal_token.ApiResponseFor201) | Successful operation
400 | [ApiResponseFor400](#create_personal_token.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#create_personal_token.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#create_personal_token.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_personal_token.ApiResponseFor404) | Not Found
429 | [ApiResponseFor429](#create_personal_token.ApiResponseFor429) | Rate Limit
500 | [ApiResponseFor500](#create_personal_token.ApiResponseFor500) | Internal Server Error

#### create_personal_token.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreatePersonalTokenResponse**](../../models/CreatePersonalTokenResponse.md) |  | 


#### create_personal_token.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_personal_token.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_personal_token.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_personal_token.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_personal_token.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_personal_token.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_personal_token**
<a id="delete_personal_token"></a>
> delete_personal_token(personal_token_id)

Delete a personal token by id

Delete a personal token

### Example

* Api Key Authentication (tokenAuth):
```python
import personal_tokens
from personal_tokens.apis.tags import personal_token_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = personal_tokens.Configuration(
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
with personal_tokens.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = personal_token_api.PersonalTokenApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'personalTokenId': "personalTokenId_example",
    }
    try:
        # Delete a personal token by id
        api_response = api_instance.delete_personal_token(
            path_params=path_params,
        )
    except personal_tokens.ApiException as e:
        print("Exception when calling PersonalTokenApi->delete_personal_token: %s\n" % e)
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
personalTokenId | PersonalTokenIdSchema | | 

# PersonalTokenIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_personal_token.ApiResponseFor204) | Successful operation
400 | [ApiResponseFor400](#delete_personal_token.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#delete_personal_token.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#delete_personal_token.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#delete_personal_token.ApiResponseFor404) | Not Found
429 | [ApiResponseFor429](#delete_personal_token.ApiResponseFor429) | Rate Limit
500 | [ApiResponseFor500](#delete_personal_token.ApiResponseFor500) | Internal Server Error

#### delete_personal_token.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_personal_token.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_personal_token.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_personal_token.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_personal_token.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_personal_token.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_personal_token.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_personal_token**
<a id="get_personal_token"></a>
> PersonalTokenResponseGet get_personal_token(personal_token_id)

Get a personal token info

Get a personal token info

### Example

* Api Key Authentication (tokenAuth):
```python
import personal_tokens
from personal_tokens.apis.tags import personal_token_api
from personal_tokens.model.personal_token_response_get import PersonalTokenResponseGet
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = personal_tokens.Configuration(
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
with personal_tokens.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = personal_token_api.PersonalTokenApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'personalTokenId': "personalTokenId_example",
    }
    try:
        # Get a personal token info
        api_response = api_instance.get_personal_token(
            path_params=path_params,
        )
        pprint(api_response)
    except personal_tokens.ApiException as e:
        print("Exception when calling PersonalTokenApi->get_personal_token: %s\n" % e)
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
personalTokenId | PersonalTokenIdSchema | | 

# PersonalTokenIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_personal_token.ApiResponseFor200) | Successful operation
400 | [ApiResponseFor400](#get_personal_token.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_personal_token.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_personal_token.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_personal_token.ApiResponseFor404) | Not Found
429 | [ApiResponseFor429](#get_personal_token.ApiResponseFor429) | Rate Limit
500 | [ApiResponseFor500](#get_personal_token.ApiResponseFor500) | Internal Server Error

#### get_personal_token.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PersonalTokenResponseGet**](../../models/PersonalTokenResponseGet.md) |  | 


#### get_personal_token.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_personal_token.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_personal_token.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_personal_token.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_personal_token.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_personal_token.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_personal_token**
<a id="list_personal_token"></a>
> PersonalTokenResponseWithResults list_personal_token()

List all existing personal token

List all existing personal token

### Example

* Api Key Authentication (tokenAuth):
```python
import personal_tokens
from personal_tokens.apis.tags import personal_token_api
from personal_tokens.model.personal_token_response_with_results import PersonalTokenResponseWithResults
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = personal_tokens.Configuration(
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
with personal_tokens.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = personal_token_api.PersonalTokenApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all existing personal token
        api_response = api_instance.list_personal_token()
        pprint(api_response)
    except personal_tokens.ApiException as e:
        print("Exception when calling PersonalTokenApi->list_personal_token: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_personal_token.ApiResponseFor200) | Successful operation
400 | [ApiResponseFor400](#list_personal_token.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#list_personal_token.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#list_personal_token.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_personal_token.ApiResponseFor404) | Not Found
429 | [ApiResponseFor429](#list_personal_token.ApiResponseFor429) | Rate Limit
500 | [ApiResponseFor500](#list_personal_token.ApiResponseFor500) | Internal Server Error

#### list_personal_token.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PersonalTokenResponseWithResults**](../../models/PersonalTokenResponseWithResults.md) |  | 


#### list_personal_token.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_personal_token.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_personal_token.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_personal_token.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_personal_token.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_personal_token.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

