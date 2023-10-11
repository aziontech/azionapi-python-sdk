# edgefunctionsinstance_edgefirewall.DefaultApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_delete**](DefaultApi.md#edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_delete) | **DELETE** /edge_firewall/{edge_firewall_id}/functions_instances/{edge_function_instance_id} | Delete an Edge Functions Instance by uuid
[**edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_get**](DefaultApi.md#edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_get) | **GET** /edge_firewall/{edge_firewall_id}/functions_instances/{edge_function_instance_id} | Retrieve an Edge Functions Instance set by uuid
[**edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_patch**](DefaultApi.md#edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_patch) | **PATCH** /edge_firewall/{edge_firewall_id}/functions_instances/{edge_function_instance_id} | Update some Edge Functions Instance attributes
[**edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_put**](DefaultApi.md#edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_put) | **PUT** /edge_firewall/{edge_firewall_id}/functions_instances/{edge_function_instance_id} | Overwrite some Edge Functions Instance attributes
[**edge_firewall_edge_firewall_id_functions_instances_get**](DefaultApi.md#edge_firewall_edge_firewall_id_functions_instances_get) | **GET** /edge_firewall/{edge_firewall_id}/functions_instances | List all user Edge Functions Instances
[**edge_firewall_edge_firewall_id_functions_instances_post**](DefaultApi.md#edge_firewall_edge_firewall_id_functions_instances_post) | **POST** /edge_firewall/{edge_firewall_id}/functions_instances | Create an Edge Functions Instance


# **edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_delete**
> edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_delete(edge_firewall_id, edge_function_instance_id)

Delete an Edge Functions Instance by uuid

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgefunctionsinstance_edgefirewall
from edgefunctionsinstance_edgefirewall.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefunctionsinstance_edgefirewall.Configuration(
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
with edgefunctionsinstance_edgefirewall.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgefunctionsinstance_edgefirewall.DefaultApi(api_client)
    edge_firewall_id = 56 # int | 
    edge_function_instance_id = 56 # int | 

    try:
        # Delete an Edge Functions Instance by uuid
        api_instance.edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_delete(edge_firewall_id, edge_function_instance_id)
    except Exception as e:
        print("Exception when calling DefaultApi->edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_firewall_id** | **int**|  | 
 **edge_function_instance_id** | **int**|  | 

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
**204** | Successfully deleted |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_get**
> EdgeFunctionsInstanceResponse edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_get(edge_firewall_id, edge_function_instance_id)

Retrieve an Edge Functions Instance set by uuid

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgefunctionsinstance_edgefirewall
from edgefunctionsinstance_edgefirewall.models.edge_functions_instance_response import EdgeFunctionsInstanceResponse
from edgefunctionsinstance_edgefirewall.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefunctionsinstance_edgefirewall.Configuration(
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
with edgefunctionsinstance_edgefirewall.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgefunctionsinstance_edgefirewall.DefaultApi(api_client)
    edge_firewall_id = 56 # int | 
    edge_function_instance_id = 56 # int | 

    try:
        # Retrieve an Edge Functions Instance set by uuid
        api_response = api_instance.edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_get(edge_firewall_id, edge_function_instance_id)
        print("The response of DefaultApi->edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_firewall_id** | **int**|  | 
 **edge_function_instance_id** | **int**|  | 

### Return type

[**EdgeFunctionsInstanceResponse**](EdgeFunctionsInstanceResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Edge Functions Instance object |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_patch**
> EdgeFunctionsInstanceResponse edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_patch(edge_firewall_id, edge_function_instance_id, body)

Update some Edge Functions Instance attributes

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgefunctionsinstance_edgefirewall
from edgefunctionsinstance_edgefirewall.models.create_edge_functions_instances_request import CreateEdgeFunctionsInstancesRequest
from edgefunctionsinstance_edgefirewall.models.edge_functions_instance_response import EdgeFunctionsInstanceResponse
from edgefunctionsinstance_edgefirewall.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefunctionsinstance_edgefirewall.Configuration(
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
with edgefunctionsinstance_edgefirewall.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgefunctionsinstance_edgefirewall.DefaultApi(api_client)
    edge_firewall_id = 56 # int | 
    edge_function_instance_id = 56 # int | 
    body = edgefunctionsinstance_edgefirewall.CreateEdgeFunctionsInstancesRequest() # CreateEdgeFunctionsInstancesRequest | 

    try:
        # Update some Edge Functions Instance attributes
        api_response = api_instance.edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_patch(edge_firewall_id, edge_function_instance_id, body)
        print("The response of DefaultApi->edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_firewall_id** | **int**|  | 
 **edge_function_instance_id** | **int**|  | 
 **body** | **CreateEdgeFunctionsInstancesRequest**|  | 

### Return type

[**EdgeFunctionsInstanceResponse**](EdgeFunctionsInstanceResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_put**
> EdgeFunctionsInstanceResponse edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_put(edge_firewall_id, edge_function_instance_id, body)

Overwrite some Edge Functions Instance attributes

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgefunctionsinstance_edgefirewall
from edgefunctionsinstance_edgefirewall.models.create_edge_functions_instances_request import CreateEdgeFunctionsInstancesRequest
from edgefunctionsinstance_edgefirewall.models.edge_functions_instance_response import EdgeFunctionsInstanceResponse
from edgefunctionsinstance_edgefirewall.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefunctionsinstance_edgefirewall.Configuration(
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
with edgefunctionsinstance_edgefirewall.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgefunctionsinstance_edgefirewall.DefaultApi(api_client)
    edge_firewall_id = 56 # int | 
    edge_function_instance_id = 56 # int | 
    body = edgefunctionsinstance_edgefirewall.CreateEdgeFunctionsInstancesRequest() # CreateEdgeFunctionsInstancesRequest | 

    try:
        # Overwrite some Edge Functions Instance attributes
        api_response = api_instance.edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_put(edge_firewall_id, edge_function_instance_id, body)
        print("The response of DefaultApi->edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->edge_firewall_edge_firewall_id_functions_instances_edge_function_instance_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_firewall_id** | **int**|  | 
 **edge_function_instance_id** | **int**|  | 
 **body** | **CreateEdgeFunctionsInstancesRequest**|  | 

### Return type

[**EdgeFunctionsInstanceResponse**](EdgeFunctionsInstanceResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_firewall_edge_firewall_id_functions_instances_get**
> ListEdgeFunctionsInstancesResponse edge_firewall_edge_firewall_id_functions_instances_get(edge_firewall_id, page=page, page_size=page_size, sort=sort, order_by=order_by)

List all user Edge Functions Instances

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgefunctionsinstance_edgefirewall
from edgefunctionsinstance_edgefirewall.models.list_edge_functions_instances_response import ListEdgeFunctionsInstancesResponse
from edgefunctionsinstance_edgefirewall.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefunctionsinstance_edgefirewall.Configuration(
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
with edgefunctionsinstance_edgefirewall.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgefunctionsinstance_edgefirewall.DefaultApi(api_client)
    edge_firewall_id = 56 # int | 
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    sort = 'sort_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)

    try:
        # List all user Edge Functions Instances
        api_response = api_instance.edge_firewall_edge_firewall_id_functions_instances_get(edge_firewall_id, page=page, page_size=page_size, sort=sort, order_by=order_by)
        print("The response of DefaultApi->edge_firewall_edge_firewall_id_functions_instances_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->edge_firewall_edge_firewall_id_functions_instances_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_firewall_id** | **int**|  | 
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**ListEdgeFunctionsInstancesResponse**](ListEdgeFunctionsInstancesResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Edge Functions Instances |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_firewall_edge_firewall_id_functions_instances_post**
> EdgeFunctionsInstanceResponse edge_firewall_edge_firewall_id_functions_instances_post(edge_firewall_id, create_edge_functions_instances_request)

Create an Edge Functions Instance

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgefunctionsinstance_edgefirewall
from edgefunctionsinstance_edgefirewall.models.create_edge_functions_instances_request import CreateEdgeFunctionsInstancesRequest
from edgefunctionsinstance_edgefirewall.models.edge_functions_instance_response import EdgeFunctionsInstanceResponse
from edgefunctionsinstance_edgefirewall.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefunctionsinstance_edgefirewall.Configuration(
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
with edgefunctionsinstance_edgefirewall.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgefunctionsinstance_edgefirewall.DefaultApi(api_client)
    edge_firewall_id = 56 # int | 
    create_edge_functions_instances_request = edgefunctionsinstance_edgefirewall.CreateEdgeFunctionsInstancesRequest() # CreateEdgeFunctionsInstancesRequest | 

    try:
        # Create an Edge Functions Instance
        api_response = api_instance.edge_firewall_edge_firewall_id_functions_instances_post(edge_firewall_id, create_edge_functions_instances_request)
        print("The response of DefaultApi->edge_firewall_edge_firewall_id_functions_instances_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->edge_firewall_edge_firewall_id_functions_instances_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_firewall_id** | **int**|  | 
 **create_edge_functions_instances_request** | [**CreateEdgeFunctionsInstancesRequest**](CreateEdgeFunctionsInstancesRequest.md)|  | 

### Return type

[**EdgeFunctionsInstanceResponse**](EdgeFunctionsInstanceResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Edge Functions Instance created |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

