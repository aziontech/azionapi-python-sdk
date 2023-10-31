# networklist.DefaultApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**network_lists_get**](DefaultApi.md#network_lists_get) | **GET** /network_lists | List all user Network Lists
[**network_lists_post**](DefaultApi.md#network_lists_post) | **POST** /network_lists | Create a Network Lists
[**network_lists_uuid_delete**](DefaultApi.md#network_lists_uuid_delete) | **DELETE** /network_lists/{uuid} | Delete a Network Lists set by uuid
[**network_lists_uuid_get**](DefaultApi.md#network_lists_uuid_get) | **GET** /network_lists/{uuid} | Retrieve a Network Lists set by uuid
[**network_lists_uuid_put**](DefaultApi.md#network_lists_uuid_put) | **PUT** /network_lists/{uuid} | Overwrite some Network Lists attributes


# **network_lists_get**
> ListNetworkListsResponse network_lists_get(page=page, page_size=page_size, sort=sort, order_by=order_by)

List all user Network Lists

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import networklist
from networklist.models.list_network_lists_response import ListNetworkListsResponse
from networklist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = networklist.Configuration(
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
with networklist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = networklist.DefaultApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    sort = 'sort_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)

    try:
        # List all user Network Lists
        api_response = api_instance.network_lists_get(page=page, page_size=page_size, sort=sort, order_by=order_by)
        print("The response of DefaultApi->network_lists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->network_lists_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**ListNetworkListsResponse**](ListNetworkListsResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Network Lists |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_lists_post**
> NetworkListsResponse network_lists_post(create_network_lists_request)

Create a Network Lists

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import networklist
from networklist.models.create_network_lists_request import CreateNetworkListsRequest
from networklist.models.network_lists_response import NetworkListsResponse
from networklist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = networklist.Configuration(
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
with networklist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = networklist.DefaultApi(api_client)
    create_network_lists_request = networklist.CreateNetworkListsRequest() # CreateNetworkListsRequest | 

    try:
        # Create a Network Lists
        api_response = api_instance.network_lists_post(create_network_lists_request)
        print("The response of DefaultApi->network_lists_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->network_lists_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_network_lists_request** | [**CreateNetworkListsRequest**](CreateNetworkListsRequest.md)|  | 

### Return type

[**NetworkListsResponse**](NetworkListsResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A Network Lists object |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_lists_uuid_delete**
> network_lists_uuid_delete(uuid, accept=accept)

Delete a Network Lists set by uuid

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import networklist
from networklist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = networklist.Configuration(
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
with networklist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = networklist.DefaultApi(api_client)
    uuid = 'uuid_example' # str | The id of the networkList to be deleted. 
    accept = 'application/json; version=3' # str |  (optional)

    try:
        # Delete a Network Lists set by uuid
        api_instance.network_lists_uuid_delete(uuid, accept=accept)
    except Exception as e:
        print("Exception when calling DefaultApi->network_lists_uuid_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The id of the networkList to be deleted.  | 
 **accept** | **str**|  | [optional] 

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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_lists_uuid_get**
> NetworkListUuidResponse network_lists_uuid_get(uuid)

Retrieve a Network Lists set by uuid

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import networklist
from networklist.models.network_list_uuid_response import NetworkListUuidResponse
from networklist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = networklist.Configuration(
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
with networklist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = networklist.DefaultApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Retrieve a Network Lists set by uuid
        api_response = api_instance.network_lists_uuid_get(uuid)
        print("The response of DefaultApi->network_lists_uuid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->network_lists_uuid_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**NetworkListUuidResponse**](NetworkListUuidResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Network Lists object |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_lists_uuid_put**
> NetworkListsResponse network_lists_uuid_put(uuid, create_network_lists_request)

Overwrite some Network Lists attributes

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import networklist
from networklist.models.create_network_lists_request import CreateNetworkListsRequest
from networklist.models.network_lists_response import NetworkListsResponse
from networklist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = networklist.Configuration(
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
with networklist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = networklist.DefaultApi(api_client)
    uuid = 'uuid_example' # str | 
    create_network_lists_request = networklist.CreateNetworkListsRequest() # CreateNetworkListsRequest | 

    try:
        # Overwrite some Network Lists attributes
        api_response = api_instance.network_lists_uuid_put(uuid, create_network_lists_request)
        print("The response of DefaultApi->network_lists_uuid_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->network_lists_uuid_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **create_network_lists_request** | [**CreateNetworkListsRequest**](CreateNetworkListsRequest.md)|  | 

### Return type

[**NetworkListsResponse**](NetworkListsResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

