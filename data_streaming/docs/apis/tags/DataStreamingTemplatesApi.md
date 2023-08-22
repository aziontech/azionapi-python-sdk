<a id="__pageTop"></a>
# data_streaming.apis.tags.data_streaming_templates_api.DataStreamingTemplatesApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data_straming_template_by_id**](#get_data_straming_template_by_id) | **get** /data_streaming/templates/{template_id} | Get an global Template info by template ID
[**list_data_streaming_templates**](#list_data_streaming_templates) | **get** /data_streaming/templates | List all global Templates that can be used on Data Streaming operations

# **get_data_straming_template_by_id**
<a id="get_data_straming_template_by_id"></a>
> TemplateResultById get_data_straming_template_by_id(template_id)

Get an global Template info by template ID

Use the GET method and add the data streaming's ID to the URI of the request to get more data on a specific data streaming global template.

### Example

* Api Key Authentication (tokenAuth):
```python
import data_streaming
from data_streaming.apis.tags import data_streaming_templates_api
from data_streaming.model.template_result_by_id import TemplateResultById
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
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'
# Enter a context with an instance of the API client
with data_streaming.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_streaming_templates_api.DataStreamingTemplatesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'template_id': 1,
    }
    try:
        # Get an global Template info by template ID
        api_response = api_instance.get_data_straming_template_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except data_streaming.ApiException as e:
        print("Exception when calling DataStreamingTemplatesApi->get_data_straming_template_by_id: %s\n" % e)
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
template_id | TemplateIdSchema | | 

# TemplateIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_data_straming_template_by_id.ApiResponseFor200) | Successful operation
400 | [ApiResponseFor400](#get_data_straming_template_by_id.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_data_straming_template_by_id.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_data_straming_template_by_id.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_data_straming_template_by_id.ApiResponseFor404) | Not Found
429 | [ApiResponseFor429](#get_data_straming_template_by_id.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#get_data_straming_template_by_id.ApiResponseFor500) | Internal Server Error

#### get_data_straming_template_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TemplateResultById**](../../models/TemplateResultById.md) |  | 


#### get_data_straming_template_by_id.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_data_straming_template_by_id.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_data_straming_template_by_id.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_data_straming_template_by_id.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_data_straming_template_by_id.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_data_straming_template_by_id.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_data_streaming_templates**
<a id="list_data_streaming_templates"></a>
> TemplateResults list_data_streaming_templates()

List all global Templates that can be used on Data Streaming operations

Use the GET method to list all global templates that can be used on Data Streaming operations.  **Note:** Customized templates won't be listed. 

### Example

* Api Key Authentication (tokenAuth):
```python
import data_streaming
from data_streaming.apis.tags import data_streaming_templates_api
from data_streaming.model.template_results import TemplateResults
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
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'
# Enter a context with an instance of the API client
with data_streaming.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_streaming_templates_api.DataStreamingTemplatesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all global Templates that can be used on Data Streaming operations
        api_response = api_instance.list_data_streaming_templates()
        pprint(api_response)
    except data_streaming.ApiException as e:
        print("Exception when calling DataStreamingTemplatesApi->list_data_streaming_templates: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_data_streaming_templates.ApiResponseFor200) | Successful operation
400 | [ApiResponseFor400](#list_data_streaming_templates.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#list_data_streaming_templates.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#list_data_streaming_templates.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_data_streaming_templates.ApiResponseFor404) | Not Found
406 | [ApiResponseFor406](#list_data_streaming_templates.ApiResponseFor406) | Not Acceptable
429 | [ApiResponseFor429](#list_data_streaming_templates.ApiResponseFor429) | Too Many Requests
500 | [ApiResponseFor500](#list_data_streaming_templates.ApiResponseFor500) | Internal Server Error

#### list_data_streaming_templates.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TemplateResults**](../../models/TemplateResults.md) |  | 


#### list_data_streaming_templates.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_data_streaming_templates.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_data_streaming_templates.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_data_streaming_templates.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_data_streaming_templates.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_data_streaming_templates.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### list_data_streaming_templates.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

