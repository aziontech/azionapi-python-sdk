# edgeapplications.EdgeApplicationsCacheSettingsApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edge_applications_edge_application_id_cache_settings_cache_settings_id_delete**](EdgeApplicationsCacheSettingsApi.md#edge_applications_edge_application_id_cache_settings_cache_settings_id_delete) | **DELETE** /edge_applications/{edge_application_id}/cache_settings/{cache_settings_id} | /edge_applications/:edge_application_id:/cache_settings/:cache_settings_id:
[**edge_applications_edge_application_id_cache_settings_cache_settings_id_get**](EdgeApplicationsCacheSettingsApi.md#edge_applications_edge_application_id_cache_settings_cache_settings_id_get) | **GET** /edge_applications/{edge_application_id}/cache_settings/{cache_settings_id} | /edge_applications/:edge_application_id:/cache_settings/:cache_settings_id:
[**edge_applications_edge_application_id_cache_settings_cache_settings_id_patch**](EdgeApplicationsCacheSettingsApi.md#edge_applications_edge_application_id_cache_settings_cache_settings_id_patch) | **PATCH** /edge_applications/{edge_application_id}/cache_settings/{cache_settings_id} | /edge_applications/:edge_application_id:/cache_settings/:cache_settings_id:
[**edge_applications_edge_application_id_cache_settings_cache_settings_id_put**](EdgeApplicationsCacheSettingsApi.md#edge_applications_edge_application_id_cache_settings_cache_settings_id_put) | **PUT** /edge_applications/{edge_application_id}/cache_settings/{cache_settings_id} | /edge_applications/:edge_application_id:/cache_settings/ca
[**edge_applications_edge_application_id_cache_settings_get**](EdgeApplicationsCacheSettingsApi.md#edge_applications_edge_application_id_cache_settings_get) | **GET** /edge_applications/{edge_application_id}/cache_settings | /edge_applications/{edge_application_id}/cache_settings
[**edge_applications_edge_application_id_cache_settings_post**](EdgeApplicationsCacheSettingsApi.md#edge_applications_edge_application_id_cache_settings_post) | **POST** /edge_applications/{edge_application_id}/cache_settings | /edge_applications/:edge_application_id:/cache_settings


# **edge_applications_edge_application_id_cache_settings_cache_settings_id_delete**
> edge_applications_edge_application_id_cache_settings_cache_settings_id_delete(edge_application_id, cache_settings_id, accept=accept, content_type=content_type)

/edge_applications/:edge_application_id:/cache_settings/:cache_settings_id:

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
    api_instance = edgeapplications.EdgeApplicationsCacheSettingsApi(api_client)
    edge_application_id = 56 # int | 
    cache_settings_id = 56 # int | 
    accept = 'application/json; version=3' # str |  (optional)
    content_type = 'application/json' # str | The type of coding used in the Body (application/json). <br>  Example: Content-Type: application/json (optional)

    try:
        # /edge_applications/:edge_application_id:/cache_settings/:cache_settings_id:
        api_instance.edge_applications_edge_application_id_cache_settings_cache_settings_id_delete(edge_application_id, cache_settings_id, accept=accept, content_type=content_type)
    except Exception as e:
        print("Exception when calling EdgeApplicationsCacheSettingsApi->edge_applications_edge_application_id_cache_settings_cache_settings_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **int**|  | 
 **cache_settings_id** | **int**|  | 
 **accept** | **str**|  | [optional] 
 **content_type** | **str**| The type of coding used in the Body (application/json). &lt;br&gt;  Example: Content-Type: application/json | [optional] 

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

# **edge_applications_edge_application_id_cache_settings_cache_settings_id_get**
> ApplicationCacheGetOneResponse edge_applications_edge_application_id_cache_settings_cache_settings_id_get(edge_application_id, cache_settings_id, accept=accept)

/edge_applications/:edge_application_id:/cache_settings/:cache_settings_id:

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgeapplications
from edgeapplications.models.application_cache_get_one_response import ApplicationCacheGetOneResponse
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
    api_instance = edgeapplications.EdgeApplicationsCacheSettingsApi(api_client)
    edge_application_id = 56 # int | 
    cache_settings_id = 56 # int | 
    accept = 'application/json; version=3' # str |  (optional)

    try:
        # /edge_applications/:edge_application_id:/cache_settings/:cache_settings_id:
        api_response = api_instance.edge_applications_edge_application_id_cache_settings_cache_settings_id_get(edge_application_id, cache_settings_id, accept=accept)
        print("The response of EdgeApplicationsCacheSettingsApi->edge_applications_edge_application_id_cache_settings_cache_settings_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsCacheSettingsApi->edge_applications_edge_application_id_cache_settings_cache_settings_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **int**|  | 
 **cache_settings_id** | **int**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**ApplicationCacheGetOneResponse**](ApplicationCacheGetOneResponse.md)

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

# **edge_applications_edge_application_id_cache_settings_cache_settings_id_patch**
> ApplicationCachePatchResponse edge_applications_edge_application_id_cache_settings_cache_settings_id_patch(edge_application_id, cache_settings_id, accept=accept, application_cache_patch_request=application_cache_patch_request)

/edge_applications/:edge_application_id:/cache_settings/:cache_settings_id:

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgeapplications
from edgeapplications.models.application_cache_patch_request import ApplicationCachePatchRequest
from edgeapplications.models.application_cache_patch_response import ApplicationCachePatchResponse
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
    api_instance = edgeapplications.EdgeApplicationsCacheSettingsApi(api_client)
    edge_application_id = 56 # int | 
    cache_settings_id = 56 # int | 
    accept = 'application/json; version=3' # str |  (optional)
    application_cache_patch_request = edgeapplications.ApplicationCachePatchRequest() # ApplicationCachePatchRequest |  (optional)

    try:
        # /edge_applications/:edge_application_id:/cache_settings/:cache_settings_id:
        api_response = api_instance.edge_applications_edge_application_id_cache_settings_cache_settings_id_patch(edge_application_id, cache_settings_id, accept=accept, application_cache_patch_request=application_cache_patch_request)
        print("The response of EdgeApplicationsCacheSettingsApi->edge_applications_edge_application_id_cache_settings_cache_settings_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsCacheSettingsApi->edge_applications_edge_application_id_cache_settings_cache_settings_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **int**|  | 
 **cache_settings_id** | **int**|  | 
 **accept** | **str**|  | [optional] 
 **application_cache_patch_request** | [**ApplicationCachePatchRequest**](ApplicationCachePatchRequest.md)|  | [optional] 

### Return type

[**ApplicationCachePatchResponse**](ApplicationCachePatchResponse.md)

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

# **edge_applications_edge_application_id_cache_settings_cache_settings_id_put**
> ApplicationCachePutResponse edge_applications_edge_application_id_cache_settings_cache_settings_id_put(edge_application_id, cache_settings_id, accept=accept, content_type=content_type, application_cache_put_request=application_cache_put_request)

/edge_applications/:edge_application_id:/cache_settings/ca

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgeapplications
from edgeapplications.models.application_cache_put_request import ApplicationCachePutRequest
from edgeapplications.models.application_cache_put_response import ApplicationCachePutResponse
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
    api_instance = edgeapplications.EdgeApplicationsCacheSettingsApi(api_client)
    edge_application_id = 56 # int | 
    cache_settings_id = 56 # int | 
    accept = 'application/json; version=3' # str |  (optional)
    content_type = 'application/json' # str | The type of coding used in the Body (application/json). <br>  Example: Content-Type: application/json (optional)
    application_cache_put_request = edgeapplications.ApplicationCachePutRequest() # ApplicationCachePutRequest |  (optional)

    try:
        # /edge_applications/:edge_application_id:/cache_settings/ca
        api_response = api_instance.edge_applications_edge_application_id_cache_settings_cache_settings_id_put(edge_application_id, cache_settings_id, accept=accept, content_type=content_type, application_cache_put_request=application_cache_put_request)
        print("The response of EdgeApplicationsCacheSettingsApi->edge_applications_edge_application_id_cache_settings_cache_settings_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsCacheSettingsApi->edge_applications_edge_application_id_cache_settings_cache_settings_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **int**|  | 
 **cache_settings_id** | **int**|  | 
 **accept** | **str**|  | [optional] 
 **content_type** | **str**| The type of coding used in the Body (application/json). &lt;br&gt;  Example: Content-Type: application/json | [optional] 
 **application_cache_put_request** | [**ApplicationCachePutRequest**](ApplicationCachePutRequest.md)|  | [optional] 

### Return type

[**ApplicationCachePutResponse**](ApplicationCachePutResponse.md)

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

# **edge_applications_edge_application_id_cache_settings_get**
> ApplicationCacheGetResponse edge_applications_edge_application_id_cache_settings_get(edge_application_id, page=page, page_size=page_size, filter=filter, order_by=order_by, sort=sort, accept=accept)

/edge_applications/{edge_application_id}/cache_settings

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgeapplications
from edgeapplications.models.application_cache_get_response import ApplicationCacheGetResponse
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
    api_instance = edgeapplications.EdgeApplicationsCacheSettingsApi(api_client)
    edge_application_id = 56 # int | 
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    filter = 'filter_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    sort = 'sort_example' # str |  (optional)
    accept = 'application/json; version=3' # str |  (optional)

    try:
        # /edge_applications/{edge_application_id}/cache_settings
        api_response = api_instance.edge_applications_edge_application_id_cache_settings_get(edge_application_id, page=page, page_size=page_size, filter=filter, order_by=order_by, sort=sort, accept=accept)
        print("The response of EdgeApplicationsCacheSettingsApi->edge_applications_edge_application_id_cache_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsCacheSettingsApi->edge_applications_edge_application_id_cache_settings_get: %s\n" % e)
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

[**ApplicationCacheGetResponse**](ApplicationCacheGetResponse.md)

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

# **edge_applications_edge_application_id_cache_settings_post**
> ApplicationCacheCreateResponse edge_applications_edge_application_id_cache_settings_post(edge_application_id, accept=accept, content_type=content_type, application_cache_create_request=application_cache_create_request)

/edge_applications/:edge_application_id:/cache_settings

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgeapplications
from edgeapplications.models.application_cache_create_request import ApplicationCacheCreateRequest
from edgeapplications.models.application_cache_create_response import ApplicationCacheCreateResponse
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
    api_instance = edgeapplications.EdgeApplicationsCacheSettingsApi(api_client)
    edge_application_id = 56 # int | 
    accept = 'application/json; version=3' # str |  (optional)
    content_type = 'application/json' # str | The type of coding used in the Body (application/json). <br>  Example: Content-Type: application/json (optional)
    application_cache_create_request = edgeapplications.ApplicationCacheCreateRequest() # ApplicationCacheCreateRequest |  (optional)

    try:
        # /edge_applications/:edge_application_id:/cache_settings
        api_response = api_instance.edge_applications_edge_application_id_cache_settings_post(edge_application_id, accept=accept, content_type=content_type, application_cache_create_request=application_cache_create_request)
        print("The response of EdgeApplicationsCacheSettingsApi->edge_applications_edge_application_id_cache_settings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsCacheSettingsApi->edge_applications_edge_application_id_cache_settings_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **int**|  | 
 **accept** | **str**|  | [optional] 
 **content_type** | **str**| The type of coding used in the Body (application/json). &lt;br&gt;  Example: Content-Type: application/json | [optional] 
 **application_cache_create_request** | [**ApplicationCacheCreateRequest**](ApplicationCacheCreateRequest.md)|  | [optional] 

### Return type

[**ApplicationCacheCreateResponse**](ApplicationCacheCreateResponse.md)

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

