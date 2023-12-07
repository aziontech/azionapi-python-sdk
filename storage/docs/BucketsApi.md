# storage.BucketsApi

All URIs are relative to *https://api.azion.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_storage_buckets_create**](BucketsApi.md#api_v1_storage_buckets_create) | **POST** /v4/storage/buckets | /v4/storage/buckets
[**api_v1_storage_buckets_destroy**](BucketsApi.md#api_v1_storage_buckets_destroy) | **DELETE** /v4/storage/buckets/{name} | /v4/storage/buckets/:name
[**api_v1_storage_buckets_list**](BucketsApi.md#api_v1_storage_buckets_list) | **GET** /v4/storage/buckets | /v4/storage/buckets
[**api_v1_storage_buckets_partial_update**](BucketsApi.md#api_v1_storage_buckets_partial_update) | **PATCH** /v4/storage/buckets/{name} | /v4/storage/buckets/:name


# **api_v1_storage_buckets_create**
> ResponseBucket api_v1_storage_buckets_create(bucket_create)

/v4/storage/buckets



### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import storage
from storage.models.bucket_create import BucketCreate
from storage.models.response_bucket import ResponseBucket
from storage.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azion.com
# See configuration.py for a list of all supported configuration parameters.
configuration = storage.Configuration(
    host = "https://api.azion.com"
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
with storage.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = storage.BucketsApi(api_client)
    bucket_create = storage.BucketCreate() # BucketCreate | 

    try:
        # /v4/storage/buckets
        api_response = api_instance.api_v1_storage_buckets_create(bucket_create)
        print("The response of BucketsApi->api_v1_storage_buckets_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketsApi->api_v1_storage_buckets_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_create** | [**BucketCreate**](BucketCreate.md)|  | 

### Return type

[**ResponseBucket**](ResponseBucket.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**406** | Not Acceptable |  -  |
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_storage_buckets_destroy**
> ResponseDeleteBucket api_v1_storage_buckets_destroy(name)

/v4/storage/buckets/:name



### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import storage
from storage.models.response_delete_bucket import ResponseDeleteBucket
from storage.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azion.com
# See configuration.py for a list of all supported configuration parameters.
configuration = storage.Configuration(
    host = "https://api.azion.com"
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
with storage.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = storage.BucketsApi(api_client)
    name = 'name_example' # str | 

    try:
        # /v4/storage/buckets/:name
        api_response = api_instance.api_v1_storage_buckets_destroy(name)
        print("The response of BucketsApi->api_v1_storage_buckets_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketsApi->api_v1_storage_buckets_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**ResponseDeleteBucket**](ResponseDeleteBucket.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**406** | Not Acceptable |  -  |
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_storage_buckets_list**
> PaginatedBucketList api_v1_storage_buckets_list(page=page, page_size=page_size)

/v4/storage/buckets



### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import storage
from storage.models.paginated_bucket_list import PaginatedBucketList
from storage.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azion.com
# See configuration.py for a list of all supported configuration parameters.
configuration = storage.Configuration(
    host = "https://api.azion.com"
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
with storage.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = storage.BucketsApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        # /v4/storage/buckets
        api_response = api_instance.api_v1_storage_buckets_list(page=page, page_size=page_size)
        print("The response of BucketsApi->api_v1_storage_buckets_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketsApi->api_v1_storage_buckets_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedBucketList**](PaginatedBucketList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**406** | Not Acceptable |  -  |
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_storage_buckets_partial_update**
> ResponseBucket api_v1_storage_buckets_partial_update(name, patched_bucket=patched_bucket)

/v4/storage/buckets/:name



### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import storage
from storage.models.patched_bucket import PatchedBucket
from storage.models.response_bucket import ResponseBucket
from storage.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azion.com
# See configuration.py for a list of all supported configuration parameters.
configuration = storage.Configuration(
    host = "https://api.azion.com"
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
with storage.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = storage.BucketsApi(api_client)
    name = 'name_example' # str | 
    patched_bucket = storage.PatchedBucket() # PatchedBucket |  (optional)

    try:
        # /v4/storage/buckets/:name
        api_response = api_instance.api_v1_storage_buckets_partial_update(name, patched_bucket=patched_bucket)
        print("The response of BucketsApi->api_v1_storage_buckets_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketsApi->api_v1_storage_buckets_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **patched_bucket** | [**PatchedBucket**](PatchedBucket.md)|  | [optional] 

### Return type

[**ResponseBucket**](ResponseBucket.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**406** | Not Acceptable |  -  |
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

