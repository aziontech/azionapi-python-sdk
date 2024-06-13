# edgeapplications.EdgeApplicationsMainSettingsApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edge_applications_get**](EdgeApplicationsMainSettingsApi.md#edge_applications_get) | **GET** /edge_applications | /edge_applications
[**edge_applications_id_delete**](EdgeApplicationsMainSettingsApi.md#edge_applications_id_delete) | **DELETE** /edge_applications/{id} | /edge_applications/:id
[**edge_applications_id_get**](EdgeApplicationsMainSettingsApi.md#edge_applications_id_get) | **GET** /edge_applications/{id} | /edge_applications/:id
[**edge_applications_id_patch**](EdgeApplicationsMainSettingsApi.md#edge_applications_id_patch) | **PATCH** /edge_applications/{id} | /edge_applications/:id
[**edge_applications_id_put**](EdgeApplicationsMainSettingsApi.md#edge_applications_id_put) | **PUT** /edge_applications/{id} | /edge_applications/:id
[**edge_applications_post**](EdgeApplicationsMainSettingsApi.md#edge_applications_post) | **POST** /edge_applications | /edge_applications


# **edge_applications_get**
> GetApplicationsResponse edge_applications_get(page=page, page_size=page_size, filter=filter, order_by=order_by, sort=sort, accept=accept)

/edge_applications

### Example

* Api Key Authentication (tokenAuth):

```python
import edgeapplications
from edgeapplications.models.get_applications_response import GetApplicationsResponse
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
    api_instance = edgeapplications.EdgeApplicationsMainSettingsApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    filter = 'filter_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    sort = 'sort_example' # str |  (optional)
    accept = 'application/json; version=3' # str |  (optional)

    try:
        # /edge_applications
        api_response = api_instance.edge_applications_get(page=page, page_size=page_size, filter=filter, order_by=order_by, sort=sort, accept=accept)
        print("The response of EdgeApplicationsMainSettingsApi->edge_applications_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsMainSettingsApi->edge_applications_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**GetApplicationsResponse**](GetApplicationsResponse.md)

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

# **edge_applications_id_delete**
> edge_applications_id_delete(id, accept=accept)

/edge_applications/:id

### Example

* Api Key Authentication (tokenAuth):

```python
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
    api_instance = edgeapplications.EdgeApplicationsMainSettingsApi(api_client)
    id = 'id_example' # str | The id of the edge application that you plan to delete.
    accept = 'application/json; version=3' # str |  (optional)

    try:
        # /edge_applications/:id
        api_instance.edge_applications_id_delete(id, accept=accept)
    except Exception as e:
        print("Exception when calling EdgeApplicationsMainSettingsApi->edge_applications_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the edge application that you plan to delete. | 
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
**204** | No response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_applications_id_get**
> GetApplicationResponse edge_applications_id_get(id, accept=accept)

/edge_applications/:id

### Example

* Api Key Authentication (tokenAuth):

```python
import edgeapplications
from edgeapplications.models.get_application_response import GetApplicationResponse
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
    api_instance = edgeapplications.EdgeApplicationsMainSettingsApi(api_client)
    id = 'id_example' # str | 
    accept = 'application/json; version=3' # str |  (optional)

    try:
        # /edge_applications/:id
        api_response = api_instance.edge_applications_id_get(id, accept=accept)
        print("The response of EdgeApplicationsMainSettingsApi->edge_applications_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsMainSettingsApi->edge_applications_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **accept** | **str**|  | [optional] 

### Return type

[**GetApplicationResponse**](GetApplicationResponse.md)

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

# **edge_applications_id_patch**
> ApplicationUpdateResponse edge_applications_id_patch(id, accept=accept, content_type=content_type, application_update_request=application_update_request)

/edge_applications/:id

### Example

* Api Key Authentication (tokenAuth):

```python
import edgeapplications
from edgeapplications.models.application_update_request import ApplicationUpdateRequest
from edgeapplications.models.application_update_response import ApplicationUpdateResponse
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
    api_instance = edgeapplications.EdgeApplicationsMainSettingsApi(api_client)
    id = 'id_example' # str | 
    accept = 'application/json; version=3' # str |  (optional)
    content_type = 'application/json' # str | The type of coding used in the Body (application/json). <br>  Example: Content-Type: application/json (optional)
    application_update_request = edgeapplications.ApplicationUpdateRequest() # ApplicationUpdateRequest |  (optional)

    try:
        # /edge_applications/:id
        api_response = api_instance.edge_applications_id_patch(id, accept=accept, content_type=content_type, application_update_request=application_update_request)
        print("The response of EdgeApplicationsMainSettingsApi->edge_applications_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsMainSettingsApi->edge_applications_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **content_type** | **str**| The type of coding used in the Body (application/json). &lt;br&gt;  Example: Content-Type: application/json | [optional] 
 **application_update_request** | [**ApplicationUpdateRequest**](ApplicationUpdateRequest.md)|  | [optional] 

### Return type

[**ApplicationUpdateResponse**](ApplicationUpdateResponse.md)

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

# **edge_applications_id_put**
> ApplicationPutResult edge_applications_id_put(id, accept=accept, content_type=content_type, application_put_request=application_put_request)

/edge_applications/:id

### Example

* Api Key Authentication (tokenAuth):

```python
import edgeapplications
from edgeapplications.models.application_put_request import ApplicationPutRequest
from edgeapplications.models.application_put_result import ApplicationPutResult
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
    api_instance = edgeapplications.EdgeApplicationsMainSettingsApi(api_client)
    id = 'id_example' # str | The Id of the edge application to be overwritten. 
    accept = 'application/json; version=3' # str |  (optional)
    content_type = 'application/json' # str | The type of coding used in the Body (application/json). <br>  Example: Content-Type: application/json (optional)
    application_put_request = edgeapplications.ApplicationPutRequest() # ApplicationPutRequest |  (optional)

    try:
        # /edge_applications/:id
        api_response = api_instance.edge_applications_id_put(id, accept=accept, content_type=content_type, application_put_request=application_put_request)
        print("The response of EdgeApplicationsMainSettingsApi->edge_applications_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsMainSettingsApi->edge_applications_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the edge application to be overwritten.  | 
 **accept** | **str**|  | [optional] 
 **content_type** | **str**| The type of coding used in the Body (application/json). &lt;br&gt;  Example: Content-Type: application/json | [optional] 
 **application_put_request** | [**ApplicationPutRequest**](ApplicationPutRequest.md)|  | [optional] 

### Return type

[**ApplicationPutResult**](ApplicationPutResult.md)

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

# **edge_applications_post**
> CreateApplicationResult edge_applications_post(accept=accept, content_type=content_type, create_application_request=create_application_request)

/edge_applications

### Example

* Api Key Authentication (tokenAuth):

```python
import edgeapplications
from edgeapplications.models.create_application_request import CreateApplicationRequest
from edgeapplications.models.create_application_result import CreateApplicationResult
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
    api_instance = edgeapplications.EdgeApplicationsMainSettingsApi(api_client)
    accept = 'application/json; version=3' # str |  (optional)
    content_type = 'application/json' # str | The type of coding used in the Body (application/json). <br>  Example: Content-Type: application/json (optional)
    create_application_request = edgeapplications.CreateApplicationRequest() # CreateApplicationRequest |  (optional)

    try:
        # /edge_applications
        api_response = api_instance.edge_applications_post(accept=accept, content_type=content_type, create_application_request=create_application_request)
        print("The response of EdgeApplicationsMainSettingsApi->edge_applications_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsMainSettingsApi->edge_applications_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  | [optional] 
 **content_type** | **str**| The type of coding used in the Body (application/json). &lt;br&gt;  Example: Content-Type: application/json | [optional] 
 **create_application_request** | [**CreateApplicationRequest**](CreateApplicationRequest.md)|  | [optional] 

### Return type

[**CreateApplicationResult**](CreateApplicationResult.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json; version=3
 - **Accept**: application/json; version=3

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**201** | Successful response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

