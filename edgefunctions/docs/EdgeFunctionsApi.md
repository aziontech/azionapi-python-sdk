# edgefunctions.EdgeFunctionsApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edge_functions_get**](EdgeFunctionsApi.md#edge_functions_get) | **GET** /edge_functions | edge_functions
[**edge_functions_id_delete**](EdgeFunctionsApi.md#edge_functions_id_delete) | **DELETE** /edge_functions/{id} | edge_functions
[**edge_functions_id_get**](EdgeFunctionsApi.md#edge_functions_id_get) | **GET** /edge_functions/{id} | edge_functions
[**edge_functions_id_patch**](EdgeFunctionsApi.md#edge_functions_id_patch) | **PATCH** /edge_functions/{id} | edge_functions
[**edge_functions_id_put**](EdgeFunctionsApi.md#edge_functions_id_put) | **PUT** /edge_functions/{id} | edge_functions
[**edge_functions_post**](EdgeFunctionsApi.md#edge_functions_post) | **POST** /edge_functions | edge_functions


# **edge_functions_get**
> ListEdgeFunctionResponse edge_functions_get(page=page, page_size=page_size, sort=sort, order_by=order_by)

edge_functions

### Example

* Api Key Authentication (tokenAuth):

```python
import edgefunctions
from edgefunctions.models.list_edge_function_response import ListEdgeFunctionResponse
from edgefunctions.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefunctions.Configuration(
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
with edgefunctions.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgefunctions.EdgeFunctionsApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    sort = 'sort_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)

    try:
        # edge_functions
        api_response = api_instance.edge_functions_get(page=page, page_size=page_size, sort=sort, order_by=order_by)
        print("The response of EdgeFunctionsApi->edge_functions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeFunctionsApi->edge_functions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**ListEdgeFunctionResponse**](ListEdgeFunctionResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; version=3, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_functions_id_delete**
> edge_functions_id_delete(id)

edge_functions

### Example

* Api Key Authentication (tokenAuth):

```python
import edgefunctions
from edgefunctions.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefunctions.Configuration(
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
with edgefunctions.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgefunctions.EdgeFunctionsApi(api_client)
    id = 56 # int | 

    try:
        # edge_functions
        api_instance.edge_functions_id_delete(id)
    except Exception as e:
        print("Exception when calling EdgeFunctionsApi->edge_functions_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_functions_id_get**
> EdgeFunctionResponse edge_functions_id_get(id)

edge_functions

### Example

* Api Key Authentication (tokenAuth):

```python
import edgefunctions
from edgefunctions.models.edge_function_response import EdgeFunctionResponse
from edgefunctions.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefunctions.Configuration(
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
with edgefunctions.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgefunctions.EdgeFunctionsApi(api_client)
    id = 56 # int | 

    try:
        # edge_functions
        api_response = api_instance.edge_functions_id_get(id)
        print("The response of EdgeFunctionsApi->edge_functions_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeFunctionsApi->edge_functions_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**EdgeFunctionResponse**](EdgeFunctionResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not found |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_functions_id_patch**
> EdgeFunctionResponse edge_functions_id_patch(id, patch_edge_function_request)

edge_functions

### Example

* Api Key Authentication (tokenAuth):

```python
import edgefunctions
from edgefunctions.models.edge_function_response import EdgeFunctionResponse
from edgefunctions.models.patch_edge_function_request import PatchEdgeFunctionRequest
from edgefunctions.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefunctions.Configuration(
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
with edgefunctions.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgefunctions.EdgeFunctionsApi(api_client)
    id = 56 # int | 
    patch_edge_function_request = edgefunctions.PatchEdgeFunctionRequest() # PatchEdgeFunctionRequest | 

    try:
        # edge_functions
        api_response = api_instance.edge_functions_id_patch(id, patch_edge_function_request)
        print("The response of EdgeFunctionsApi->edge_functions_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeFunctionsApi->edge_functions_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **patch_edge_function_request** | [**PatchEdgeFunctionRequest**](PatchEdgeFunctionRequest.md)|  | 

### Return type

[**EdgeFunctionResponse**](EdgeFunctionResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json; version=3
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_functions_id_put**
> EdgeFunctionResponse edge_functions_id_put(id, put_edge_function_request)

edge_functions

### Example

* Api Key Authentication (tokenAuth):

```python
import edgefunctions
from edgefunctions.models.edge_function_response import EdgeFunctionResponse
from edgefunctions.models.put_edge_function_request import PutEdgeFunctionRequest
from edgefunctions.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefunctions.Configuration(
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
with edgefunctions.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgefunctions.EdgeFunctionsApi(api_client)
    id = 56 # int | 
    put_edge_function_request = edgefunctions.PutEdgeFunctionRequest() # PutEdgeFunctionRequest | 

    try:
        # edge_functions
        api_response = api_instance.edge_functions_id_put(id, put_edge_function_request)
        print("The response of EdgeFunctionsApi->edge_functions_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeFunctionsApi->edge_functions_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **put_edge_function_request** | [**PutEdgeFunctionRequest**](PutEdgeFunctionRequest.md)|  | 

### Return type

[**EdgeFunctionResponse**](EdgeFunctionResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json; version=3
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_functions_post**
> EdgeFunctionResponse edge_functions_post(create_edge_function_request)

edge_functions

### Example

* Api Key Authentication (tokenAuth):

```python
import edgefunctions
from edgefunctions.models.create_edge_function_request import CreateEdgeFunctionRequest
from edgefunctions.models.edge_function_response import EdgeFunctionResponse
from edgefunctions.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefunctions.Configuration(
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
with edgefunctions.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgefunctions.EdgeFunctionsApi(api_client)
    create_edge_function_request = edgefunctions.CreateEdgeFunctionRequest() # CreateEdgeFunctionRequest | 

    try:
        # edge_functions
        api_response = api_instance.edge_functions_post(create_edge_function_request)
        print("The response of EdgeFunctionsApi->edge_functions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeFunctionsApi->edge_functions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_edge_function_request** | [**CreateEdgeFunctionRequest**](CreateEdgeFunctionRequest.md)|  | 

### Return type

[**EdgeFunctionResponse**](EdgeFunctionResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Invalid request |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

