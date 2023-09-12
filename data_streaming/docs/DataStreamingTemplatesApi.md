# data_streaming.DataStreamingTemplatesApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_straming_template_by_id**](DataStreamingTemplatesApi.md#get_data_straming_template_by_id) | **GET** /data_streaming/templates/{template_id} | Get an global Template info by template ID
[**list_data_streaming_templates**](DataStreamingTemplatesApi.md#list_data_streaming_templates) | **GET** /data_streaming/templates | List all global Templates that can be used on Data Streaming operations


# **get_data_straming_template_by_id**
> TemplateResultById get_data_straming_template_by_id(template_id)

Get an global Template info by template ID

Use the GET method and add the data streaming's ID to the URI of the request to get more data on a specific data streaming global template.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import data_streaming
from data_streaming.models.template_result_by_id import TemplateResultById
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
    api_instance = data_streaming.DataStreamingTemplatesApi(api_client)
    template_id = 56 # int | 

    try:
        # Get an global Template info by template ID
        api_response = api_instance.get_data_straming_template_by_id(template_id)
        print("The response of DataStreamingTemplatesApi->get_data_straming_template_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataStreamingTemplatesApi->get_data_straming_template_by_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **int**|  | 

### Return type

[**TemplateResultById**](TemplateResultById.md)

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
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_data_streaming_templates**
> TemplateResults list_data_streaming_templates()

List all global Templates that can be used on Data Streaming operations

Use the GET method to list all global templates that can be used on Data Streaming operations.  **Note:** Customized templates won't be listed. 

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import data_streaming
from data_streaming.models.template_results import TemplateResults
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
    api_instance = data_streaming.DataStreamingTemplatesApi(api_client)

    try:
        # List all global Templates that can be used on Data Streaming operations
        api_response = api_instance.list_data_streaming_templates()
        print("The response of DataStreamingTemplatesApi->list_data_streaming_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataStreamingTemplatesApi->list_data_streaming_templates: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**TemplateResults**](TemplateResults.md)

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

