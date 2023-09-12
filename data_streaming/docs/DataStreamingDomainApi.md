# data_streaming.DataStreamingDomainApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_data_streaming**](DataStreamingDomainApi.md#list_data_streaming) | **GET** /data_streaming/domains | List all domains used on data streaming


# **list_data_streaming**
> DataStreamingsDomainResponse list_data_streaming(name=name, streaming_id=streaming_id, selected=selected)

List all domains used on data streaming

Use the GET method to list all available domains that can be used on Data Streaming operations.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import data_streaming
from data_streaming.models.data_streamings_domain_response import DataStreamingsDomainResponse
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
    api_instance = data_streaming.DataStreamingDomainApi(api_client)
    name = 'name_example' # str | Domain's name in data streaming (optional)
    streaming_id = 56 # int |  (optional)
    selected = True # bool |  (optional)

    try:
        # List all domains used on data streaming
        api_response = api_instance.list_data_streaming(name=name, streaming_id=streaming_id, selected=selected)
        print("The response of DataStreamingDomainApi->list_data_streaming:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataStreamingDomainApi->list_data_streaming: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Domain&#39;s name in data streaming | [optional] 
 **streaming_id** | **int**|  | [optional] 
 **selected** | **bool**|  | [optional] 

### Return type

[**DataStreamingsDomainResponse**](DataStreamingsDomainResponse.md)

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

