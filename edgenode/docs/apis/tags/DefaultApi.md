<a id="__pageTop"></a>
# edgenode.apis.tags.default_api.DefaultApi

All URIs are relative to *http://localhost:3001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_edge_node**](#authorize_edge_node) | **patch** /edge_nodes/authorize | Authorize edge-node
[**create_edge_node_svcs**](#create_edge_node_svcs) | **post** /edge_nodes/{edgenodeId}/services | Create an edge-node Service association
[**del_edge_node**](#del_edge_node) | **delete** /edge_nodes/{edgenodeId} | Delete edge-node by ID
[**del_edge_node_svc**](#del_edge_node_svc) | **delete** /edge_nodes/{edgenodeId}/services/{bindId} | Delete an edge-node Service association
[**get_edge_node**](#get_edge_node) | **get** /edge_nodes/{edgenodeId} | Return edge-node by ID
[**get_edge_node_groups**](#get_edge_node_groups) | **get** /edge_nodes/groups | Return edge-node groups
[**get_edge_node_svc_detail**](#get_edge_node_svc_detail) | **get** /edge_nodes/{edgenodeId}/services/{bindId} | Return edge-node Service association by ID
[**get_edge_node_svcs**](#get_edge_node_svcs) | **get** /edge_nodes/{edgenodeId}/services | Return edge-node Services association
[**get_edge_nodes**](#get_edge_nodes) | **get** /edge_nodes | Return edge-nodes
[**update_edge_node**](#update_edge_node) | **patch** /edge_nodes/{edgenodeId} | Update edge-node
[**update_edge_node_svc_detail**](#update_edge_node_svc_detail) | **patch** /edge_nodes/{edgenodeId}/services/{bindId} | Update edge-node Service association by ID

# **authorize_edge_node**
<a id="authorize_edge_node"></a>
> AuthorizeEdgeNodesResponse authorize_edge_node(authorize_edge_nodes_request)

Authorize edge-node

### Example

* Api Key Authentication (tokenAuth):
```python
import edgenode
from edgenode.apis.tags import default_api
from edgenode.model.authorize_edge_nodes_response import AuthorizeEdgeNodesResponse
from edgenode.model.authorize_edge_nodes_request import AuthorizeEdgeNodesRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = edgenode.Configuration(
    host = "http://localhost:3001"
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
with edgenode.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    body = AuthorizeEdgeNodesRequest(
        edge_node_ids=[
            1
        ],
    )
    try:
        # Authorize edge-node
        api_response = api_instance.authorize_edge_node(
            body=body,
        )
        pprint(api_response)
    except edgenode.ApiException as e:
        print("Exception when calling DefaultApi->authorize_edge_node: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonVersion3] | required |
content_type | str | optional, default is 'application/json; version&#x3D;3' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthorizeEdgeNodesRequest**](../../models/AuthorizeEdgeNodesRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#authorize_edge_node.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#authorize_edge_node.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#authorize_edge_node.ApiResponseFor422) | Unprocessable Entity

#### authorize_edge_node.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthorizeEdgeNodesResponse**](../../models/AuthorizeEdgeNodesResponse.md) |  | 


#### authorize_edge_node.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### authorize_edge_node.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_edge_node_svcs**
<a id="create_edge_node_svcs"></a>
> ServiceBindDetailResponse create_edge_node_svcs(edgenode_idservice_bind_request)

Create an edge-node Service association

### Example

* Api Key Authentication (tokenAuth):
```python
import edgenode
from edgenode.apis.tags import default_api
from edgenode.model.service_bind_request import ServiceBindRequest
from edgenode.model.service_bind_detail_response import ServiceBindDetailResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = edgenode.Configuration(
    host = "http://localhost:3001"
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
with edgenode.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edgenodeId': 1,
    }
    body = ServiceBindRequest(
        service_id=1,
        variables=[
            Variable(
                name="name_example",
                value="value_example",
            )
        ],
    )
    try:
        # Create an edge-node Service association
        api_response = api_instance.create_edge_node_svcs(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except edgenode.ApiException as e:
        print("Exception when calling DefaultApi->create_edge_node_svcs: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonVersion3] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json; version&#x3D;3' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**ServiceBindRequest**](../../models/ServiceBindRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
edgenodeId | EdgenodeIdSchema | | 

# EdgenodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_edge_node_svcs.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_edge_node_svcs.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#create_edge_node_svcs.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_edge_node_svcs.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#create_edge_node_svcs.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#create_edge_node_svcs.ApiResponseFor500) | Internal Server Error

#### create_edge_node_svcs.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**ServiceBindDetailResponse**](../../models/ServiceBindDetailResponse.md) |  | 


#### create_edge_node_svcs.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_edge_node_svcs.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_edge_node_svcs.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_edge_node_svcs.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_edge_node_svcs.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **del_edge_node**
<a id="del_edge_node"></a>
> del_edge_node(edgenode_id)

Delete edge-node by ID

### Example

* Api Key Authentication (tokenAuth):
```python
import edgenode
from edgenode.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = edgenode.Configuration(
    host = "http://localhost:3001"
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
with edgenode.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edgenodeId': 1,
    }
    try:
        # Delete edge-node by ID
        api_response = api_instance.del_edge_node(
            path_params=path_params,
        )
    except edgenode.ApiException as e:
        print("Exception when calling DefaultApi->del_edge_node: %s\n" % e)
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
edgenodeId | EdgenodeIdSchema | | 

# EdgenodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#del_edge_node.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#del_edge_node.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#del_edge_node.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#del_edge_node.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#del_edge_node.ApiResponseFor500) | Internal Server Error

#### del_edge_node.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### del_edge_node.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### del_edge_node.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### del_edge_node.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### del_edge_node.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **del_edge_node_svc**
<a id="del_edge_node_svc"></a>
> del_edge_node_svc(edgenode_idbind_id)

Delete an edge-node Service association

### Example

* Api Key Authentication (tokenAuth):
```python
import edgenode
from edgenode.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = edgenode.Configuration(
    host = "http://localhost:3001"
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
with edgenode.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edgenodeId': 1,
        'bindId': 1,
    }
    try:
        # Delete an edge-node Service association
        api_response = api_instance.del_edge_node_svc(
            path_params=path_params,
        )
    except edgenode.ApiException as e:
        print("Exception when calling DefaultApi->del_edge_node_svc: %s\n" % e)
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
edgenodeId | EdgenodeIdSchema | | 
bindId | BindIdSchema | | 

# EdgenodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# BindIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#del_edge_node_svc.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#del_edge_node_svc.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#del_edge_node_svc.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#del_edge_node_svc.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#del_edge_node_svc.ApiResponseFor500) | Internal Server Error

#### del_edge_node_svc.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### del_edge_node_svc.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### del_edge_node_svc.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### del_edge_node_svc.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### del_edge_node_svc.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_edge_node**
<a id="get_edge_node"></a>
> EdgeNodeDetailResponse get_edge_node(edgenode_id)

Return edge-node by ID

### Example

* Api Key Authentication (tokenAuth):
```python
import edgenode
from edgenode.apis.tags import default_api
from edgenode.model.edge_node_detail_response import EdgeNodeDetailResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = edgenode.Configuration(
    host = "http://localhost:3001"
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
with edgenode.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edgenodeId': 1,
    }
    try:
        # Return edge-node by ID
        api_response = api_instance.get_edge_node(
            path_params=path_params,
        )
        pprint(api_response)
    except edgenode.ApiException as e:
        print("Exception when calling DefaultApi->get_edge_node: %s\n" % e)
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
edgenodeId | EdgenodeIdSchema | | 

# EdgenodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_edge_node.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_edge_node.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#get_edge_node.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_edge_node.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#get_edge_node.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#get_edge_node.ApiResponseFor500) | Internal Server Error

#### get_edge_node.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**EdgeNodeDetailResponse**](../../models/EdgeNodeDetailResponse.md) |  | 


#### get_edge_node.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_edge_node.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_edge_node.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_edge_node.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_edge_node.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_edge_node_groups**
<a id="get_edge_node_groups"></a>
> [NodeGroupResponse] get_edge_node_groups()

Return edge-node groups

### Example

* Api Key Authentication (tokenAuth):
```python
import edgenode
from edgenode.apis.tags import default_api
from edgenode.model.node_group_response import NodeGroupResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = edgenode.Configuration(
    host = "http://localhost:3001"
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
with edgenode.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Return edge-node groups
        api_response = api_instance.get_edge_node_groups()
        pprint(api_response)
    except edgenode.ApiException as e:
        print("Exception when calling DefaultApi->get_edge_node_groups: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_edge_node_groups.ApiResponseFor200) | OK
500 | [ApiResponseFor500](#get_edge_node_groups.ApiResponseFor500) | Internal Server Error

#### get_edge_node_groups.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NodeGroupResponse**]({{complexTypePrefix}}NodeGroupResponse.md) | [**NodeGroupResponse**]({{complexTypePrefix}}NodeGroupResponse.md) | [**NodeGroupResponse**]({{complexTypePrefix}}NodeGroupResponse.md) |  | 

#### get_edge_node_groups.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_edge_node_svc_detail**
<a id="get_edge_node_svc_detail"></a>
> ServiceBindDetailResponse get_edge_node_svc_detail(edgenode_idbind_id)

Return edge-node Service association by ID

### Example

* Api Key Authentication (tokenAuth):
```python
import edgenode
from edgenode.apis.tags import default_api
from edgenode.model.service_bind_detail_response import ServiceBindDetailResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = edgenode.Configuration(
    host = "http://localhost:3001"
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
with edgenode.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edgenodeId': 1,
        'bindId': 1,
    }
    try:
        # Return edge-node Service association by ID
        api_response = api_instance.get_edge_node_svc_detail(
            path_params=path_params,
        )
        pprint(api_response)
    except edgenode.ApiException as e:
        print("Exception when calling DefaultApi->get_edge_node_svc_detail: %s\n" % e)
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
edgenodeId | EdgenodeIdSchema | | 
bindId | BindIdSchema | | 

# EdgenodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# BindIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_edge_node_svc_detail.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_edge_node_svc_detail.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#get_edge_node_svc_detail.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_edge_node_svc_detail.ApiResponseFor500) | Internal Server Error

#### get_edge_node_svc_detail.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**ServiceBindDetailResponse**](../../models/ServiceBindDetailResponse.md) |  | 


#### get_edge_node_svc_detail.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_edge_node_svc_detail.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_edge_node_svc_detail.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_edge_node_svcs**
<a id="get_edge_node_svcs"></a>
> ServiceResponseWithTotal get_edge_node_svcs(edgenode_id)

Return edge-node Services association

### Example

* Api Key Authentication (tokenAuth):
```python
import edgenode
from edgenode.apis.tags import default_api
from edgenode.model.service_response_with_total import ServiceResponseWithTotal
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = edgenode.Configuration(
    host = "http://localhost:3001"
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
with edgenode.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edgenodeId': 1,
    }
    query_params = {
    }
    try:
        # Return edge-node Services association
        api_response = api_instance.get_edge_node_svcs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except edgenode.ApiException as e:
        print("Exception when calling DefaultApi->get_edge_node_svcs: %s\n" % e)

    # example passing only optional values
    path_params = {
        'edgenodeId': 1,
    }
    query_params = {
        'is_bound': True,
        'filter': "filter_example",
        'order_by': "order_by_example",
        'sort': "sort_example",
        'page': 1,
        'page_size': 1,
    }
    try:
        # Return edge-node Services association
        api_response = api_instance.get_edge_node_svcs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except edgenode.ApiException as e:
        print("Exception when calling DefaultApi->get_edge_node_svcs: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
is_bound | IsBoundSchema | | optional
filter | FilterSchema | | optional
order_by | OrderBySchema | | optional
sort | SortSchema | | optional
page | PageSchema | | optional
page_size | PageSizeSchema | | optional


# IsBoundSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# FilterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrderBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
edgenodeId | EdgenodeIdSchema | | 

# EdgenodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_edge_node_svcs.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_edge_node_svcs.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#get_edge_node_svcs.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#get_edge_node_svcs.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#get_edge_node_svcs.ApiResponseFor500) | Internal Server Error

#### get_edge_node_svcs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**ServiceResponseWithTotal**](../../models/ServiceResponseWithTotal.md) |  | 


#### get_edge_node_svcs.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_edge_node_svcs.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_edge_node_svcs.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_edge_node_svcs.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_edge_nodes**
<a id="get_edge_nodes"></a>
> EdgeNodeResponseWithTotal get_edge_nodes()

Return edge-nodes

### Example

* Api Key Authentication (tokenAuth):
```python
import edgenode
from edgenode.apis.tags import default_api
from edgenode.model.edge_node_response_with_total import EdgeNodeResponseWithTotal
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = edgenode.Configuration(
    host = "http://localhost:3001"
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
with edgenode.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only optional values
    query_params = {
        'filter': "filter_example",
        'order_by': "order_by_example",
        'sort': "sort_example",
        'only_ids': True,
        'page_size': 1,
    }
    try:
        # Return edge-nodes
        api_response = api_instance.get_edge_nodes(
            query_params=query_params,
        )
        pprint(api_response)
    except edgenode.ApiException as e:
        print("Exception when calling DefaultApi->get_edge_nodes: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
filter | FilterSchema | | optional
order_by | OrderBySchema | | optional
sort | SortSchema | | optional
only_ids | OnlyIdsSchema | | optional
page_size | PageSizeSchema | | optional


# FilterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrderBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OnlyIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_edge_nodes.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_edge_nodes.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#get_edge_nodes.ApiResponseFor500) | Internal Server Error

#### get_edge_nodes.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**EdgeNodeResponseWithTotal**](../../models/EdgeNodeResponseWithTotal.md) |  | 


#### get_edge_nodes.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_edge_nodes.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_edge_node**
<a id="update_edge_node"></a>
> UpdateEdgeNodeResponse update_edge_node(edgenode_id)

Update edge-node

### Example

* Api Key Authentication (tokenAuth):
```python
import edgenode
from edgenode.apis.tags import default_api
from edgenode.model.update_edge_node_response import UpdateEdgeNodeResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = edgenode.Configuration(
    host = "http://localhost:3001"
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
with edgenode.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edgenodeId': 1,
    }
    try:
        # Update edge-node
        api_response = api_instance.update_edge_node(
            path_params=path_params,
        )
        pprint(api_response)
    except edgenode.ApiException as e:
        print("Exception when calling DefaultApi->update_edge_node: %s\n" % e)
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
edgenodeId | EdgenodeIdSchema | | 

# EdgenodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_edge_node.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#update_edge_node.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#update_edge_node.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_edge_node.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#update_edge_node.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#update_edge_node.ApiResponseFor500) | Internal Server Error

#### update_edge_node.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateEdgeNodeResponse**](../../models/UpdateEdgeNodeResponse.md) |  | 


#### update_edge_node.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_edge_node.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_edge_node.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_edge_node.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_edge_node.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_edge_node_svc_detail**
<a id="update_edge_node_svc_detail"></a>
> ServiceBindDetailResponse update_edge_node_svc_detail(edgenode_idbind_idupdate_service_bind_request)

Update edge-node Service association by ID

### Example

* Api Key Authentication (tokenAuth):
```python
import edgenode
from edgenode.apis.tags import default_api
from edgenode.model.update_service_bind_request import UpdateServiceBindRequest
from edgenode.model.service_bind_detail_response import ServiceBindDetailResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3001
# See configuration.py for a list of all supported configuration parameters.
configuration = edgenode.Configuration(
    host = "http://localhost:3001"
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
with edgenode.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edgenodeId': 1,
        'bindId': 1,
    }
    body = UpdateServiceBindRequest(
        variables=[
            Variable(
                name="name_example",
                value="value_example",
            )
        ],
    )
    try:
        # Update edge-node Service association by ID
        api_response = api_instance.update_edge_node_svc_detail(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except edgenode.ApiException as e:
        print("Exception when calling DefaultApi->update_edge_node_svc_detail: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonVersion3] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json; version&#x3D;3' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateServiceBindRequest**](../../models/UpdateServiceBindRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
edgenodeId | EdgenodeIdSchema | | 
bindId | BindIdSchema | | 

# EdgenodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# BindIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_edge_node_svc_detail.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#update_edge_node_svc_detail.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#update_edge_node_svc_detail.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_edge_node_svc_detail.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#update_edge_node_svc_detail.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#update_edge_node_svc_detail.ApiResponseFor500) | Internal Server Error

#### update_edge_node_svc_detail.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**ServiceBindDetailResponse**](../../models/ServiceBindDetailResponse.md) |  | 


#### update_edge_node_svc_detail.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_edge_node_svc_detail.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_edge_node_svc_detail.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_edge_node_svc_detail.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_edge_node_svc_detail.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

