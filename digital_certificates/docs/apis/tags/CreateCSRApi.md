<a id="__pageTop"></a>
# digital_certificates.apis.tags.create_csr_api.CreateCSRApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_csr**](#create_csr) | **post** /digital_certificates/csr | Create an encrypted Certificate Request with Azion, which can then be sent for signing to a CA

# **create_csr**
<a id="create_csr"></a>
> DC200 create_csr(any_type)

Create an encrypted Certificate Request with Azion, which can then be sent for signing to a CA

### Example

* Api Key Authentication (tokenAuth):
```python
import digital_certificates
from digital_certificates.apis.tags import create_csr_api
from digital_certificates.model.dc400 import DC400
from digital_certificates.model.dc200 import DC200
from digital_certificates.model.dc403 import DC403
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
    api_instance = create_csr_api.CreateCSRApi(api_client)

    # example passing only required values which don't have defaults set
    body = dict(
        name="name_example",
        common_name="common_name_example",
        country="country_example",
        state="state_example",
        locality="locality_example",
        organization="organization_example",
        organization_unity="organization_unity_example",
        email="email_example",
        private_key_type="private_key_type_example",
        sans=[
            "sans_example"
        ],
    )
    try:
        # Create an encrypted Certificate Request with Azion, which can then be sent for signing to a CA
        api_response = api_instance.create_csr(
            body=body,
        )
        pprint(api_response)
    except digital_certificates.ApiException as e:
        print("Exception when calling CreateCSRApi->create_csr: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
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
**common_name** | str,  | str,  |  | [optional] 
**country** | str,  | str,  |  | [optional] 
**state** | str,  | str,  |  | [optional] 
**locality** | str,  | str,  |  | [optional] 
**organization** | str,  | str,  |  | [optional] 
**organization_unity** | str,  | str,  |  | [optional] 
**email** | str,  | str,  |  | [optional] 
**private_key_type** | str,  | str,  |  | [optional] 
**[sans](#sans)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# sans

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_csr.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_csr.ApiResponseFor400) | Successful operation
403 | [ApiResponseFor403](#create_csr.ApiResponseFor403) | Forbidden

#### create_csr.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**DC200**](../../models/DC200.md) |  | 


#### create_csr.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**DC400**](../../models/DC400.md) |  | 


#### create_csr.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJsonVersion3, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJsonVersion3
Type | Description  | Notes
------------- | ------------- | -------------
[**DC403**](../../models/DC403.md) |  | 


### Authorization

[tokenAuth](../../../README.md#tokenAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

