<a id="__pageTop"></a>
# digital_certificates.apis.tags.update_digital_certificate_api.UpdateDigitalCertificateApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_digital_certificate**](#update_digital_certificate) | **patch** /digital_certificates/{digital_certificate_id} | Change only select settings of your digital certificate or CSR.

# **update_digital_certificate**
<a id="update_digital_certificate"></a>
> DC200 update_digital_certificate(digital_certificate_idany_type)

Change only select settings of your digital certificate or CSR.

### Example

* Api Key Authentication (tokenAuth):
```python
import digital_certificates
from digital_certificates.apis.tags import update_digital_certificate_api
from digital_certificates.model.dc400 import DC400
from digital_certificates.model.dc200 import DC200
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
    api_instance = update_digital_certificate_api.UpdateDigitalCertificateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'digital_certificate_id': 1,
    }
    body = dict(
        name="name_example",
        certificate="certificate_example",
        private_key="private_key_example",
        certificate_type="edge_certificate",
        managed=True,
    )
    try:
        # Change only select settings of your digital certificate or CSR.
        api_response = api_instance.update_digital_certificate(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except digital_certificates.ApiException as e:
        print("Exception when calling UpdateDigitalCertificateApi->update_digital_certificate: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json; version&#x3D;3', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**certificate** | str,  | str,  |  | [optional] 
**private_key** | str,  | str,  |  | [optional] 
**certificate_type** | str,  | str,  |  | [optional] must be one of ["edge_certificate", "trusted_ca_certificate", ] 
**managed** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

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
200 | [ApiResponseFor200](#update_digital_certificate.ApiResponseFor200) | Successful operation
400 | [ApiResponseFor400](#update_digital_certificate.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#update_digital_certificate.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_digital_certificate.ApiResponseFor404) | Not Found

#### update_digital_certificate.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**DC200**](../../models/DC200.md) |  | 


#### update_digital_certificate.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**DC400**](../../models/DC400.md) |  | 


#### update_digital_certificate.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**DC403**](../../models/DC403.md) |  | 


#### update_digital_certificate.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**DC404**](../../models/DC404.md) |  | 


### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

