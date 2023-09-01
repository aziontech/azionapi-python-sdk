# data_streaming.DataStreamingApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_data_streaming**](DataStreamingApi.md#create_new_data_streaming) | **POST** /data_streaming/streamings | Create a new data streaming
[**delete_data_streaming_by_id**](DataStreamingApi.md#delete_data_streaming_by_id) | **DELETE** /data_streaming/streamings/{data_streaming_id} | Delete data streaming
[**edit_data_streaming_by_id**](DataStreamingApi.md#edit_data_streaming_by_id) | **PATCH** /data_streaming/streamings/{data_streaming_id} | Edit data streaming
[**list_data_streaming_by_id**](DataStreamingApi.md#list_data_streaming_by_id) | **GET** /data_streaming/streamings/{data_streaming_id} | Get expecific data streaming by Data Streaming ID
[**list_data_streamings**](DataStreamingApi.md#list_data_streamings) | **GET** /data_streaming/streamings | List all exist data streamings
[**overwrite_data_streaming_by_id**](DataStreamingApi.md#overwrite_data_streaming_by_id) | **PUT** /data_streaming/streamings/{data_streaming_id} | Overwrite data streaming


# **create_new_data_streaming**
> CreateNewDataStreaming201Response create_new_data_streaming(create_new_data_streaming_request)

Create a new data streaming

Create a new data streaming.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import data_streaming
from data_streaming.models.create_new_data_streaming201_response import CreateNewDataStreaming201Response
from data_streaming.models.create_new_data_streaming_request import CreateNewDataStreamingRequest
from data_streaming.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = data_streaming.Configuration(
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
with data_streaming.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_streaming.DataStreamingApi(api_client)
    create_new_data_streaming_request = data_streaming.CreateNewDataStreamingRequest() # CreateNewDataStreamingRequest | 

    try:
        # Create a new data streaming
        api_response = api_instance.create_new_data_streaming(create_new_data_streaming_request)
        print("The response of DataStreamingApi->create_new_data_streaming:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataStreamingApi->create_new_data_streaming: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_new_data_streaming_request** | [**CreateNewDataStreamingRequest**](CreateNewDataStreamingRequest.md)|  | 

### Return type

[**CreateNewDataStreaming201Response**](CreateNewDataStreaming201Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**406** | Not Acceptable |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data_streaming_by_id**
> delete_data_streaming_by_id(data_streaming_id)

Delete data streaming

Use the DELETE method to remove a data streaming from your account. 

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import data_streaming
from data_streaming.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = data_streaming.Configuration(
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
with data_streaming.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_streaming.DataStreamingApi(api_client)
    data_streaming_id = 56 # int | 

    try:
        # Delete data streaming
        api_instance.delete_data_streaming_by_id(data_streaming_id)
    except Exception as e:
        print("Exception when calling DataStreamingApi->delete_data_streaming_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_streaming_id** | **int**|  | 

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
**204** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**406** | Not Acceptable |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_data_streaming_by_id**
> CreateNewDataStreaming201Response edit_data_streaming_by_id(data_streaming_id, create_new_data_streaming_request)

Edit data streaming

Use the PATCH method to change only select settings of your data streaming. 

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import data_streaming
from data_streaming.models.create_new_data_streaming201_response import CreateNewDataStreaming201Response
from data_streaming.models.create_new_data_streaming_request import CreateNewDataStreamingRequest
from data_streaming.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = data_streaming.Configuration(
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
with data_streaming.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_streaming.DataStreamingApi(api_client)
    data_streaming_id = 56 # int | 
    create_new_data_streaming_request = data_streaming.CreateNewDataStreamingRequest() # CreateNewDataStreamingRequest | 

    try:
        # Edit data streaming
        api_response = api_instance.edit_data_streaming_by_id(data_streaming_id, create_new_data_streaming_request)
        print("The response of DataStreamingApi->edit_data_streaming_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataStreamingApi->edit_data_streaming_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_streaming_id** | **int**|  | 
 **create_new_data_streaming_request** | [**CreateNewDataStreamingRequest**](CreateNewDataStreamingRequest.md)|  | 

### Return type

[**CreateNewDataStreaming201Response**](CreateNewDataStreaming201Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**406** | Not Acceptable |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_data_streaming_by_id**
> DataStreamingsById list_data_streaming_by_id(data_streaming_id)

Get expecific data streaming by Data Streaming ID

Use the GET method and add the data streaming's ID to the URI of the request to get more data on a specific data streaming.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import data_streaming
from data_streaming.models.data_streamings_by_id import DataStreamingsById
from data_streaming.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = data_streaming.Configuration(
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
with data_streaming.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_streaming.DataStreamingApi(api_client)
    data_streaming_id = 56 # int | 

    try:
        # Get expecific data streaming by Data Streaming ID
        api_response = api_instance.list_data_streaming_by_id(data_streaming_id)
        print("The response of DataStreamingApi->list_data_streaming_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataStreamingApi->list_data_streaming_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_streaming_id** | **int**|  | 

### Return type

[**DataStreamingsById**](DataStreamingsById.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**406** | Not Acceptable |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_data_streamings**
> DataStreamingResponseWithResults list_data_streamings()

List all exist data streamings

Use the GET method to list all data streamings, both active and inactive, and its properties.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import data_streaming
from data_streaming.models.data_streaming_response_with_results import DataStreamingResponseWithResults
from data_streaming.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = data_streaming.Configuration(
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
with data_streaming.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_streaming.DataStreamingApi(api_client)

    try:
        # List all exist data streamings
        api_response = api_instance.list_data_streamings()
        print("The response of DataStreamingApi->list_data_streamings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataStreamingApi->list_data_streamings: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**DataStreamingResponseWithResults**](DataStreamingResponseWithResults.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**406** | Not Acceptable |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **overwrite_data_streaming_by_id**
> CreateNewDataStreaming201Response overwrite_data_streaming_by_id(data_streaming_id, create_new_data_streaming_request)

Overwrite data streaming

Use the PUT method to overwrite the data streaming. Although  you can change a single property using the PUT method, you must pass all fields for the request to be completed. 

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import data_streaming
from data_streaming.models.create_new_data_streaming201_response import CreateNewDataStreaming201Response
from data_streaming.models.create_new_data_streaming_request import CreateNewDataStreamingRequest
from data_streaming.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = data_streaming.Configuration(
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
with data_streaming.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_streaming.DataStreamingApi(api_client)
    data_streaming_id = 56 # int | 
    create_new_data_streaming_request = data_streaming.CreateNewDataStreamingRequest() # CreateNewDataStreamingRequest | 

    try:
        # Overwrite data streaming
        api_response = api_instance.overwrite_data_streaming_by_id(data_streaming_id, create_new_data_streaming_request)
        print("The response of DataStreamingApi->overwrite_data_streaming_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataStreamingApi->overwrite_data_streaming_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_streaming_id** | **int**|  | 
 **create_new_data_streaming_request** | [**CreateNewDataStreamingRequest**](CreateNewDataStreamingRequest.md)|  | 

### Return type

[**CreateNewDataStreaming201Response**](CreateNewDataStreaming201Response.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**406** | Not Acceptable |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

