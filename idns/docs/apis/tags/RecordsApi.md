<a id="__pageTop"></a>
# idns.apis.tags.records_api.RecordsApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_zone_record**](#delete_zone_record) | **delete** /intelligent_dns/{zone_id}/records/{record_id} | Remove an Intelligent DNS zone record
[**get_zone_records**](#get_zone_records) | **get** /intelligent_dns/{zone_id}/records | Get a collection of Intelligent DNS zone records
[**post_zone_record**](#post_zone_record) | **post** /intelligent_dns/{zone_id}/records | Create a new Intelligent DNS zone record
[**put_zone_record**](#put_zone_record) | **put** /intelligent_dns/{zone_id}/records/{record_id} | Update an Intelligent DNS zone record

# **delete_zone_record**
<a id="delete_zone_record"></a>
> str, none_type delete_zone_record(zone_idrecord_id)

Remove an Intelligent DNS zone record

### Example

* Api Key Authentication (tokenAuth):
```python
import idns
from idns.apis.tags import records_api
from idns.model.error_response import ErrorResponse
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
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'
# Enter a context with an instance of the API client
with idns.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = records_api.RecordsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'zone_id': 1,
        'record_id': 1,
    }
    try:
        # Remove an Intelligent DNS zone record
        api_response = api_instance.delete_zone_record(
            path_params=path_params,
        )
        pprint(api_response)
    except idns.ApiException as e:
        print("Exception when calling RecordsApi->delete_zone_record: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
zone_id | ZoneIdSchema | | 
record_id | RecordIdSchema | | 

# ZoneIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RecordIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_zone_record.ApiResponseFor204) | Record removed
404 | [ApiResponseFor404](#delete_zone_record.ApiResponseFor404) | Record not found

#### delete_zone_record.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor204ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor204ResponseBodyApplicationJsonVersion3

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  |  | 

#### delete_zone_record.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_zone_records**
<a id="get_zone_records"></a>
> GetRecordsResponse get_zone_records(zone_id)

Get a collection of Intelligent DNS zone records

### Example

* Api Key Authentication (tokenAuth):
```python
import idns
from idns.apis.tags import records_api
from idns.model.error_response import ErrorResponse
from idns.model.get_records_response import GetRecordsResponse
from idns.model.errors_response import ErrorsResponse
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
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'
# Enter a context with an instance of the API client
with idns.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = records_api.RecordsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'zone_id': 1,
    }
    try:
        # Get a collection of Intelligent DNS zone records
        api_response = api_instance.get_zone_records(
            path_params=path_params,
        )
        pprint(api_response)
    except idns.ApiException as e:
        print("Exception when calling RecordsApi->get_zone_records: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
zone_id | ZoneIdSchema | | 

# ZoneIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_zone_records.ApiResponseFor200) | Zones collection retrieved
400 | [ApiResponseFor400](#get_zone_records.ApiResponseFor400) | Error
404 | [ApiResponseFor404](#get_zone_records.ApiResponseFor404) | Zone not found

#### get_zone_records.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**GetRecordsResponse**](../../models/GetRecordsResponse.md) |  | 


#### get_zone_records.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorsResponse**](../../models/ErrorsResponse.md) |  | 


#### get_zone_records.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **post_zone_record**
<a id="post_zone_record"></a>
> PostOrPutRecordResponse post_zone_record(zone_id)

Create a new Intelligent DNS zone record

### Example

* Api Key Authentication (tokenAuth):
```python
import idns
from idns.apis.tags import records_api
from idns.model.error_response import ErrorResponse
from idns.model.record_post_or_put import RecordPostOrPut
from idns.model.errors_response import ErrorsResponse
from idns.model.post_or_put_record_response import PostOrPutRecordResponse
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
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'
# Enter a context with an instance of the API client
with idns.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = records_api.RecordsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'zone_id': 1,
    }
    try:
        # Create a new Intelligent DNS zone record
        api_response = api_instance.post_zone_record(
            path_params=path_params,
        )
        pprint(api_response)
    except idns.ApiException as e:
        print("Exception when calling RecordsApi->post_zone_record: %s\n" % e)

    # example passing only optional values
    path_params = {
        'zone_id': 1,
    }
    body = RecordPostOrPut(
        id=1,
        entry="entry_example",
        description="description_example",
        answers_list=[
            "answers_list_example"
        ],
        policy="policy_example",
        weight=1,
        record_type="record_type_example",
        ttl=1,
    )
    try:
        # Create a new Intelligent DNS zone record
        api_response = api_instance.post_zone_record(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except idns.ApiException as e:
        print("Exception when calling RecordsApi->post_zone_record: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RecordPostOrPut**](../../models/RecordPostOrPut.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
zone_id | ZoneIdSchema | | 

# ZoneIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#post_zone_record.ApiResponseFor201) | Record added
400 | [ApiResponseFor400](#post_zone_record.ApiResponseFor400) | Error
404 | [ApiResponseFor404](#post_zone_record.ApiResponseFor404) | Zone not found

#### post_zone_record.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**PostOrPutRecordResponse**](../../models/PostOrPutRecordResponse.md) |  | 


#### post_zone_record.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorsResponse**](../../models/ErrorsResponse.md) |  | 


#### post_zone_record.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **put_zone_record**
<a id="put_zone_record"></a>
> PostOrPutRecordResponse put_zone_record(zone_idrecord_id)

Update an Intelligent DNS zone record

### Example

* Api Key Authentication (tokenAuth):
```python
import idns
from idns.apis.tags import records_api
from idns.model.error_response import ErrorResponse
from idns.model.record_post_or_put import RecordPostOrPut
from idns.model.errors_response import ErrorsResponse
from idns.model.post_or_put_record_response import PostOrPutRecordResponse
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
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'
# Enter a context with an instance of the API client
with idns.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = records_api.RecordsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'zone_id': 1,
        'record_id': 1,
    }
    try:
        # Update an Intelligent DNS zone record
        api_response = api_instance.put_zone_record(
            path_params=path_params,
        )
        pprint(api_response)
    except idns.ApiException as e:
        print("Exception when calling RecordsApi->put_zone_record: %s\n" % e)

    # example passing only optional values
    path_params = {
        'zone_id': 1,
        'record_id': 1,
    }
    body = RecordPostOrPut(
        id=1,
        entry="entry_example",
        description="description_example",
        answers_list=[
            "answers_list_example"
        ],
        policy="policy_example",
        weight=1,
        record_type="record_type_example",
        ttl=1,
    )
    try:
        # Update an Intelligent DNS zone record
        api_response = api_instance.put_zone_record(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except idns.ApiException as e:
        print("Exception when calling RecordsApi->put_zone_record: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RecordPostOrPut**](../../models/RecordPostOrPut.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
zone_id | ZoneIdSchema | | 
record_id | RecordIdSchema | | 

# ZoneIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RecordIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#put_zone_record.ApiResponseFor200) | Record updated
400 | [ApiResponseFor400](#put_zone_record.ApiResponseFor400) | Record update error
404 | [ApiResponseFor404](#put_zone_record.ApiResponseFor404) | Record not found

#### put_zone_record.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**PostOrPutRecordResponse**](../../models/PostOrPutRecordResponse.md) |  | 


#### put_zone_record.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorsResponse**](../../models/ErrorsResponse.md) |  | 


#### put_zone_record.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

