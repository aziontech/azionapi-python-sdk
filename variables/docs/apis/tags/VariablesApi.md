<a id="__pageTop"></a>
# variables.apis.tags.variables_api.VariablesApi

All URIs are relative to *https://stage-api.azion.net/variables*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_variables_create**](#api_variables_create) | **post** /variables | /variables
[**api_variables_destroy**](#api_variables_destroy) | **delete** /variables/{uuid} | /variables/:uuid
[**api_variables_list**](#api_variables_list) | **get** /variables | /variables
[**api_variables_retrieve**](#api_variables_retrieve) | **get** /variables/{uuid} | /variables/:uuid
[**api_variables_update**](#api_variables_update) | **put** /variables/{uuid} | /variables/:uuid

# **api_variables_create**
<a id="api_variables_create"></a>
> VariableGet api_variables_create(variable_create)

/variables

Create a new Variable. <br><ul><li>If the attribute \"secret\" is informed with value \"true\" in request payload the Variable value will be secret and no longer viewable after creation.</li><li>If the attribute \"secret\" is not informed the Variable value will be considered as not secret by default.</li></ul>

### Example

* Api Key Authentication (tokenAuth):
```python
import variables
from variables.apis.tags import variables_api
from variables.model.variable_create import VariableCreate
from variables.model.variable_get import VariableGet
from pprint import pprint
# Defining the host is optional and defaults to https://stage-api.azion.net/variables
# See configuration.py for a list of all supported configuration parameters.
configuration = variables.Configuration(
    host = "https://stage-api.azion.net/variables"
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
with variables.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = variables_api.VariablesApi(api_client)

    # example passing only required values which don't have defaults set
    body = VariableCreate(
        key="key_example",
        value="value_example",
        secret=True,
    )
    try:
        # /variables
        api_response = api_instance.api_variables_create(
            body=body,
        )
        pprint(api_response)
    except variables.ApiException as e:
        print("Exception when calling VariablesApi->api_variables_create: %s\n" % e)
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
[**VariableCreate**](../../models/VariableCreate.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#api_variables_create.ApiResponseFor201) | 
400 | [ApiResponseFor400](#api_variables_create.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#api_variables_create.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#api_variables_create.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#api_variables_create.ApiResponseFor500) | Internal Server Error

#### api_variables_create.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VariableGet**](../../models/VariableGet.md) |  | 


#### api_variables_create.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### api_variables_create.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### api_variables_create.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### api_variables_create.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_variables_destroy**
<a id="api_variables_destroy"></a>
> api_variables_destroy(uuid)

/variables/:uuid

Delete a Variable by it's UUID

### Example

* Api Key Authentication (tokenAuth):
```python
import variables
from variables.apis.tags import variables_api
from pprint import pprint
# Defining the host is optional and defaults to https://stage-api.azion.net/variables
# See configuration.py for a list of all supported configuration parameters.
configuration = variables.Configuration(
    host = "https://stage-api.azion.net/variables"
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
with variables.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = variables_api.VariablesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'uuid': "bf325375-e030-4fcc-aa00-917317c57477",
    }
    try:
        # /variables/:uuid
        api_response = api_instance.api_variables_destroy(
            path_params=path_params,
        )
    except variables.ApiException as e:
        print("Exception when calling VariablesApi->api_variables_destroy: %s\n" % e)
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
204 | [ApiResponseFor204](#api_variables_destroy.ApiResponseFor204) | No response body
400 | [ApiResponseFor400](#api_variables_destroy.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#api_variables_destroy.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#api_variables_destroy.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#api_variables_destroy.ApiResponseFor500) | Internal Server Error

#### api_variables_destroy.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### api_variables_destroy.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### api_variables_destroy.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### api_variables_destroy.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### api_variables_destroy.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_variables_list**
<a id="api_variables_list"></a>
> [Variable] api_variables_list()

/variables

List all user's Variables.

### Example

* Api Key Authentication (tokenAuth):
```python
import variables
from variables.apis.tags import variables_api
from variables.model.variable import Variable
from pprint import pprint
# Defining the host is optional and defaults to https://stage-api.azion.net/variables
# See configuration.py for a list of all supported configuration parameters.
configuration = variables.Configuration(
    host = "https://stage-api.azion.net/variables"
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
with variables.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = variables_api.VariablesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # /variables
        api_response = api_instance.api_variables_list()
        pprint(api_response)
    except variables.ApiException as e:
        print("Exception when calling VariablesApi->api_variables_list: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#api_variables_list.ApiResponseFor200) | 
404 | [ApiResponseFor404](#api_variables_list.ApiResponseFor404) | Not Found

#### api_variables_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Variable**]({{complexTypePrefix}}Variable.md) | [**Variable**]({{complexTypePrefix}}Variable.md) | [**Variable**]({{complexTypePrefix}}Variable.md) |  | 

#### api_variables_list.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_variables_retrieve**
<a id="api_variables_retrieve"></a>
> Variable api_variables_retrieve(uuid)

/variables/:uuid

Retrieve all data for a Variable by it's UUID

### Example

* Api Key Authentication (tokenAuth):
```python
import variables
from variables.apis.tags import variables_api
from variables.model.variable import Variable
from pprint import pprint
# Defining the host is optional and defaults to https://stage-api.azion.net/variables
# See configuration.py for a list of all supported configuration parameters.
configuration = variables.Configuration(
    host = "https://stage-api.azion.net/variables"
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
with variables.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = variables_api.VariablesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'uuid': "bf325375-e030-4fcc-aa00-917317c57477",
    }
    try:
        # /variables/:uuid
        api_response = api_instance.api_variables_retrieve(
            path_params=path_params,
        )
        pprint(api_response)
    except variables.ApiException as e:
        print("Exception when calling VariablesApi->api_variables_retrieve: %s\n" % e)
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
200 | [ApiResponseFor200](#api_variables_retrieve.ApiResponseFor200) | 
400 | [ApiResponseFor400](#api_variables_retrieve.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#api_variables_retrieve.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#api_variables_retrieve.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#api_variables_retrieve.ApiResponseFor500) | Internal Server Error

#### api_variables_retrieve.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Variable**](../../models/Variable.md) |  | 


#### api_variables_retrieve.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### api_variables_retrieve.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### api_variables_retrieve.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### api_variables_retrieve.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **api_variables_update**
<a id="api_variables_update"></a>
> VariableGet api_variables_update(uuidvariable_create)

/variables/:uuid

Update variable attributes by it's UUID. Keep the Variable UUID but overwrite all editable attributes.

### Example

* Api Key Authentication (tokenAuth):
```python
import variables
from variables.apis.tags import variables_api
from variables.model.variable_create import VariableCreate
from variables.model.variable_get import VariableGet
from pprint import pprint
# Defining the host is optional and defaults to https://stage-api.azion.net/variables
# See configuration.py for a list of all supported configuration parameters.
configuration = variables.Configuration(
    host = "https://stage-api.azion.net/variables"
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
with variables.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = variables_api.VariablesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'uuid': "bf325375-e030-4fcc-aa00-917317c57477",
    }
    body = VariableCreate(
        key="key_example",
        value="value_example",
        secret=True,
    )
    try:
        # /variables/:uuid
        api_response = api_instance.api_variables_update(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except variables.ApiException as e:
        print("Exception when calling VariablesApi->api_variables_update: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationXWwwFormUrlencoded, SchemaForRequestBodyMultipartFormData] | required |
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
[**VariableCreate**](../../models/VariableCreate.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**VariableCreate**](../../models/VariableCreate.md) |  | 


# SchemaForRequestBodyMultipartFormData
Type | Description  | Notes
------------- | ------------- | -------------
[**VariableCreate**](../../models/VariableCreate.md) |  | 


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
200 | [ApiResponseFor200](#api_variables_update.ApiResponseFor200) | 
400 | [ApiResponseFor400](#api_variables_update.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#api_variables_update.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#api_variables_update.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#api_variables_update.ApiResponseFor500) | Internal Server Error

#### api_variables_update.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VariableGet**](../../models/VariableGet.md) |  | 


#### api_variables_update.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### api_variables_update.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### api_variables_update.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### api_variables_update.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

