<a id="__pageTop"></a>
# edgeapplications.apis.tags.edge_applications_rules_engine_api.EdgeApplicationsRulesEngineApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edge_applications_edge_application_id_rules_engine_phase_rules_get**](#edge_applications_edge_application_id_rules_engine_phase_rules_get) | **get** /edge_applications/{edge_application_id}/rules_engine/{phase}/rules | /edge_applications/{edge_application_id}/rules_engine/{phase}/rules
[**edge_applications_edge_application_id_rules_engine_phase_rules_post**](#edge_applications_edge_application_id_rules_engine_phase_rules_post) | **post** /edge_applications/{edge_application_id}/rules_engine/{phase}/rules | /edge_applications/{edge_application_id}/rules_engine/{phase}/rules
[**edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete**](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete) | **delete** /edge_applications/{edge_application_id}/rules_engine/{phase}/rules/{rule_id} | /edge_applications/{edge_application_id}/rules_engine/{phase}/rules
[**edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get**](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get) | **get** /edge_applications/{edge_application_id}/rules_engine/{phase}/rules/{rule_id} | /edge_applications/{edge_application_id}/rules_engine/{phase}/rules
[**edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch**](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch) | **patch** /edge_applications/{edge_application_id}/rules_engine/{phase}/rules/{rule_id} | /edge_applications/:edge_application_id:/rules_engine/:phase:/rules/:rule_id:
[**edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put**](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put) | **put** /edge_applications/{edge_application_id}/rules_engine/{phase}/rules/{rule_id} | /edge_applications/:edge_application_id:/rules_engine/:phase:/rules/:rule_id:

# **edge_applications_edge_application_id_rules_engine_phase_rules_get**
<a id="edge_applications_edge_application_id_rules_engine_phase_rules_get"></a>
> RulesEngineResponse edge_applications_edge_application_id_rules_engine_phase_rules_get(edge_application_idphase)

/edge_applications/{edge_application_id}/rules_engine/{phase}/rules

### Example

* Api Key Authentication (tokenAuth):
```python
import edgeapplications
from edgeapplications.apis.tags import edge_applications_rules_engine_api
from edgeapplications.model.rules_engine_response import RulesEngineResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgeapplications.Configuration(
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
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edge_applications_rules_engine_api.EdgeApplicationsRulesEngineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edge_application_id': 1,
        'phase': "phase_example",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # /edge_applications/{edge_application_id}/rules_engine/{phase}/rules
        api_response = api_instance.edge_applications_edge_application_id_rules_engine_phase_rules_get(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsRulesEngineApi->edge_applications_edge_application_id_rules_engine_phase_rules_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'edge_application_id': 1,
        'phase': "phase_example",
    }
    query_params = {
        'page': 1,
        'page_size': 1,
        'filter': "filter_example",
        'order_by': "order_by_example",
        'sort': "sort_example",
    }
    header_params = {
        'Accept': "application/json; version=3",
    }
    try:
        # /edge_applications/{edge_application_id}/rules_engine/{phase}/rules
        api_response = api_instance.edge_applications_edge_application_id_rules_engine_phase_rules_get(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsRulesEngineApi->edge_applications_edge_application_id_rules_engine_phase_rules_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page | PageSchema | | optional
page_size | PageSizeSchema | | optional
filter | FilterSchema | | optional
order_by | OrderBySchema | | optional
sort | SortSchema | | optional


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

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Accept | AcceptSchema | | optional

# AcceptSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
edge_application_id | EdgeApplicationIdSchema | | 
phase | PhaseSchema | | 

# EdgeApplicationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# PhaseSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edge_applications_edge_application_id_rules_engine_phase_rules_get.ApiResponseFor200) | Successful response
400 | [ApiResponseFor400](#edge_applications_edge_application_id_rules_engine_phase_rules_get.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#edge_applications_edge_application_id_rules_engine_phase_rules_get.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edge_applications_edge_application_id_rules_engine_phase_rules_get.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#edge_applications_edge_application_id_rules_engine_phase_rules_get.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#edge_applications_edge_application_id_rules_engine_phase_rules_get.ApiResponseFor500) | Internal Server Error

#### edge_applications_edge_application_id_rules_engine_phase_rules_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**RulesEngineResponse**](../../models/RulesEngineResponse.md) |  | 


#### edge_applications_edge_application_id_rules_engine_phase_rules_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_rules_engine_phase_rules_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_rules_engine_phase_rules_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_rules_engine_phase_rules_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_rules_engine_phase_rules_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edge_applications_edge_application_id_rules_engine_phase_rules_post**
<a id="edge_applications_edge_application_id_rules_engine_phase_rules_post"></a>
> RulesEngineIdResponse edge_applications_edge_application_id_rules_engine_phase_rules_post(edge_application_idphase)

/edge_applications/{edge_application_id}/rules_engine/{phase}/rules

Check below the list of behaviors that can be applied:  | Name                                | Behavior               | | ----------------------------------- | ---------------------- | | Add Request Cookie                  | add_request_cookie     | | Add Request Header                  | add_request_header     | | Add Response Cookie                 | set_cookie             | | Add Response Header                 | add_response_header    | | Bypass Cache                        | bypass_cache_phase     | | Capture Match Groups                | capture_match_groups   | | Deliver                             | deliver                | | Deny (403 Forbidden)                | deny                   | | Enable Gzip                         | enable_gzip            | | Filter Request Cookie               | filter_request_cookie  | | Filter Request Header               | filter_request_header  | | Filter Response Cookie              | filter_response_cookie | | Filter Response Header              | filter_response_header | | Finish Request Phase                | finish_request_phase   | | Forward Cookies                     | forward_cookies        | | Optimize Images                     | optimize_images        | | Redirect HTTP to HTTPS              | redirect_http_to_https | | Redirect To (301 Moved Permanently) | redirect_to_301        | | Redirect To (302 Found)             | redirect_to_302        | | Rewrite Request                     | rewrite_request        | | Run Function                        | run_function           | | Set Cache Policy                    | set_cache_policy       | | Set Origin                          | set_origin             |

### Example

* Api Key Authentication (tokenAuth):
```python
import edgeapplications
from edgeapplications.apis.tags import edge_applications_rules_engine_api
from edgeapplications.model.rules_engine_id_response import RulesEngineIdResponse
from edgeapplications.model.create_rules_engine_request import CreateRulesEngineRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgeapplications.Configuration(
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
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edge_applications_rules_engine_api.EdgeApplicationsRulesEngineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edge_application_id': 1,
        'phase': "phase_example",
    }
    header_params = {
    }
    try:
        # /edge_applications/{edge_application_id}/rules_engine/{phase}/rules
        api_response = api_instance.edge_applications_edge_application_id_rules_engine_phase_rules_post(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsRulesEngineApi->edge_applications_edge_application_id_rules_engine_phase_rules_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'edge_application_id': 1,
        'phase': "phase_example",
    }
    header_params = {
        'Accept': "application/json; version=3",
        'Content-Type': "application/json",
    }
    body = CreateRulesEngineRequest(
        name="name_example",
        description="description_example",
        criteria=[
            [
                RulesEngineCriteria(
                    conditional="conditional_example",
                    variable="variable_example",
                    operator="operator_example",
                    input_value="input_value_example",
                )
            ]
        ],
        behaviors=[
            RulesEngineBehavior(
                name="name_example",
                target="target_example",
            )
        ],
    )
    try:
        # /edge_applications/{edge_application_id}/rules_engine/{phase}/rules
        api_response = api_instance.edge_applications_edge_application_id_rules_engine_phase_rules_post(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsRulesEngineApi->edge_applications_edge_application_id_rules_engine_phase_rules_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonVersion3, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
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
[**CreateRulesEngineRequest**](../../models/CreateRulesEngineRequest.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Accept | AcceptSchema | | optional
Content-Type | ContentTypeSchema | | optional

# AcceptSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
edge_application_id | EdgeApplicationIdSchema | | 
phase | PhaseSchema | | 

# EdgeApplicationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# PhaseSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edge_applications_edge_application_id_rules_engine_phase_rules_post.ApiResponseFor200) | Successful response
400 | [ApiResponseFor400](#edge_applications_edge_application_id_rules_engine_phase_rules_post.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#edge_applications_edge_application_id_rules_engine_phase_rules_post.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edge_applications_edge_application_id_rules_engine_phase_rules_post.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#edge_applications_edge_application_id_rules_engine_phase_rules_post.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#edge_applications_edge_application_id_rules_engine_phase_rules_post.ApiResponseFor500) | Internal Server Error

#### edge_applications_edge_application_id_rules_engine_phase_rules_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**RulesEngineIdResponse**](../../models/RulesEngineIdResponse.md) |  | 


#### edge_applications_edge_application_id_rules_engine_phase_rules_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_rules_engine_phase_rules_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_rules_engine_phase_rules_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_rules_engine_phase_rules_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_rules_engine_phase_rules_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete**
<a id="edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete"></a>
> edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete(edge_application_idphaserule_id)

/edge_applications/{edge_application_id}/rules_engine/{phase}/rules

### Example

* Api Key Authentication (tokenAuth):
```python
import edgeapplications
from edgeapplications.apis.tags import edge_applications_rules_engine_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgeapplications.Configuration(
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
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edge_applications_rules_engine_api.EdgeApplicationsRulesEngineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edge_application_id': 1,
        'phase': "phase_example",
        'rule_id': 1,
    }
    header_params = {
    }
    try:
        # /edge_applications/{edge_application_id}/rules_engine/{phase}/rules
        api_response = api_instance.edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete(
            path_params=path_params,
            header_params=header_params,
        )
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsRulesEngineApi->edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete: %s\n" % e)

    # example passing only optional values
    path_params = {
        'edge_application_id': 1,
        'phase': "phase_example",
        'rule_id': 1,
    }
    header_params = {
        'Accept': "application/json; version=3",
    }
    try:
        # /edge_applications/{edge_application_id}/rules_engine/{phase}/rules
        api_response = api_instance.edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete(
            path_params=path_params,
            header_params=header_params,
        )
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsRulesEngineApi->edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Accept | AcceptSchema | | optional

# AcceptSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
edge_application_id | EdgeApplicationIdSchema | | 
phase | PhaseSchema | | 
rule_id | RuleIdSchema | | 

# EdgeApplicationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# PhaseSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RuleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete.ApiResponseFor204) | No response
400 | [ApiResponseFor400](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete.ApiResponseFor500) | Internal Server Error

#### edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get**
<a id="edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get"></a>
> RulesEngineIdResponse edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get(edge_application_idphaserule_id)

/edge_applications/{edge_application_id}/rules_engine/{phase}/rules

### Example

* Api Key Authentication (tokenAuth):
```python
import edgeapplications
from edgeapplications.apis.tags import edge_applications_rules_engine_api
from edgeapplications.model.rules_engine_id_response import RulesEngineIdResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgeapplications.Configuration(
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
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edge_applications_rules_engine_api.EdgeApplicationsRulesEngineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edge_application_id': 1,
        'phase': "phase_example",
        'rule_id': 1,
    }
    header_params = {
    }
    try:
        # /edge_applications/{edge_application_id}/rules_engine/{phase}/rules
        api_response = api_instance.edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsRulesEngineApi->edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'edge_application_id': 1,
        'phase': "phase_example",
        'rule_id': 1,
    }
    header_params = {
        'Accept': "application/json; version=3",
    }
    try:
        # /edge_applications/{edge_application_id}/rules_engine/{phase}/rules
        api_response = api_instance.edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsRulesEngineApi->edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Accept | AcceptSchema | | optional

# AcceptSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
edge_application_id | EdgeApplicationIdSchema | | 
phase | PhaseSchema | | 
rule_id | RuleIdSchema | | 

# EdgeApplicationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# PhaseSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RuleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get.ApiResponseFor200) | Successful response
400 | [ApiResponseFor400](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get.ApiResponseFor500) | Internal Server Error

#### edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**RulesEngineIdResponse**](../../models/RulesEngineIdResponse.md) |  | 


#### edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch**
<a id="edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch"></a>
> RulesEngineIdResponse edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch(edge_application_idphaserule_id)

/edge_applications/:edge_application_id:/rules_engine/:phase:/rules/:rule_id:

### Example

* Api Key Authentication (tokenAuth):
```python
import edgeapplications
from edgeapplications.apis.tags import edge_applications_rules_engine_api
from edgeapplications.model.rules_engine_id_response import RulesEngineIdResponse
from edgeapplications.model.patch_rules_engine_request import PatchRulesEngineRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgeapplications.Configuration(
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
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edge_applications_rules_engine_api.EdgeApplicationsRulesEngineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edge_application_id': 1,
        'phase': "phase_example",
        'rule_id': 1,
    }
    header_params = {
    }
    try:
        # /edge_applications/:edge_application_id:/rules_engine/:phase:/rules/:rule_id:
        api_response = api_instance.edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsRulesEngineApi->edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch: %s\n" % e)

    # example passing only optional values
    path_params = {
        'edge_application_id': 1,
        'phase': "phase_example",
        'rule_id': 1,
    }
    header_params = {
        'Accept': "application/json; version=3",
        'Content-Type': "application/json",
    }
    body = PatchRulesEngineRequest(
        name="name_example",
        description="description_example",
        criteria=[
            [
                RulesEngineCriteria(
                    conditional="conditional_example",
                    variable="variable_example",
                    operator="operator_example",
                    input_value="input_value_example",
                )
            ]
        ],
        behaviors=[
            RulesEngineBehavior(
                name="name_example",
                target="target_example",
            )
        ],
    )
    try:
        # /edge_applications/:edge_application_id:/rules_engine/:phase:/rules/:rule_id:
        api_response = api_instance.edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsRulesEngineApi->edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonVersion3, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
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
[**PatchRulesEngineRequest**](../../models/PatchRulesEngineRequest.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Accept | AcceptSchema | | optional
Content-Type | ContentTypeSchema | | optional

# AcceptSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
edge_application_id | EdgeApplicationIdSchema | | 
phase | PhaseSchema | | 
rule_id | RuleIdSchema | | 

# EdgeApplicationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# PhaseSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RuleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch.ApiResponseFor200) | Successful response
400 | [ApiResponseFor400](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch.ApiResponseFor500) | Internal Server Error

#### edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**RulesEngineIdResponse**](../../models/RulesEngineIdResponse.md) |  | 


#### edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put**
<a id="edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put"></a>
> RulesEngineIdResponse edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put(edge_application_idphaserule_id)

/edge_applications/:edge_application_id:/rules_engine/:phase:/rules/:rule_id:

### Example

* Api Key Authentication (tokenAuth):
```python
import edgeapplications
from edgeapplications.apis.tags import edge_applications_rules_engine_api
from edgeapplications.model.rules_engine_id_response import RulesEngineIdResponse
from edgeapplications.model.update_rules_engine_request import UpdateRulesEngineRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgeapplications.Configuration(
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
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edge_applications_rules_engine_api.EdgeApplicationsRulesEngineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'edge_application_id': 1,
        'phase': "phase_example",
        'rule_id': 1,
    }
    header_params = {
    }
    try:
        # /edge_applications/:edge_application_id:/rules_engine/:phase:/rules/:rule_id:
        api_response = api_instance.edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsRulesEngineApi->edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put: %s\n" % e)

    # example passing only optional values
    path_params = {
        'edge_application_id': 1,
        'phase': "phase_example",
        'rule_id': 1,
    }
    header_params = {
        'Accept': "application/json; version=3",
        'Content-Type': "application/json",
    }
    body = UpdateRulesEngineRequest(
        name="name_example",
        description="description_example",
        criteria=[
            [
                RulesEngineCriteria(
                    conditional="conditional_example",
                    variable="variable_example",
                    operator="operator_example",
                    input_value="input_value_example",
                )
            ]
        ],
        behaviors=[
            RulesEngineBehavior(
                name="name_example",
                target="target_example",
            )
        ],
    )
    try:
        # /edge_applications/:edge_application_id:/rules_engine/:phase:/rules/:rule_id:
        api_response = api_instance.edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except edgeapplications.ApiException as e:
        print("Exception when calling EdgeApplicationsRulesEngineApi->edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonVersion3, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
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
[**UpdateRulesEngineRequest**](../../models/UpdateRulesEngineRequest.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Accept | AcceptSchema | | optional
Content-Type | ContentTypeSchema | | optional

# AcceptSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
edge_application_id | EdgeApplicationIdSchema | | 
phase | PhaseSchema | | 
rule_id | RuleIdSchema | | 

# EdgeApplicationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# PhaseSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RuleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put.ApiResponseFor200) | Successful response
400 | [ApiResponseFor400](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put.ApiResponseFor422) | Unprocessable Entity
500 | [ApiResponseFor500](#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put.ApiResponseFor500) | Internal Server Error

#### edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**RulesEngineIdResponse**](../../models/RulesEngineIdResponse.md) |  | 


#### edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

