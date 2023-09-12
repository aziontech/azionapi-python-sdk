# edgeapplications.EdgeApplicationsDeviceGroupsApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edge_applications_edge_application_id_device_groups_device_group_id_delete**](EdgeApplicationsDeviceGroupsApi.md#edge_applications_edge_application_id_device_groups_device_group_id_delete) | **DELETE** /edge_applications/{edge_application_id}/device_groups/{device_group_id} | /edge_applications/{edge_application_id}/device_groups/{device_group_id}
[**edge_applications_edge_application_id_device_groups_device_group_id_get**](EdgeApplicationsDeviceGroupsApi.md#edge_applications_edge_application_id_device_groups_device_group_id_get) | **GET** /edge_applications/{edge_application_id}/device_groups/{device_group_id} | /edge_applications/{edge_application_id}/device_groups/{device_group_id}
[**edge_applications_edge_application_id_device_groups_device_group_id_patch**](EdgeApplicationsDeviceGroupsApi.md#edge_applications_edge_application_id_device_groups_device_group_id_patch) | **PATCH** /edge_applications/{edge_application_id}/device_groups/{device_group_id} | /edge_applications/{edge_application_id}/device_groups/{device_group_id}
[**edge_applications_edge_application_id_device_groups_device_group_id_put**](EdgeApplicationsDeviceGroupsApi.md#edge_applications_edge_application_id_device_groups_device_group_id_put) | **PUT** /edge_applications/{edge_application_id}/device_groups/{device_group_id} | /edge_applications/{edge_application_id}/device_groups/{device_group_id}
[**edge_applications_edge_application_id_device_groups_get**](EdgeApplicationsDeviceGroupsApi.md#edge_applications_edge_application_id_device_groups_get) | **GET** /edge_applications/{edge_application_id}/device_groups | /edge_applications/{edge_application_id}/device_groups
[**edge_applications_edge_application_id_device_groups_post**](EdgeApplicationsDeviceGroupsApi.md#edge_applications_edge_application_id_device_groups_post) | **POST** /edge_applications/{edge_application_id}/device_groups | /edge_applications/{edge_application_id}/device_groups


# **edge_applications_edge_application_id_device_groups_device_group_id_delete**
> edge_applications_edge_application_id_device_groups_device_group_id_delete(edge_application_id, device_group_id, accept=accept)

/edge_applications/{edge_application_id}/device_groups/{device_group_id}

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgeapplications
from edgeapplications.rest import ApiException
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
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgeapplications.EdgeApplicationsDeviceGroupsApi(api_client)
    edge_application_id = 56 # int | 
    device_group_id = 56 # int | 
    accept = 'application/json; version=3' # str | The id of the Device Groups that you plan to delete. (optional)

    try:
        # /edge_applications/{edge_application_id}/device_groups/{device_group_id}
        api_instance.edge_applications_edge_application_id_device_groups_device_group_id_delete(edge_application_id, device_group_id, accept=accept)
    except Exception as e:
        print("Exception when calling EdgeApplicationsDeviceGroupsApi->edge_applications_edge_application_id_device_groups_device_group_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **int**|  | 
 **device_group_id** | **int**|  | 
 **accept** | **str**| The id of the Device Groups that you plan to delete. | [optional] 

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
**204** | No response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_applications_edge_application_id_device_groups_device_group_id_get**
> DeviceGroupsIdResponse edge_applications_edge_application_id_device_groups_device_group_id_get(edge_application_id, device_group_id, accept=accept)

/edge_applications/{edge_application_id}/device_groups/{device_group_id}

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgeapplications
from edgeapplications.models.device_groups_id_response import DeviceGroupsIdResponse
from edgeapplications.rest import ApiException
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
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgeapplications.EdgeApplicationsDeviceGroupsApi(api_client)
    edge_application_id = 56 # int | 
    device_group_id = 56 # int | 
    accept = 'application/json; version=3' # str | The id of the Device Groups that you plan to query. (optional)

    try:
        # /edge_applications/{edge_application_id}/device_groups/{device_group_id}
        api_response = api_instance.edge_applications_edge_application_id_device_groups_device_group_id_get(edge_application_id, device_group_id, accept=accept)
        print("The response of EdgeApplicationsDeviceGroupsApi->edge_applications_edge_application_id_device_groups_device_group_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsDeviceGroupsApi->edge_applications_edge_application_id_device_groups_device_group_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **int**|  | 
 **device_group_id** | **int**|  | 
 **accept** | **str**| The id of the Device Groups that you plan to query. | [optional] 

### Return type

[**DeviceGroupsIdResponse**](DeviceGroupsIdResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_applications_edge_application_id_device_groups_device_group_id_patch**
> DeviceGroupsIdResponse edge_applications_edge_application_id_device_groups_device_group_id_patch(edge_application_id, device_group_id, accept=accept, content_type=content_type, patch_device_groups_request=patch_device_groups_request)

/edge_applications/{edge_application_id}/device_groups/{device_group_id}

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgeapplications
from edgeapplications.models.device_groups_id_response import DeviceGroupsIdResponse
from edgeapplications.models.patch_device_groups_request import PatchDeviceGroupsRequest
from edgeapplications.rest import ApiException
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
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgeapplications.EdgeApplicationsDeviceGroupsApi(api_client)
    edge_application_id = 56 # int | 
    device_group_id = 56 # int | 
    accept = 'application/json; version=3' # str |  (optional)
    content_type = 'application/json' # str | The type of coding used in the Body (application/json). <br>  Example: Content-Type: application/json (optional)
    patch_device_groups_request = edgeapplications.PatchDeviceGroupsRequest() # PatchDeviceGroupsRequest |  (optional)

    try:
        # /edge_applications/{edge_application_id}/device_groups/{device_group_id}
        api_response = api_instance.edge_applications_edge_application_id_device_groups_device_group_id_patch(edge_application_id, device_group_id, accept=accept, content_type=content_type, patch_device_groups_request=patch_device_groups_request)
        print("The response of EdgeApplicationsDeviceGroupsApi->edge_applications_edge_application_id_device_groups_device_group_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsDeviceGroupsApi->edge_applications_edge_application_id_device_groups_device_group_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **int**|  | 
 **device_group_id** | **int**|  | 
 **accept** | **str**|  | [optional] 
 **content_type** | **str**| The type of coding used in the Body (application/json). &lt;br&gt;  Example: Content-Type: application/json | [optional] 
 **patch_device_groups_request** | [**PatchDeviceGroupsRequest**](PatchDeviceGroupsRequest.md)|  | [optional] 

### Return type

[**DeviceGroupsIdResponse**](DeviceGroupsIdResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json; version=3
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_applications_edge_application_id_device_groups_device_group_id_put**
> DeviceGroupsIdResponse edge_applications_edge_application_id_device_groups_device_group_id_put(edge_application_id, device_group_id, accept=accept, content_type=content_type, update_device_groups_request=update_device_groups_request)

/edge_applications/{edge_application_id}/device_groups/{device_group_id}

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgeapplications
from edgeapplications.models.device_groups_id_response import DeviceGroupsIdResponse
from edgeapplications.models.update_device_groups_request import UpdateDeviceGroupsRequest
from edgeapplications.rest import ApiException
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
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgeapplications.EdgeApplicationsDeviceGroupsApi(api_client)
    edge_application_id = 56 # int | 
    device_group_id = 56 # int | 
    accept = 'application/json; version=3' # str |  (optional)
    content_type = 'application/json' # str | The type of coding used in the Body (application/json). <br>  Example: Content-Type: application/json (optional)
    update_device_groups_request = edgeapplications.UpdateDeviceGroupsRequest() # UpdateDeviceGroupsRequest |  (optional)

    try:
        # /edge_applications/{edge_application_id}/device_groups/{device_group_id}
        api_response = api_instance.edge_applications_edge_application_id_device_groups_device_group_id_put(edge_application_id, device_group_id, accept=accept, content_type=content_type, update_device_groups_request=update_device_groups_request)
        print("The response of EdgeApplicationsDeviceGroupsApi->edge_applications_edge_application_id_device_groups_device_group_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsDeviceGroupsApi->edge_applications_edge_application_id_device_groups_device_group_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **int**|  | 
 **device_group_id** | **int**|  | 
 **accept** | **str**|  | [optional] 
 **content_type** | **str**| The type of coding used in the Body (application/json). &lt;br&gt;  Example: Content-Type: application/json | [optional] 
 **update_device_groups_request** | [**UpdateDeviceGroupsRequest**](UpdateDeviceGroupsRequest.md)|  | [optional] 

### Return type

[**DeviceGroupsIdResponse**](DeviceGroupsIdResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json; version=3
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_applications_edge_application_id_device_groups_get**
> DeviceGroupsResponse edge_applications_edge_application_id_device_groups_get(edge_application_id, page=page, page_size=page_size, filter=filter, order_by=order_by, sort=sort, accept=accept)

/edge_applications/{edge_application_id}/device_groups

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgeapplications
from edgeapplications.models.device_groups_response import DeviceGroupsResponse
from edgeapplications.rest import ApiException
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
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgeapplications.EdgeApplicationsDeviceGroupsApi(api_client)
    edge_application_id = 56 # int | 
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    filter = 'filter_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    sort = 'sort_example' # str |  (optional)
    accept = 'application/json; version=3' # str |  (optional)

    try:
        # /edge_applications/{edge_application_id}/device_groups
        api_response = api_instance.edge_applications_edge_application_id_device_groups_get(edge_application_id, page=page, page_size=page_size, filter=filter, order_by=order_by, sort=sort, accept=accept)
        print("The response of EdgeApplicationsDeviceGroupsApi->edge_applications_edge_application_id_device_groups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsDeviceGroupsApi->edge_applications_edge_application_id_device_groups_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **int**|  | 
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**DeviceGroupsResponse**](DeviceGroupsResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_applications_edge_application_id_device_groups_post**
> DeviceGroupsIdResponse edge_applications_edge_application_id_device_groups_post(edge_application_id, accept=accept, content_type=content_type, create_device_groups_request=create_device_groups_request)

/edge_applications/{edge_application_id}/device_groups

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgeapplications
from edgeapplications.models.create_device_groups_request import CreateDeviceGroupsRequest
from edgeapplications.models.device_groups_id_response import DeviceGroupsIdResponse
from edgeapplications.rest import ApiException
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
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgeapplications.EdgeApplicationsDeviceGroupsApi(api_client)
    edge_application_id = 56 # int | 
    accept = 'application/json; version=3' # str |  (optional)
    content_type = 'application/json' # str | The type of coding used in the Body (application/json). <br>  Example: Content-Type: application/json (optional)
    create_device_groups_request = edgeapplications.CreateDeviceGroupsRequest() # CreateDeviceGroupsRequest |  (optional)

    try:
        # /edge_applications/{edge_application_id}/device_groups
        api_response = api_instance.edge_applications_edge_application_id_device_groups_post(edge_application_id, accept=accept, content_type=content_type, create_device_groups_request=create_device_groups_request)
        print("The response of EdgeApplicationsDeviceGroupsApi->edge_applications_edge_application_id_device_groups_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsDeviceGroupsApi->edge_applications_edge_application_id_device_groups_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **int**|  | 
 **accept** | **str**|  | [optional] 
 **content_type** | **str**| The type of coding used in the Body (application/json). &lt;br&gt;  Example: Content-Type: application/json | [optional] 
 **create_device_groups_request** | [**CreateDeviceGroupsRequest**](CreateDeviceGroupsRequest.md)|  | [optional] 

### Return type

[**DeviceGroupsIdResponse**](DeviceGroupsIdResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json; version=3
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

