<a id="__pageTop"></a>
# storageapi.apis.tags.default_api.DefaultApi

All URIs are relative to *https://storage-api.azion.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_version**](#delete_version) | **delete** /storage/{version_id}/delete | /storage/:version_id/delete
[**storage_version_id_post**](#storage_version_id_post) | **post** /storage/{version_id} | /storage/:version_id

# **delete_version**
<a id="delete_version"></a>
> delete_version(version_id)

/storage/:version_id/delete

Delete a version. A version is just um path prefix/sub-namespace for a set of files.

### Example

* Api Key Authentication (tokenAuth):
```python
import storageapi
from storageapi.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://storage-api.azion.com
# See configuration.py for a list of all supported configuration parameters.
configuration = storageapi.Configuration(
    host = "https://storage-api.azion.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'
# Enter a context with an instance of the API client
with storageapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'version_id': "version_id_example",
    }
    try:
        # /storage/:version_id/delete
        api_response = api_instance.delete_version(
            path_params=path_params,
        )
    except storageapi.ApiException as e:
        print("Exception when calling DefaultApi->delete_version: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version_id | VersionIdSchema | | 

# VersionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_version.ApiResponseFor204) | The resource was deleted successfully.

#### delete_version.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **storage_version_id_post**
<a id="storage_version_id_post"></a>
> bool, date, datetime, dict, float, int, list, str, none_type storage_version_id_post(x_azion_static_pathversion_id)

/storage/:version_id

Upload file and transfer to remote storage

### Example

* Api Key Authentication (tokenAuth):
```python
import storageapi
from storageapi.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://storage-api.azion.com
# See configuration.py for a list of all supported configuration parameters.
configuration = storageapi.Configuration(
    host = "https://storage-api.azion.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'
# Enter a context with an instance of the API client
with storageapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'version_id': "version_id_example",
    }
    header_params = {
        'X-Azion-Static-Path': "X-Azion-Static-Path_example",
    }
    try:
        # /storage/:version_id
        api_response = api_instance.storage_version_id_post(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except storageapi.ApiException as e:
        print("Exception when calling DefaultApi->storage_version_id_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'version_id': "version_id_example",
    }
    header_params = {
        'Content-Type': "b2/x-auto",
        'X-Azion-Static-Path': "X-Azion-Static-Path_example",
    }
    body = open('/path/to/file', 'rb')
    try:
        # /storage/:version_id
        api_response = api_instance.storage_version_id_post(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except storageapi.ApiException as e:
        print("Exception when calling DefaultApi->storage_version_id_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationOctetStream, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/octet-stream' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationOctetStream

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Content-Type | ContentTypeSchema | | optional
X-Azion-Static-Path | XAzionStaticPathSchema | | 

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "b2/x-auto"

# XAzionStaticPathSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version_id | VersionIdSchema | | 

# VersionIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#storage_version_id_post.ApiResponseFor201) | 

#### storage_version_id_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

