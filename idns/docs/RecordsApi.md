# idns.RecordsApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_zone_record**](RecordsApi.md#delete_zone_record) | **DELETE** /intelligent_dns/{zone_id}/records/{record_id} | Remove an Intelligent DNS zone record
[**get_zone_records**](RecordsApi.md#get_zone_records) | **GET** /intelligent_dns/{zone_id}/records | Get a collection of Intelligent DNS zone records
[**post_zone_record**](RecordsApi.md#post_zone_record) | **POST** /intelligent_dns/{zone_id}/records | Create a new Intelligent DNS zone record
[**put_zone_record**](RecordsApi.md#put_zone_record) | **PUT** /intelligent_dns/{zone_id}/records/{record_id} | Update an Intelligent DNS zone record


# **delete_zone_record**
> str delete_zone_record(zone_id, record_id)

Remove an Intelligent DNS zone record

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import idns
from idns.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = idns.Configuration(
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
with idns.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = idns.RecordsApi(api_client)
    zone_id = 56 # int | The hosted zone id
    record_id = 56 # int | The zone record id

    try:
        # Remove an Intelligent DNS zone record
        api_response = api_instance.delete_zone_record(zone_id, record_id)
        print("The response of RecordsApi->delete_zone_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->delete_zone_record: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**| The hosted zone id | 
 **record_id** | **int**| The zone record id | 

### Return type

**str**

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Record removed |  -  |
**404** | Record not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_records**
> GetRecordsResponse get_zone_records(zone_id)

Get a collection of Intelligent DNS zone records

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import idns
from idns.models.get_records_response import GetRecordsResponse
from idns.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = idns.Configuration(
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
with idns.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = idns.RecordsApi(api_client)
    zone_id = 56 # int | The hosted zone id

    try:
        # Get a collection of Intelligent DNS zone records
        api_response = api_instance.get_zone_records(zone_id)
        print("The response of RecordsApi->get_zone_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->get_zone_records: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**| The hosted zone id | 

### Return type

[**GetRecordsResponse**](GetRecordsResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Zones collection retrieved |  -  |
**400** | Error |  -  |
**404** | Zone not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_zone_record**
> PostOrPutRecordResponse post_zone_record(zone_id, record_post_or_put=record_post_or_put)

Create a new Intelligent DNS zone record

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import idns
from idns.models.post_or_put_record_response import PostOrPutRecordResponse
from idns.models.record_post_or_put import RecordPostOrPut
from idns.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = idns.Configuration(
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
with idns.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = idns.RecordsApi(api_client)
    zone_id = 56 # int | The hosted zone id
    record_post_or_put = {"record_type":"A","entry":"site","description":"Site record","ttl":3600,"answers_list":["1.2.3.4","5.6.7.8"]} # RecordPostOrPut |  (optional)

    try:
        # Create a new Intelligent DNS zone record
        api_response = api_instance.post_zone_record(zone_id, record_post_or_put=record_post_or_put)
        print("The response of RecordsApi->post_zone_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->post_zone_record: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**| The hosted zone id | 
 **record_post_or_put** | [**RecordPostOrPut**](RecordPostOrPut.md)|  | [optional] 

### Return type

[**PostOrPutRecordResponse**](PostOrPutRecordResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Record added |  -  |
**400** | Error |  -  |
**404** | Zone not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_zone_record**
> PostOrPutRecordResponse put_zone_record(zone_id, record_id, record_post_or_put=record_post_or_put)

Update an Intelligent DNS zone record

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import idns
from idns.models.post_or_put_record_response import PostOrPutRecordResponse
from idns.models.record_post_or_put import RecordPostOrPut
from idns.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = idns.Configuration(
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
with idns.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = idns.RecordsApi(api_client)
    zone_id = 56 # int | The hosted zone id
    record_id = 56 # int | The zone record id
    record_post_or_put = {"record_type":"A","entry":"site","description":"Site record","ttl":3600,"answers_list":["1.2.3.4","5.6.7.8","1.1.2.2"]} # RecordPostOrPut |  (optional)

    try:
        # Update an Intelligent DNS zone record
        api_response = api_instance.put_zone_record(zone_id, record_id, record_post_or_put=record_post_or_put)
        print("The response of RecordsApi->put_zone_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->put_zone_record: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**| The hosted zone id | 
 **record_id** | **int**| The zone record id | 
 **record_post_or_put** | [**RecordPostOrPut**](RecordPostOrPut.md)|  | [optional] 

### Return type

[**PostOrPutRecordResponse**](PostOrPutRecordResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Record updated |  -  |
**400** | Record update error |  -  |
**404** | Record not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

