<a id="__pageTop"></a>
# digital_certificates.apis.tags.delete_digital_certificate_api.DeleteDigitalCertificateApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remove_digital_certificates**](#remove_digital_certificates) | **delete** /digital_certificates/{digital_certificate_id} | Remove a digital certificate or CSR from your account

# **remove_digital_certificates**
<a id="remove_digital_certificates"></a>
> remove_digital_certificates(digital_certificate_id)

Remove a digital certificate or CSR from your account

### Example

* Api Key Authentication (tokenAuth):
```python
import digital_certificates
from digital_certificates.apis.tags import delete_digital_certificate_api
from digital_certificates.model.dc400 import DC400
from digital_certificates.model.dc409 import DC409
from digital_certificates.model.dc403 import DC403
from digital_certificates.model.dc404 import DC404
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
    api_instance = delete_digital_certificate_api.DeleteDigitalCertificateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'digital_certificate_id': 1,
    }
    try:
        # Remove a digital certificate or CSR from your account
        api_response = api_instance.remove_digital_certificates(
            path_params=path_params,
        )
    except digital_certificates.ApiException as e:
        print("Exception when calling DeleteDigitalCertificateApi->remove_digital_certificates: %s\n" % e)
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
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#remove_digital_certificates.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#remove_digital_certificates.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#remove_digital_certificates.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#remove_digital_certificates.ApiResponseFor404) | Not Found
409 | [ApiResponseFor409](#remove_digital_certificates.ApiResponseFor409) | Forbidden

#### remove_digital_certificates.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### remove_digital_certificates.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**DC400**](../../models/DC400.md) |  | 


#### remove_digital_certificates.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**DC403**](../../models/DC403.md) |  | 


#### remove_digital_certificates.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**DC404**](../../models/DC404.md) |  | 


#### remove_digital_certificates.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**DC409**](../../models/DC409.md) |  | 


### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

