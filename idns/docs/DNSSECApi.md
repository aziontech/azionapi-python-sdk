# idns.DNSSECApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_zone_dns_sec**](DNSSECApi.md#get_zone_dns_sec) | **GET** /intelligent_dns/{zone_id}/dnssec | Retrieve the DNSSEC zone status
[**put_zone_dns_sec**](DNSSECApi.md#put_zone_dns_sec) | **PATCH** /intelligent_dns/{zone_id}/dnssec | Update the DNSSEC zone


# **get_zone_dns_sec**
> GetOrPatchDnsSecResponse get_zone_dns_sec(zone_id)

Retrieve the DNSSEC zone status

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import idns
from idns.models.get_or_patch_dns_sec_response import GetOrPatchDnsSecResponse
from idns.rest import ApiException
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
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with idns.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = idns.DNSSECApi(api_client)
    zone_id = 56 # int | The hosted zone id

    try:
        # Retrieve the DNSSEC zone status
        api_response = api_instance.get_zone_dns_sec(zone_id)
        print("The response of DNSSECApi->get_zone_dns_sec:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSECApi->get_zone_dns_sec: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**| The hosted zone id | 

### Return type

[**GetOrPatchDnsSecResponse**](GetOrPatchDnsSecResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DNSSEC status retrieved |  -  |
**400** | Error |  -  |
**404** | Zone not found |  -  |
**500** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_zone_dns_sec**
> GetOrPatchDnsSecResponse put_zone_dns_sec(zone_id, dns_sec=dns_sec)

Update the DNSSEC zone

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import idns
from idns.models.dns_sec import DnsSec
from idns.models.get_or_patch_dns_sec_response import GetOrPatchDnsSecResponse
from idns.rest import ApiException
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
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with idns.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = idns.DNSSECApi(api_client)
    zone_id = 56 # int | The hosted zone id
    dns_sec = {"is_enabled":true} # DnsSec |  (optional)

    try:
        # Update the DNSSEC zone
        api_response = api_instance.put_zone_dns_sec(zone_id, dns_sec=dns_sec)
        print("The response of DNSSECApi->put_zone_dns_sec:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSECApi->put_zone_dns_sec: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**| The hosted zone id | 
 **dns_sec** | [**DnsSec**](DnsSec.md)|  | [optional] 

### Return type

[**GetOrPatchDnsSecResponse**](GetOrPatchDnsSecResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DNSSEC status updated |  -  |
**201** | Zone updated |  -  |
**400** | Zone update error |  -  |
**404** | Zone not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

