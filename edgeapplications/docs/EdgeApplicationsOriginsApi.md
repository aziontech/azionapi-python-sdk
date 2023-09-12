# edgeapplications.EdgeApplicationsOriginsApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edge_applications_edge_application_id_origins_get**](EdgeApplicationsOriginsApi.md#edge_applications_edge_application_id_origins_get) | **GET** /edge_applications/{edge_application_id}/origins | /edge_applications/{edge_application_id}/origins
[**edge_applications_edge_application_id_origins_origin_key_delete**](EdgeApplicationsOriginsApi.md#edge_applications_edge_application_id_origins_origin_key_delete) | **DELETE** /edge_applications/{edge_application_id}/origins/{origin_key} | /edge_applications/{edge_application_id}/origins/{origin_id}
[**edge_applications_edge_application_id_origins_origin_key_get**](EdgeApplicationsOriginsApi.md#edge_applications_edge_application_id_origins_origin_key_get) | **GET** /edge_applications/{edge_application_id}/origins/{origin_key} | /edge_applications/{edge_application_id}/origins/{origin_key}
[**edge_applications_edge_application_id_origins_origin_key_patch**](EdgeApplicationsOriginsApi.md#edge_applications_edge_application_id_origins_origin_key_patch) | **PATCH** /edge_applications/{edge_application_id}/origins/{origin_key} | /edge_applications/:edge_application_id:/origins/:origin_id:
[**edge_applications_edge_application_id_origins_origin_key_put**](EdgeApplicationsOriginsApi.md#edge_applications_edge_application_id_origins_origin_key_put) | **PUT** /edge_applications/{edge_application_id}/origins/{origin_key} | /edge_applications/{edge_application_id}/origins/{origin_id}
[**edge_applications_edge_application_id_origins_post**](EdgeApplicationsOriginsApi.md#edge_applications_edge_application_id_origins_post) | **POST** /edge_applications/{edge_application_id}/origins | /edge_applications/{edge_application_id}/origins


# **edge_applications_edge_application_id_origins_get**
> OriginsResponse edge_applications_edge_application_id_origins_get(edge_application_id, page=page, page_size=page_size, filter=filter, order_by=order_by, sort=sort, accept=accept)

/edge_applications/{edge_application_id}/origins

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgeapplications
from edgeapplications.models.origins_response import OriginsResponse
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
    api_instance = edgeapplications.EdgeApplicationsOriginsApi(api_client)
    edge_application_id = 56 # int | 
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    filter = 'filter_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    sort = 'sort_example' # str |  (optional)
    accept = 'application/json; version=3' # str |  (optional)

    try:
        # /edge_applications/{edge_application_id}/origins
        api_response = api_instance.edge_applications_edge_application_id_origins_get(edge_application_id, page=page, page_size=page_size, filter=filter, order_by=order_by, sort=sort, accept=accept)
        print("The response of EdgeApplicationsOriginsApi->edge_applications_edge_application_id_origins_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsOriginsApi->edge_applications_edge_application_id_origins_get: %s\n" % e)
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

[**OriginsResponse**](OriginsResponse.md)

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

# **edge_applications_edge_application_id_origins_origin_key_delete**
> edge_applications_edge_application_id_origins_origin_key_delete(edge_application_id, origin_key, accept=accept)

/edge_applications/{edge_application_id}/origins/{origin_id}

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
    api_instance = edgeapplications.EdgeApplicationsOriginsApi(api_client)
    edge_application_id = 56 # int | 
    origin_key = 'origin_key_example' # str | 
    accept = 'application/json; version=3' # str | The id of the Origin that you plan to delete. (optional)

    try:
        # /edge_applications/{edge_application_id}/origins/{origin_id}
        api_instance.edge_applications_edge_application_id_origins_origin_key_delete(edge_application_id, origin_key, accept=accept)
    except Exception as e:
        print("Exception when calling EdgeApplicationsOriginsApi->edge_applications_edge_application_id_origins_origin_key_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **int**|  | 
 **origin_key** | **str**|  | 
 **accept** | **str**| The id of the Origin that you plan to delete. | [optional] 

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

# **edge_applications_edge_application_id_origins_origin_key_get**
> OriginsIdResponse edge_applications_edge_application_id_origins_origin_key_get(edge_application_id, origin_key, accept=accept)

/edge_applications/{edge_application_id}/origins/{origin_key}

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgeapplications
from edgeapplications.models.origins_id_response import OriginsIdResponse
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
    api_instance = edgeapplications.EdgeApplicationsOriginsApi(api_client)
    edge_application_id = 56 # int | 
    origin_key = 'origin_key_example' # str | 
    accept = 'application/json; version=3' # str | The id of the Origin that you plan to query. (optional)

    try:
        # /edge_applications/{edge_application_id}/origins/{origin_key}
        api_response = api_instance.edge_applications_edge_application_id_origins_origin_key_get(edge_application_id, origin_key, accept=accept)
        print("The response of EdgeApplicationsOriginsApi->edge_applications_edge_application_id_origins_origin_key_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsOriginsApi->edge_applications_edge_application_id_origins_origin_key_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **int**|  | 
 **origin_key** | **str**|  | 
 **accept** | **str**| The id of the Origin that you plan to query. | [optional] 

### Return type

[**OriginsIdResponse**](OriginsIdResponse.md)

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

# **edge_applications_edge_application_id_origins_origin_key_patch**
> OriginsIdResponse edge_applications_edge_application_id_origins_origin_key_patch(edge_application_id, origin_key, accept=accept, content_type=content_type, patch_origins_request=patch_origins_request)

/edge_applications/:edge_application_id:/origins/:origin_id:

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgeapplications
from edgeapplications.models.origins_id_response import OriginsIdResponse
from edgeapplications.models.patch_origins_request import PatchOriginsRequest
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
    api_instance = edgeapplications.EdgeApplicationsOriginsApi(api_client)
    edge_application_id = 56 # int | 
    origin_key = 'origin_key_example' # str | 
    accept = 'application/json; version=3' # str |  (optional)
    content_type = 'application/json' # str | The type of coding used in the Body (application/json). <br>  Example: Content-Type: application/json (optional)
    patch_origins_request = edgeapplications.PatchOriginsRequest() # PatchOriginsRequest |  (optional)

    try:
        # /edge_applications/:edge_application_id:/origins/:origin_id:
        api_response = api_instance.edge_applications_edge_application_id_origins_origin_key_patch(edge_application_id, origin_key, accept=accept, content_type=content_type, patch_origins_request=patch_origins_request)
        print("The response of EdgeApplicationsOriginsApi->edge_applications_edge_application_id_origins_origin_key_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsOriginsApi->edge_applications_edge_application_id_origins_origin_key_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **int**|  | 
 **origin_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **content_type** | **str**| The type of coding used in the Body (application/json). &lt;br&gt;  Example: Content-Type: application/json | [optional] 
 **patch_origins_request** | [**PatchOriginsRequest**](PatchOriginsRequest.md)|  | [optional] 

### Return type

[**OriginsIdResponse**](OriginsIdResponse.md)

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

# **edge_applications_edge_application_id_origins_origin_key_put**
> OriginsIdResponse edge_applications_edge_application_id_origins_origin_key_put(edge_application_id, origin_key, accept=accept, content_type=content_type, update_origins_request=update_origins_request)

/edge_applications/{edge_application_id}/origins/{origin_id}

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgeapplications
from edgeapplications.models.origins_id_response import OriginsIdResponse
from edgeapplications.models.update_origins_request import UpdateOriginsRequest
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
    api_instance = edgeapplications.EdgeApplicationsOriginsApi(api_client)
    edge_application_id = 56 # int | 
    origin_key = 'origin_key_example' # str | 
    accept = 'application/json; version=3' # str |  (optional)
    content_type = 'application/json' # str | The type of coding used in the Body (application/json). <br>  Example: Content-Type: application/json (optional)
    update_origins_request = edgeapplications.UpdateOriginsRequest() # UpdateOriginsRequest |  (optional)

    try:
        # /edge_applications/{edge_application_id}/origins/{origin_id}
        api_response = api_instance.edge_applications_edge_application_id_origins_origin_key_put(edge_application_id, origin_key, accept=accept, content_type=content_type, update_origins_request=update_origins_request)
        print("The response of EdgeApplicationsOriginsApi->edge_applications_edge_application_id_origins_origin_key_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsOriginsApi->edge_applications_edge_application_id_origins_origin_key_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **int**|  | 
 **origin_key** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **content_type** | **str**| The type of coding used in the Body (application/json). &lt;br&gt;  Example: Content-Type: application/json | [optional] 
 **update_origins_request** | [**UpdateOriginsRequest**](UpdateOriginsRequest.md)|  | [optional] 

### Return type

[**OriginsIdResponse**](OriginsIdResponse.md)

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

# **edge_applications_edge_application_id_origins_post**
> OriginsIdResponse edge_applications_edge_application_id_origins_post(edge_application_id, accept=accept, content_type=content_type, create_origins_request=create_origins_request)

/edge_applications/{edge_application_id}/origins

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgeapplications
from edgeapplications.models.create_origins_request import CreateOriginsRequest
from edgeapplications.models.origins_id_response import OriginsIdResponse
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
    api_instance = edgeapplications.EdgeApplicationsOriginsApi(api_client)
    edge_application_id = 56 # int | 
    accept = 'application/json; version=3' # str |  (optional)
    content_type = 'application/json' # str | The type of coding used in the Body (application/json). <br>  Example: Content-Type: application/json (optional)
    create_origins_request = edgeapplications.CreateOriginsRequest() # CreateOriginsRequest |  (optional)

    try:
        # /edge_applications/{edge_application_id}/origins
        api_response = api_instance.edge_applications_edge_application_id_origins_post(edge_application_id, accept=accept, content_type=content_type, create_origins_request=create_origins_request)
        print("The response of EdgeApplicationsOriginsApi->edge_applications_edge_application_id_origins_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsOriginsApi->edge_applications_edge_application_id_origins_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **int**|  | 
 **accept** | **str**|  | [optional] 
 **content_type** | **str**| The type of coding used in the Body (application/json). &lt;br&gt;  Example: Content-Type: application/json | [optional] 
 **create_origins_request** | [**CreateOriginsRequest**](CreateOriginsRequest.md)|  | [optional] 

### Return type

[**OriginsIdResponse**](OriginsIdResponse.md)

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

