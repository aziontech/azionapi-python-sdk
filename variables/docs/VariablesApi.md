# variables.VariablesApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_variables_create**](VariablesApi.md#api_variables_create) | **POST** /variables | /variables
[**api_variables_destroy**](VariablesApi.md#api_variables_destroy) | **DELETE** /variables/{uuid} | /variables/:uuid
[**api_variables_list**](VariablesApi.md#api_variables_list) | **GET** /variables | /variables
[**api_variables_retrieve**](VariablesApi.md#api_variables_retrieve) | **GET** /variables/{uuid} | /variables/:uuid
[**api_variables_update**](VariablesApi.md#api_variables_update) | **PUT** /variables/{uuid} | /variables/:uuid


# **api_variables_create**
> VariableGet api_variables_create(variable_create)

/variables

Create a new Variable. <br><ul><li>If the attribute \"secret\" is informed with value \"true\" in request payload the Variable value will be secret and no longer viewable after creation.</li><li>If the attribute \"secret\" is not informed the Variable value will be considered as not secret by default.</li></ul>

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import variables
from variables.models.variable_create import VariableCreate
from variables.models.variable_get import VariableGet
from variables.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = variables.Configuration(
    host = "https://api.azionapi.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with variables.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = variables.VariablesApi(api_client)
    variable_create = {"key":"MY_SIMPLE_VAR","value":"My not secret value"} # VariableCreate | 

    try:
        # /variables
        api_response = api_instance.api_variables_create(variable_create)
        print("The response of VariablesApi->api_variables_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariablesApi->api_variables_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_create** | [**VariableCreate**](VariableCreate.md)|  | 

### Return type

[**VariableGet**](VariableGet.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_variables_destroy**
> api_variables_destroy(uuid)

/variables/:uuid

Delete a Variable by it's UUID

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import variables
from variables.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = variables.Configuration(
    host = "https://api.azionapi.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with variables.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = variables.VariablesApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # /variables/:uuid
        api_instance.api_variables_destroy(uuid)
    except Exception as e:
        print("Exception when calling VariablesApi->api_variables_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_variables_list**
> List[Variable] api_variables_list()

/variables

List all user's Variables.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import variables
from variables.models.variable import Variable
from variables.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = variables.Configuration(
    host = "https://api.azionapi.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with variables.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = variables.VariablesApi(api_client)

    try:
        # /variables
        api_response = api_instance.api_variables_list()
        print("The response of VariablesApi->api_variables_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariablesApi->api_variables_list: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[Variable]**](Variable.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_variables_retrieve**
> Variable api_variables_retrieve(uuid)

/variables/:uuid

Retrieve all data for a Variable by it's UUID

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import variables
from variables.models.variable import Variable
from variables.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = variables.Configuration(
    host = "https://api.azionapi.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with variables.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = variables.VariablesApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # /variables/:uuid
        api_response = api_instance.api_variables_retrieve(uuid)
        print("The response of VariablesApi->api_variables_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariablesApi->api_variables_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**Variable**](Variable.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_variables_update**
> VariableGet api_variables_update(uuid, variable_create)

/variables/:uuid

Update variable attributes by it's UUID. Keep the Variable UUID but overwrite all editable attributes.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import variables
from variables.models.variable_create import VariableCreate
from variables.models.variable_get import VariableGet
from variables.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = variables.Configuration(
    host = "https://api.azionapi.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with variables.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = variables.VariablesApi(api_client)
    uuid = 'uuid_example' # str | 
    variable_create = {"key":"MY_NEW_SIMPLE_VAR_KEY","value":"My new not secret value"} # VariableCreate | 

    try:
        # /variables/:uuid
        api_response = api_instance.api_variables_update(uuid, variable_create)
        print("The response of VariablesApi->api_variables_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VariablesApi->api_variables_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **variable_create** | [**VariableCreate**](VariableCreate.md)|  | 

### Return type

[**VariableGet**](VariableGet.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

