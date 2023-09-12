# edgeapplications.EdgeApplicationsEdgeFunctionsInstancesApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edge_applications_edge_application_id_functions_instances_functions_instances_id_delete**](EdgeApplicationsEdgeFunctionsInstancesApi.md#edge_applications_edge_application_id_functions_instances_functions_instances_id_delete) | **DELETE** /edge_applications/{edge_application_id}/functions_instances/{functions_instances_id} | /edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:
[**edge_applications_edge_application_id_functions_instances_functions_instances_id_get**](EdgeApplicationsEdgeFunctionsInstancesApi.md#edge_applications_edge_application_id_functions_instances_functions_instances_id_get) | **GET** /edge_applications/{edge_application_id}/functions_instances/{functions_instances_id} | /edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:
[**edge_applications_edge_application_id_functions_instances_functions_instances_id_patch**](EdgeApplicationsEdgeFunctionsInstancesApi.md#edge_applications_edge_application_id_functions_instances_functions_instances_id_patch) | **PATCH** /edge_applications/{edge_application_id}/functions_instances/{functions_instances_id} | /edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:
[**edge_applications_edge_application_id_functions_instances_functions_instances_id_put**](EdgeApplicationsEdgeFunctionsInstancesApi.md#edge_applications_edge_application_id_functions_instances_functions_instances_id_put) | **PUT** /edge_applications/{edge_application_id}/functions_instances/{functions_instances_id} | /edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:
[**edge_applications_edge_application_id_functions_instances_get**](EdgeApplicationsEdgeFunctionsInstancesApi.md#edge_applications_edge_application_id_functions_instances_get) | **GET** /edge_applications/{edge_application_id}/functions_instances | /edge_applications/:edge_application_id:/functions_instances
[**edge_applications_edge_application_id_functions_instances_post**](EdgeApplicationsEdgeFunctionsInstancesApi.md#edge_applications_edge_application_id_functions_instances_post) | **POST** /edge_applications/{edge_application_id}/functions_instances | edge_application/:edge_application_id:/functions_instances


# **edge_applications_edge_application_id_functions_instances_functions_instances_id_delete**
> edge_applications_edge_application_id_functions_instances_functions_instances_id_delete(edge_application_id, functions_instances_id, accept=accept, content_type=content_type)

/edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:

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
    api_instance = edgeapplications.EdgeApplicationsEdgeFunctionsInstancesApi(api_client)
    edge_application_id = 'edge_application_id_example' # str | 
    functions_instances_id = 'functions_instances_id_example' # str | 
    accept = 'application/json; version=3' # str |  (optional)
    content_type = 'application/json' # str | The type of coding used in the Body (application/json). <br>  Example: Content-Type: application/json (optional)

    try:
        # /edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:
        api_instance.edge_applications_edge_application_id_functions_instances_functions_instances_id_delete(edge_application_id, functions_instances_id, accept=accept, content_type=content_type)
    except Exception as e:
        print("Exception when calling EdgeApplicationsEdgeFunctionsInstancesApi->edge_applications_edge_application_id_functions_instances_functions_instances_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **str**|  | 
 **functions_instances_id** | **str**|  | 
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

# **edge_applications_edge_application_id_functions_instances_functions_instances_id_get**
> ApplicationInstancesGetOneResponse edge_applications_edge_application_id_functions_instances_functions_instances_id_get(edge_application_id, functions_instances_id, accept=accept)

/edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgeapplications
from edgeapplications.models.application_instances_get_one_response import ApplicationInstancesGetOneResponse
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
    api_instance = edgeapplications.EdgeApplicationsEdgeFunctionsInstancesApi(api_client)
    edge_application_id = 56 # int | 
    functions_instances_id = 56 # int | 
    accept = 'application/json; version=3' # str | The id of the edge function instance you plan to query.  (optional)

    try:
        # /edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:
        api_response = api_instance.edge_applications_edge_application_id_functions_instances_functions_instances_id_get(edge_application_id, functions_instances_id, accept=accept)
        print("The response of EdgeApplicationsEdgeFunctionsInstancesApi->edge_applications_edge_application_id_functions_instances_functions_instances_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsEdgeFunctionsInstancesApi->edge_applications_edge_application_id_functions_instances_functions_instances_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **int**|  | 
 **functions_instances_id** | **int**|  | 
 **accept** | **str**| The id of the edge function instance you plan to query.  | [optional] 

### Return type

[**ApplicationInstancesGetOneResponse**](ApplicationInstancesGetOneResponse.md)

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

# **edge_applications_edge_application_id_functions_instances_functions_instances_id_patch**
> ApplicationInstanceResults edge_applications_edge_application_id_functions_instances_functions_instances_id_patch(edge_application_id, functions_instances_id, accept=accept, content_type=content_type, application_update_instance_request=application_update_instance_request)

/edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgeapplications
from edgeapplications.models.application_instance_results import ApplicationInstanceResults
from edgeapplications.models.application_update_instance_request import ApplicationUpdateInstanceRequest
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
    api_instance = edgeapplications.EdgeApplicationsEdgeFunctionsInstancesApi(api_client)
    edge_application_id = 'edge_application_id_example' # str | The id of the edge application you plan to overwrite 
    functions_instances_id = 'functions_instances_id_example' # str | The id of the edge function instance you plan to overwrite.
    accept = 'application/json; version=3' # str |  (optional)
    content_type = 'application/json' # str | The type of coding used in the Body (application/json). <br>  Example: Content-Type: application/json (optional)
    application_update_instance_request = edgeapplications.ApplicationUpdateInstanceRequest() # ApplicationUpdateInstanceRequest |  (optional)

    try:
        # /edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:
        api_response = api_instance.edge_applications_edge_application_id_functions_instances_functions_instances_id_patch(edge_application_id, functions_instances_id, accept=accept, content_type=content_type, application_update_instance_request=application_update_instance_request)
        print("The response of EdgeApplicationsEdgeFunctionsInstancesApi->edge_applications_edge_application_id_functions_instances_functions_instances_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsEdgeFunctionsInstancesApi->edge_applications_edge_application_id_functions_instances_functions_instances_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **str**| The id of the edge application you plan to overwrite  | 
 **functions_instances_id** | **str**| The id of the edge function instance you plan to overwrite. | 
 **accept** | **str**|  | [optional] 
 **content_type** | **str**| The type of coding used in the Body (application/json). &lt;br&gt;  Example: Content-Type: application/json | [optional] 
 **application_update_instance_request** | [**ApplicationUpdateInstanceRequest**](ApplicationUpdateInstanceRequest.md)|  | [optional] 

### Return type

[**ApplicationInstanceResults**](ApplicationInstanceResults.md)

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
**405** | Method Not Allowed |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_applications_edge_application_id_functions_instances_functions_instances_id_put**
> ApplicationInstanceResults edge_applications_edge_application_id_functions_instances_functions_instances_id_put(edge_application_id, functions_instances_id, accept=accept, content_type=content_type, application_put_instance_request=application_put_instance_request)

/edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgeapplications
from edgeapplications.models.application_instance_results import ApplicationInstanceResults
from edgeapplications.models.application_put_instance_request import ApplicationPutInstanceRequest
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
    api_instance = edgeapplications.EdgeApplicationsEdgeFunctionsInstancesApi(api_client)
    edge_application_id = 'edge_application_id_example' # str | The id of the edge application you plan to overwrite 
    functions_instances_id = 'functions_instances_id_example' # str | The id of the edge function instance you plan to overwrite.
    accept = 'application/json; version=3' # str |  (optional)
    content_type = 'application/json' # str | The type of coding used in the Body (application/json). <br>  Example: Content-Type: application/json (optional)
    application_put_instance_request = edgeapplications.ApplicationPutInstanceRequest() # ApplicationPutInstanceRequest |  (optional)

    try:
        # /edge_applications/:edge_application_id:/functions_instances/:functions_instances_id:
        api_response = api_instance.edge_applications_edge_application_id_functions_instances_functions_instances_id_put(edge_application_id, functions_instances_id, accept=accept, content_type=content_type, application_put_instance_request=application_put_instance_request)
        print("The response of EdgeApplicationsEdgeFunctionsInstancesApi->edge_applications_edge_application_id_functions_instances_functions_instances_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsEdgeFunctionsInstancesApi->edge_applications_edge_application_id_functions_instances_functions_instances_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **str**| The id of the edge application you plan to overwrite  | 
 **functions_instances_id** | **str**| The id of the edge function instance you plan to overwrite. | 
 **accept** | **str**|  | [optional] 
 **content_type** | **str**| The type of coding used in the Body (application/json). &lt;br&gt;  Example: Content-Type: application/json | [optional] 
 **application_put_instance_request** | [**ApplicationPutInstanceRequest**](ApplicationPutInstanceRequest.md)|  | [optional] 

### Return type

[**ApplicationInstanceResults**](ApplicationInstanceResults.md)

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
**405** | Method Not Allowed |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_applications_edge_application_id_functions_instances_get**
> ApplicationInstancesGetResponse edge_applications_edge_application_id_functions_instances_get(edge_application_id, page=page, page_size=page_size, filter=filter, order_by=order_by, sort=sort, accept=accept)

/edge_applications/:edge_application_id:/functions_instances

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgeapplications
from edgeapplications.models.application_instances_get_response import ApplicationInstancesGetResponse
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
    api_instance = edgeapplications.EdgeApplicationsEdgeFunctionsInstancesApi(api_client)
    edge_application_id = 56 # int | 
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    filter = 'filter_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    sort = 'sort_example' # str |  (optional)
    accept = 'application/json; version=3' # str |  (optional)

    try:
        # /edge_applications/:edge_application_id:/functions_instances
        api_response = api_instance.edge_applications_edge_application_id_functions_instances_get(edge_application_id, page=page, page_size=page_size, filter=filter, order_by=order_by, sort=sort, accept=accept)
        print("The response of EdgeApplicationsEdgeFunctionsInstancesApi->edge_applications_edge_application_id_functions_instances_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsEdgeFunctionsInstancesApi->edge_applications_edge_application_id_functions_instances_get: %s\n" % e)
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

[**ApplicationInstancesGetResponse**](ApplicationInstancesGetResponse.md)

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

# **edge_applications_edge_application_id_functions_instances_post**
> ApplicationInstanceResults edge_applications_edge_application_id_functions_instances_post(edge_application_id, accept=accept, content_type=content_type, application_create_instance_request=application_create_instance_request)

edge_application/:edge_application_id:/functions_instances

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgeapplications
from edgeapplications.models.application_create_instance_request import ApplicationCreateInstanceRequest
from edgeapplications.models.application_instance_results import ApplicationInstanceResults
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
    api_instance = edgeapplications.EdgeApplicationsEdgeFunctionsInstancesApi(api_client)
    edge_application_id = 56 # int | 
    accept = 'application/json; version=3' # str |  (optional)
    content_type = 'application/json' # str | The type of coding used in the Body (application/json). <br>  Example: Content-Type: application/json (optional)
    application_create_instance_request = edgeapplications.ApplicationCreateInstanceRequest() # ApplicationCreateInstanceRequest |  (optional)

    try:
        # edge_application/:edge_application_id:/functions_instances
        api_response = api_instance.edge_applications_edge_application_id_functions_instances_post(edge_application_id, accept=accept, content_type=content_type, application_create_instance_request=application_create_instance_request)
        print("The response of EdgeApplicationsEdgeFunctionsInstancesApi->edge_applications_edge_application_id_functions_instances_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsEdgeFunctionsInstancesApi->edge_applications_edge_application_id_functions_instances_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **int**|  | 
 **accept** | **str**|  | [optional] 
 **content_type** | **str**| The type of coding used in the Body (application/json). &lt;br&gt;  Example: Content-Type: application/json | [optional] 
 **application_create_instance_request** | [**ApplicationCreateInstanceRequest**](ApplicationCreateInstanceRequest.md)|  | [optional] 

### Return type

[**ApplicationInstanceResults**](ApplicationInstanceResults.md)

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

