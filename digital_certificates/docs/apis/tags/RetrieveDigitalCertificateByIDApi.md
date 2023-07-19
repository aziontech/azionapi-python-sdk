<a id="__pageTop"></a>
# digital_certificates.apis.tags.retrieve_digital_certificate_by_id_api.RetrieveDigitalCertificateByIDApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_certificate**](#get_certificate) | **get** /digital_certificates/{digital_certificate_id} | Get more data on a specific digital certificate or CSR.

# **get_certificate**
<a id="get_certificate"></a>
> DC200 get_certificate(digital_certificate_id)

Get more data on a specific digital certificate or CSR.

### Example

* Api Key Authentication (tokenAuth):
```python
import digital_certificates
from digital_certificates.apis.tags import retrieve_digital_certificate_by_id_api
from digital_certificates.model.dc400 import DC400
from digital_certificates.model.dc401 import DC401
from digital_certificates.model.dc200 import DC200
from digital_certificates.model.dc403 import DC403
from digital_certificates.model.dc404 import DC404
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
    api_instance = retrieve_digital_certificate_by_id_api.RetrieveDigitalCertificateByIDApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'digital_certificate_id': 1,
    }
    try:
        # Get more data on a specific digital certificate or CSR.
        api_response = api_instance.get_certificate(
            path_params=path_params,
        )
        pprint(api_response)
    except digital_certificates.ApiException as e:
        print("Exception when calling RetrieveDigitalCertificateByIDApi->get_certificate: %s\n" % e)
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
digital_certificate_id | DigitalCertificateIdSchema | | 

# DigitalCertificateIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_certificate.ApiResponseFor200) | Successful operation
400 | [ApiResponseFor400](#get_certificate.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#get_certificate.ApiResponseFor401) | Unauthorized operation
403 | [ApiResponseFor403](#get_certificate.ApiResponseFor403) | Forbidden operation
404 | [ApiResponseFor404](#get_certificate.ApiResponseFor404) | Data not found
406 | [ApiResponseFor406](#get_certificate.ApiResponseFor406) | Not Acceptable

#### get_certificate.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**DC200**](../../models/DC200.md) |  | 


#### get_certificate.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**DC400**](../../models/DC400.md) |  | 


#### get_certificate.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**DC401**](../../models/DC401.md) |  | 


#### get_certificate.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**DC403**](../../models/DC403.md) |  | 


#### get_certificate.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**DC404**](../../models/DC404.md) |  | 


#### get_certificate.ApiResponseFor406
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

