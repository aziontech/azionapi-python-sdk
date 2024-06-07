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
[**storage_api_s3_credentials_by_access_key**](StorageApi.md#storage_api_s3_credentials_by_access_key) | **GET** /v4/storage/s3-credentials/{s3_credential_access_key} | get by s3 credentials by access key
[**storage_api_s3_credentials_create**](StorageApi.md#storage_api_s3_credentials_create) | **POST** /v4/storage/s3-credentials | create s3 credentials
[**storage_api_s3_credentials_delete**](StorageApi.md#storage_api_s3_credentials_delete) | **DELETE** /v4/storage/s3-credentials/{s3_credential_access_key} | delete by s3 credentials
[**storage_api_s3_credentials_list**](StorageApi.md#storage_api_s3_credentials_list) | **GET** /v4/storage/s3-credentials | List s3 credentials


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
> PaginatedBucketObjectList storage_api_buckets_objects_list(bucket_name, continuation_token=continuation_token, max_object_count=max_object_count)

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
    continuation_token = 'continuation_token_example' # str | Token for next page. (optional)
    max_object_count = 56 # int | Number of results to return per page. (optional)

    try:
        # List buckets objects
        api_response = api_instance.storage_api_buckets_objects_list(bucket_name, continuation_token=continuation_token, max_object_count=max_object_count)
        print("The response of StorageApi->storage_api_buckets_objects_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_api_buckets_objects_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_name** | **str**|  | 
 **continuation_token** | **str**| Token for next page. | [optional] 
 **max_object_count** | **int**| Number of results to return per page. | [optional] 

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
> storage_api_buckets_objects_retrieve(bucket_name, object_key)

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
        api_instance.storage_api_buckets_objects_retrieve(bucket_name, object_key)
    except Exception as e:
        print("Exception when calling StorageApi->storage_api_buckets_objects_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_name** | **str**|  | 
 **object_key** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/json, application/xml, text/plain, image/jpeg, image/png, image/gif, video/mp4, audio/mpeg, application/pdf, application/javascript, text/css, application/octet-stream, multipart/form-data, application/x-www-form-urlencoded

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
> ResponseBucket storage_api_buckets_partial_update(name, bucket_update=bucket_update)

Update bucket info



### Example

* Api Key Authentication (tokenAuth):

```python
import storage
from storage.models.bucket_update import BucketUpdate
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
    bucket_update = storage.BucketUpdate() # BucketUpdate |  (optional)

    try:
        # Update bucket info
        api_response = api_instance.storage_api_buckets_partial_update(name, bucket_update=bucket_update)
        print("The response of StorageApi->storage_api_buckets_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_api_buckets_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **bucket_update** | [**BucketUpdate**](BucketUpdate.md)|  | [optional] 

### Return type

[**ResponseBucket**](ResponseBucket.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

# **storage_api_s3_credentials_by_access_key**
> ResponseS3Credential storage_api_s3_credentials_by_access_key(s3_credential_access_key)

get by s3 credentials by access key



### Example

* Api Key Authentication (tokenAuth):

```python
import storage
from storage.models.response_s3_credential import ResponseS3Credential
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
    s3_credential_access_key = 's3_credential_access_key_example' # str | 

    try:
        # get by s3 credentials by access key
        api_response = api_instance.storage_api_s3_credentials_by_access_key(s3_credential_access_key)
        print("The response of StorageApi->storage_api_s3_credentials_by_access_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_api_s3_credentials_by_access_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s3_credential_access_key** | **str**|  | 

### Return type

[**ResponseS3Credential**](ResponseS3Credential.md)

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

# **storage_api_s3_credentials_create**
> ResponseS3Credential storage_api_s3_credentials_create(s3_credential_create)

create s3 credentials



### Example

* Api Key Authentication (tokenAuth):

```python
import storage
from storage.models.response_s3_credential import ResponseS3Credential
from storage.models.s3_credential_create import S3CredentialCreate
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
    s3_credential_create = storage.S3CredentialCreate() # S3CredentialCreate | 

    try:
        # create s3 credentials
        api_response = api_instance.storage_api_s3_credentials_create(s3_credential_create)
        print("The response of StorageApi->storage_api_s3_credentials_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_api_s3_credentials_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s3_credential_create** | [**S3CredentialCreate**](S3CredentialCreate.md)|  | 

### Return type

[**ResponseS3Credential**](ResponseS3Credential.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_api_s3_credentials_delete**
> ResponseS3Credential storage_api_s3_credentials_delete(s3_credential_access_key)

delete by s3 credentials



### Example

* Api Key Authentication (tokenAuth):

```python
import storage
from storage.models.response_s3_credential import ResponseS3Credential
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
    s3_credential_access_key = 's3_credential_access_key_example' # str | 

    try:
        # delete by s3 credentials
        api_response = api_instance.storage_api_s3_credentials_delete(s3_credential_access_key)
        print("The response of StorageApi->storage_api_s3_credentials_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_api_s3_credentials_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s3_credential_access_key** | **str**|  | 

### Return type

[**ResponseS3Credential**](ResponseS3Credential.md)

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

# **storage_api_s3_credentials_list**
> PaginatedS3CredentialList storage_api_s3_credentials_list(key=key, last_modified=last_modified, size=size, continuation_token=continuation_token)

List s3 credentials



### Example

* Api Key Authentication (tokenAuth):

```python
import storage
from storage.models.paginated_s3_credential_list import PaginatedS3CredentialList
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
    key = 'key_example' # str | Object key. Used to identify the object for requests. Sent in POST requests as a path variable. (optional)
    last_modified = 'last_modified_example' # str | Timestamp of the last modification to the object. (optional)
    size = 56 # int | Size of file in bytes. (optional)
    continuation_token = 'continuation_token_example' # str | Hash that can be added to the continuation_token query to skip list to the next page. (optional)

    try:
        # List s3 credentials
        api_response = api_instance.storage_api_s3_credentials_list(key=key, last_modified=last_modified, size=size, continuation_token=continuation_token)
        print("The response of StorageApi->storage_api_s3_credentials_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->storage_api_s3_credentials_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Object key. Used to identify the object for requests. Sent in POST requests as a path variable. | [optional] 
 **last_modified** | **str**| Timestamp of the last modification to the object. | [optional] 
 **size** | **int**| Size of file in bytes. | [optional] 
 **continuation_token** | **str**| Hash that can be added to the continuation_token query to skip list to the next page. | [optional] 

### Return type

[**PaginatedS3CredentialList**](PaginatedS3CredentialList.md)

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

