<a id="__pageTop"></a>
# digital_certificates.apis.tags.retrieve_digital_certificate_list_api.RetrieveDigitalCertificateListApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_digital_certificates**](#list_digital_certificates) | **get** /digital_certificates | List all existing digital certificates and CSRs registered to your account

# **list_digital_certificates**
<a id="list_digital_certificates"></a>
> DC200List list_digital_certificates()

List all existing digital certificates and CSRs registered to your account

### Example

* Api Key Authentication (tokenAuth):
```python
import digital_certificates
from digital_certificates.apis.tags import retrieve_digital_certificate_list_api
from digital_certificates.model.dc400 import DC400
from digital_certificates.model.dc401 import DC401
from digital_certificates.model.dc403 import DC403
from digital_certificates.model.dc404 import DC404
from digital_certificates.model.dc200_list import DC200List
from digital_certificates.model.dc406 import DC406
from pprint import pprint
# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = digital_certificates.Configuration(
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
with digital_certificates.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = retrieve_digital_certificate_list_api.RetrieveDigitalCertificateListApi(api_client)

    # example passing only optional values
    query_params = {
        'order_by': "id",
        'sort': "asc",
        'name': "name_example",
        'search': "search_example",
    }
    try:
        # List all existing digital certificates and CSRs registered to your account
        api_response = api_instance.list_digital_certificates(
            query_params=query_params,
        )
        pprint(api_response)
    except digital_certificates.ApiException as e:
        print("Exception when calling RetrieveDigitalCertificateListApi->list_digital_certificates: %s\n" % e)
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
order_by | OrderBySchema | | optional
sort | SortSchema | | optional
name | NameSchema | | optional
search | SearchSchema | | optional


# OrderBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["name", "id", ] if omitted the server will use the default value of "id"

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["asc", "desc", ] if omitted the server will use the default value of "asc"

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SearchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_digital_certificates.ApiResponseFor200) | Successful operation
400 | [ApiResponseFor400](#list_digital_certificates.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#list_digital_certificates.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#list_digital_certificates.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#list_digital_certificates.ApiResponseFor404) | Not Found
406 | [ApiResponseFor406](#list_digital_certificates.ApiResponseFor406) | Not acceptable

#### list_digital_certificates.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**DC200List**](../../models/DC200List.md) |  | 


#### list_digital_certificates.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**DC400**](../../models/DC400.md) |  | 


#### list_digital_certificates.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**DC401**](../../models/DC401.md) |  | 


#### list_digital_certificates.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**DC403**](../../models/DC403.md) |  | 


#### list_digital_certificates.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**DC404**](../../models/DC404.md) |  | 


#### list_digital_certificates.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor406ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor406ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**DC406**](../../models/DC406.md) |  | 


### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

