# storage.StorageApi

All URIs are relative to *https://api.azion.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storage_api_buckets_create**](StorageApi.md#storage_api_buckets_create) | **POST** /v4/storage/buckets | Create a new bucket
[**storage_api_buckets_destroy**](StorageApi.md#storage_api_buckets_destroy) | **DELETE** /v4/storage/buckets/{name} | Delete a bucket
[**storage_api_buckets_list**](StorageApi.md#storage_api_buckets_list) | **GET** /v4/storage/buckets | List buckets
[**storage_api_buckets_objects_create**](StorageApi.md#storage_api_buckets_objects_create) | **POST** /v4/storage/buckets/{bucket_name}/objects/{object_key} | Create new object key
[**storage_api_buckets_objects_destroy**](StorageApi.md#storage_api_buckets_objects_destroy) | **DELETE** /v4/storage/buckets/{bucket_name}/objects/{object_key} | Delete object key
[**storage_api_buckets_objects_list**](StorageApi.md#storage_api_buckets_objects_list) | **GET** /v4/storage/buckets/{bucket_name}/objects | List buckets objects
[**storage_api_buckets_objects_retrieve**](StorageApi.md#storage_api_buckets_objects_retrieve) | **GET** /v4/storage/buckets/{bucket_name}/objects/{object_key} | Download object
[**storage_api_buckets_objects_update**](StorageApi.md#storage_api_buckets_objects_update) | **PUT** /v4/storage/buckets/{bucket_name}/objects/{object_key} | Update the object key
[**storage_api_buckets_partial_update**](StorageApi.md#storage_api_buckets_partial_update) | **PATCH** /v4/storage/buckets/{name} | Update bucket info


# **storage_api_buckets_create**
> ResponseBucket storage_api_buckets_create(bucket_create)

Create a new bucket



### Example

* Api Key Authentication (tokenAuth):

```python
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
    api_instance = storage.StorageApi(api_client)
    bucket_create = storage.BucketCreate() # BucketCreate | 

    try:
        # Create a new bucket
        api_response = api_instance.storage_api_buckets_create(bucket_create)
        print("The response of StorageApi->storage_api_buckets_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_api_buckets_create: %s\n" % e)
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

# **storage_api_buckets_destroy**
> SuccessBucketOperation storage_api_buckets_destroy(name)

Delete a bucket



### Example

* Api Key Authentication (tokenAuth):

```python
import storage
from storage.models.success_bucket_operation import SuccessBucketOperation
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
    api_instance = storage.StorageApi(api_client)
    name = 'name_example' # str | 

    try:
        # Delete a bucket
        api_response = api_instance.storage_api_buckets_destroy(name)
        print("The response of StorageApi->storage_api_buckets_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_api_buckets_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**SuccessBucketOperation**](SuccessBucketOperation.md)

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

# **storage_api_buckets_list**
> PaginatedBucketList storage_api_buckets_list(page=page, page_size=page_size)

List buckets



### Example

* Api Key Authentication (tokenAuth):

```python
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
    api_instance = storage.StorageApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        # List buckets
        api_response = api_instance.storage_api_buckets_list(page=page, page_size=page_size)
        print("The response of StorageApi->storage_api_buckets_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_api_buckets_list: %s\n" % e)
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

# **storage_api_buckets_objects_create**
> SuccessObjectOperation storage_api_buckets_objects_create(bucket_name, object_key, content_type=content_type, body=body)

Create new object key

Create a new object key in the bucket.

### Example

* Api Key Authentication (tokenAuth):

```python
import storage
from storage.models.success_object_operation import SuccessObjectOperation
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
    api_instance = storage.StorageApi(api_client)
    bucket_name = 'bucket_name_example' # str | 
    object_key = 'object_key_example' # str | 
    content_type = 'content_type_example' # str | The content type of the file (Example: text/plain). (optional)
    body = None # bytearray |  (optional)

    try:
        # Create new object key
        api_response = api_instance.storage_api_buckets_objects_create(bucket_name, object_key, content_type=content_type, body=body)
        print("The response of StorageApi->storage_api_buckets_objects_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_api_buckets_objects_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_name** | **str**|  | 
 **object_key** | **str**|  | 
 **content_type** | **str**| The content type of the file (Example: text/plain). | [optional] 
 **body** | **bytearray**|  | [optional] 

### Return type

[**SuccessObjectOperation**](SuccessObjectOperation.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**406** | Not Acceptable |  -  |
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_api_buckets_objects_destroy**
> SuccessObjectOperation storage_api_buckets_objects_destroy(bucket_name, object_key)

Delete object key

Delete an object key from bucket

### Example

* Api Key Authentication (tokenAuth):

```python
import storage
from storage.models.success_object_operation import SuccessObjectOperation
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
    api_instance = storage.StorageApi(api_client)
    bucket_name = 'bucket_name_example' # str | 
    object_key = 'object_key_example' # str | 

    try:
        # Delete object key
        api_response = api_instance.storage_api_buckets_objects_destroy(bucket_name, object_key)
        print("The response of StorageApi->storage_api_buckets_objects_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_api_buckets_objects_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_name** | **str**|  | 
 **object_key** | **str**|  | 

### Return type

[**SuccessObjectOperation**](SuccessObjectOperation.md)

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

# **storage_api_buckets_objects_list**
> PaginatedBucketObjectList storage_api_buckets_objects_list(bucket_name, page=page, page_size=page_size)

List buckets objects



### Example

* Api Key Authentication (tokenAuth):

```python
import storage
from storage.models.paginated_bucket_object_list import PaginatedBucketObjectList
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
    api_instance = storage.StorageApi(api_client)
    bucket_name = 'bucket_name_example' # str | 
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)

    try:
        # List buckets objects
        api_response = api_instance.storage_api_buckets_objects_list(bucket_name, page=page, page_size=page_size)
        print("The response of StorageApi->storage_api_buckets_objects_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_api_buckets_objects_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_name** | **str**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**PaginatedBucketObjectList**](PaginatedBucketObjectList.md)

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

# **storage_api_buckets_objects_retrieve**
> bytearray storage_api_buckets_objects_retrieve(bucket_name, object_key)

Download object

Download the object key from bucket.

### Example

* Api Key Authentication (tokenAuth):

```python
import storage
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
    api_instance = storage.StorageApi(api_client)
    bucket_name = 'bucket_name_example' # str | 
    object_key = 'object_key_example' # str | 

    try:
        # Download object
        api_response = api_instance.storage_api_buckets_objects_retrieve(bucket_name, object_key)
        print("The response of StorageApi->storage_api_buckets_objects_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_api_buckets_objects_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_name** | **str**|  | 
 **object_key** | **str**|  | 

### Return type

**bytearray**

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

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

# **storage_api_buckets_objects_update**
> SuccessObjectOperation storage_api_buckets_objects_update(bucket_name, object_key, content_type=content_type, body=body)

Update the object key

Update the object key from bucket.

### Example

* Api Key Authentication (tokenAuth):

```python
import storage
from storage.models.success_object_operation import SuccessObjectOperation
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
    api_instance = storage.StorageApi(api_client)
    bucket_name = 'bucket_name_example' # str | 
    object_key = 'object_key_example' # str | 
    content_type = 'content_type_example' # str | The content type of the file (Example: text/plain). (optional)
    body = None # bytearray |  (optional)

    try:
        # Update the object key
        api_response = api_instance.storage_api_buckets_objects_update(bucket_name, object_key, content_type=content_type, body=body)
        print("The response of StorageApi->storage_api_buckets_objects_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_api_buckets_objects_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_name** | **str**|  | 
 **object_key** | **str**|  | 
 **content_type** | **str**| The content type of the file (Example: text/plain). | [optional] 
 **body** | **bytearray**|  | [optional] 

### Return type

[**SuccessObjectOperation**](SuccessObjectOperation.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
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

# **storage_api_buckets_partial_update**
> ResponseBucket storage_api_buckets_partial_update(name)

Update bucket info



### Example

* Api Key Authentication (tokenAuth):

```python
import storage
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
    api_instance = storage.StorageApi(api_client)
    name = 'name_example' # str | 

    try:
        # Update bucket info
        api_response = api_instance.storage_api_buckets_partial_update(name)
        print("The response of StorageApi->storage_api_buckets_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_api_buckets_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**ResponseBucket**](ResponseBucket.md)

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

