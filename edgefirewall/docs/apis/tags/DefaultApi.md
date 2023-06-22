<a id="__pageTop"></a>
# edgefirewall.apis.tags.default_api.DefaultApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edge_firewall_get**](#edge_firewall_get) | **get** /edge_firewall | List all user edge firewall
[**edge_firewall_post**](#edge_firewall_post) | **post** /edge_firewall | Create a edge firewall
[**edge_firewall_uuid_delete**](#edge_firewall_uuid_delete) | **delete** /edge_firewall/{uuid} | Delete an edge firewall by uuid
[**edge_firewall_uuid_get**](#edge_firewall_uuid_get) | **get** /edge_firewall/{uuid} | Retrieve an edge firewall set by uuid
[**edge_firewall_uuid_patch**](#edge_firewall_uuid_patch) | **patch** /edge_firewall/{uuid} | Update some edge firewall attributes, like \&quot;active\&quot;
[**edge_firewall_uuid_put**](#edge_firewall_uuid_put) | **put** /edge_firewall/{uuid} | Overwrite some edge firewall attributes, like \&quot;active\&quot;

# **edge_firewall_get**
<a id="edge_firewall_get"></a>
> ListEdgeFirewallResponse edge_firewall_get()

List all user edge firewall

### Example

* Api Key Authentication (tokenAuth):
```python
import edgefirewall
from edgefirewall.apis.tags import default_api
from edgefirewall.model.list_edge_firewall_response import ListEdgeFirewallResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefirewall.Configuration(
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
with edgefirewall.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only optional values
    query_params = {
        'page': 1,
        'page_size': 1,
        'sort': "sort_example",
        'order_by': "order_by_example",
    }
    try:
        # List all user edge firewall
        api_response = api_instance.edge_firewall_get(
            query_params=query_params,
        )
        pprint(api_response)
    except edgefirewall.ApiException as e:
        print("Exception when calling DefaultApi->edge_firewall_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page | PageSchema | | optional
page_size | PageSizeSchema | | optional
sort | SortSchema | | optional
order_by | OrderBySchema | | optional


# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrderBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edge_firewall_get.ApiResponseFor200) | A list of edge firewalls

#### edge_firewall_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListEdgeFirewallResponse**](../../models/ListEdgeFirewallResponse.md) |  | 


### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edge_firewall_post**
<a id="edge_firewall_post"></a>
> edge_firewall_post(create_edge_firewall_request)

Create a edge firewall

### Example

* Api Key Authentication (tokenAuth):
```python
import edgefirewall
from edgefirewall.apis.tags import default_api
from edgefirewall.model.create_edge_firewall_request import CreateEdgeFirewallRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefirewall.Configuration(
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
with edgefirewall.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    body = CreateEdgeFirewallRequest(
        name="name_example",
        domains=[
            1
        ],
        is_active=True,
        edge_functions_enabled=True,
        network_protection_enabled=True,
        waf_enabled=True,
    )
    try:
        # Create a edge firewall
        api_response = api_instance.edge_firewall_post(
            body=body,
        )
    except edgefirewall.ApiException as e:
        print("Exception when calling DefaultApi->edge_firewall_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateEdgeFirewallRequest**](../../models/CreateEdgeFirewallRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#edge_firewall_post.ApiResponseFor201) | Edge firewall created
400 | [ApiResponseFor400](#edge_firewall_post.ApiResponseFor400) | Internal Server Error
500 | [ApiResponseFor500](#edge_firewall_post.ApiResponseFor500) | Internal Server Error

#### edge_firewall_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_firewall_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_firewall_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edge_firewall_uuid_delete**
<a id="edge_firewall_uuid_delete"></a>
> edge_firewall_uuid_delete(uuid)

Delete an edge firewall by uuid

### Example

* Api Key Authentication (tokenAuth):
```python
import edgefirewall
from edgefirewall.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefirewall.Configuration(
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
with edgefirewall.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'uuid': "uuid_example",
    }
    try:
        # Delete an edge firewall by uuid
        api_response = api_instance.edge_firewall_uuid_delete(
            path_params=path_params,
        )
    except edgefirewall.ApiException as e:
        print("Exception when calling DefaultApi->edge_firewall_uuid_delete: %s\n" % e)
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
uuid | UuidSchema | | 

# UuidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#edge_firewall_uuid_delete.ApiResponseFor204) | Successfully deleted

#### edge_firewall_uuid_delete.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edge_firewall_uuid_get**
<a id="edge_firewall_uuid_get"></a>
> EdgeFirewallResponse edge_firewall_uuid_get(uuid)

Retrieve an edge firewall set by uuid

### Example

* Api Key Authentication (tokenAuth):
```python
import edgefirewall
from edgefirewall.apis.tags import default_api
from edgefirewall.model.edge_firewall_response import EdgeFirewallResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefirewall.Configuration(
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
with edgefirewall.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'uuid': "uuid_example",
    }
    try:
        # Retrieve an edge firewall set by uuid
        api_response = api_instance.edge_firewall_uuid_get(
            path_params=path_params,
        )
        pprint(api_response)
    except edgefirewall.ApiException as e:
        print("Exception when calling DefaultApi->edge_firewall_uuid_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
uuid | UuidSchema | | 

# UuidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edge_firewall_uuid_get.ApiResponseFor200) | An edge firewall object

#### edge_firewall_uuid_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EdgeFirewallResponse**](../../models/EdgeFirewallResponse.md) |  | 


### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edge_firewall_uuid_patch**
<a id="edge_firewall_uuid_patch"></a>
> ListEdgeFirewallResponse edge_firewall_uuid_patch(uuidbody)

Update some edge firewall attributes, like \"active\"

### Example

* Api Key Authentication (tokenAuth):
```python
import edgefirewall
from edgefirewall.apis.tags import default_api
from edgefirewall.model.list_edge_firewall_response import ListEdgeFirewallResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefirewall.Configuration(
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
with edgefirewall.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'uuid': "uuid_example",
    }
    body = ListEdgeFirewallResponse(
        count=1,
        total_pages=1,
        schema_version=1,
        links=Links(
            previous="previous_example",
            next="next_example",
        ),
        results=[
            EdgeFirewall(
                id=1,
                name="name_example",
                is_active=True,
                last_editor="last_editor_example",
                last_modified="last_modified_example",
                edge_functions_enabled=True,
                network_protection_enabled=True,
                waf_enabled=True,
                debug_rules=True,
                domains=[
                    1
                ],
            )
        ],
    )
    try:
        # Update some edge firewall attributes, like \"active\"
        api_response = api_instance.edge_firewall_uuid_patch(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except edgefirewall.ApiException as e:
        print("Exception when calling DefaultApi->edge_firewall_uuid_patch: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListEdgeFirewallResponse**](../../models/ListEdgeFirewallResponse.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
uuid | UuidSchema | | 

# UuidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edge_firewall_uuid_patch.ApiResponseFor200) | Successfully updated
400 | [ApiResponseFor400](#edge_firewall_uuid_patch.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#edge_firewall_uuid_patch.ApiResponseFor500) | Internal Server Error

#### edge_firewall_uuid_patch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListEdgeFirewallResponse**](../../models/ListEdgeFirewallResponse.md) |  | 


#### edge_firewall_uuid_patch.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_firewall_uuid_patch.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edge_firewall_uuid_put**
<a id="edge_firewall_uuid_put"></a>
> ListEdgeFirewallResponse edge_firewall_uuid_put(uuidbody)

Overwrite some edge firewall attributes, like \"active\"

### Example

* Api Key Authentication (tokenAuth):
```python
import edgefirewall
from edgefirewall.apis.tags import default_api
from edgefirewall.model.list_edge_firewall_response import ListEdgeFirewallResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefirewall.Configuration(
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
with edgefirewall.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'uuid': "uuid_example",
    }
    body = ListEdgeFirewallResponse(
        count=1,
        total_pages=1,
        schema_version=1,
        links=Links(
            previous="previous_example",
            next="next_example",
        ),
        results=[
            EdgeFirewall(
                id=1,
                name="name_example",
                is_active=True,
                last_editor="last_editor_example",
                last_modified="last_modified_example",
                edge_functions_enabled=True,
                network_protection_enabled=True,
                waf_enabled=True,
                debug_rules=True,
                domains=[
                    1
                ],
            )
        ],
    )
    try:
        # Overwrite some edge firewall attributes, like \"active\"
        api_response = api_instance.edge_firewall_uuid_put(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except edgefirewall.ApiException as e:
        print("Exception when calling DefaultApi->edge_firewall_uuid_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListEdgeFirewallResponse**](../../models/ListEdgeFirewallResponse.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
uuid | UuidSchema | | 

# UuidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edge_firewall_uuid_put.ApiResponseFor200) | Successfully updated
400 | [ApiResponseFor400](#edge_firewall_uuid_put.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#edge_firewall_uuid_put.ApiResponseFor500) | Internal Server Error

#### edge_firewall_uuid_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListEdgeFirewallResponse**](../../models/ListEdgeFirewallResponse.md) |  | 


#### edge_firewall_uuid_put.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_firewall_uuid_put.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

