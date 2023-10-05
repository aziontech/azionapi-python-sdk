# idns.ZonesApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_zone**](ZonesApi.md#delete_zone) | **DELETE** /intelligent_dns/{zone_id} | Remove an Intelligent DNS hosted zone
[**get_zone**](ZonesApi.md#get_zone) | **GET** /intelligent_dns/{zone_id} | Get an Intelligent DNS hosted zone
[**get_zones**](ZonesApi.md#get_zones) | **GET** /intelligent_dns | Get a collection of Intelligent DNS zones
[**post_zone**](ZonesApi.md#post_zone) | **POST** /intelligent_dns | Add a new Intelligent DNS zone
[**put_zone**](ZonesApi.md#put_zone) | **PUT** /intelligent_dns/{zone_id} | Update an Intelligent DNS hosted zone


# **delete_zone**
> str delete_zone(zone_id)

Remove an Intelligent DNS hosted zone

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import idns
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
    api_instance = idns.ZonesApi(api_client)
    zone_id = 56 # int | The hosted zone id

    try:
        # Remove an Intelligent DNS hosted zone
        api_response = api_instance.delete_zone(zone_id)
        print("The response of ZonesApi->delete_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZonesApi->delete_zone: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**| The hosted zone id | 

### Return type

**str**

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Zone removed |  -  |
**404** | Zone not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone**
> GetZoneResponse get_zone(zone_id)

Get an Intelligent DNS hosted zone

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import idns
from idns.models.get_zone_response import GetZoneResponse
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
    api_instance = idns.ZonesApi(api_client)
    zone_id = 56 # int | The hosted zone id

    try:
        # Get an Intelligent DNS hosted zone
        api_response = api_instance.get_zone(zone_id)
        print("The response of ZonesApi->get_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZonesApi->get_zone: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**| The hosted zone id | 

### Return type

[**GetZoneResponse**](GetZoneResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Zone retrieved |  -  |
**404** | Zone not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zones**
> GetZonesResponse get_zones(order_by=order_by, sort=sort, page=page, page_size=page_size)

Get a collection of Intelligent DNS zones

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import idns
from idns.models.get_zones_response import GetZonesResponse
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
    api_instance = idns.ZonesApi(api_client)
    order_by = 'name' # str | Identifies which property the return should be sorted by. (optional) (default to 'name')
    sort = 'asc' # str | Defines whether objects are shown in ascending or descending order depending on the value set in order_by. (optional) (default to 'asc')
    page = 1 # int | Identifies which page should be returned, if the return is paginated. (optional) (default to 1)
    page_size = 10 # int | Identifies how many items should be returned per page. (optional) (default to 10)

    try:
        # Get a collection of Intelligent DNS zones
        api_response = api_instance.get_zones(order_by=order_by, sort=sort, page=page, page_size=page_size)
        print("The response of ZonesApi->get_zones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZonesApi->get_zones: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_by** | **str**| Identifies which property the return should be sorted by. | [optional] [default to &#39;name&#39;]
 **sort** | **str**| Defines whether objects are shown in ascending or descending order depending on the value set in order_by. | [optional] [default to &#39;asc&#39;]
 **page** | **int**| Identifies which page should be returned, if the return is paginated. | [optional] [default to 1]
 **page_size** | **int**| Identifies how many items should be returned per page. | [optional] [default to 10]

### Return type

[**GetZonesResponse**](GetZonesResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Zones collection retrieved |  -  |
**400** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_zone**
> PostOrPutZoneResponse post_zone(zone=zone)

Add a new Intelligent DNS zone

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import idns
from idns.models.post_or_put_zone_response import PostOrPutZoneResponse
from idns.models.zone import Zone
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
    api_instance = idns.ZonesApi(api_client)
    zone = {"name":"New Intelligent DNS zone","domain":"new.domain.com","is_active":true} # Zone |  (optional)

    try:
        # Add a new Intelligent DNS zone
        api_response = api_instance.post_zone(zone=zone)
        print("The response of ZonesApi->post_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZonesApi->post_zone: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | [**Zone**](Zone.md)|  | [optional] 

### Return type

[**PostOrPutZoneResponse**](PostOrPutZoneResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Zone added |  -  |
**400** | Error |  -  |
**404** | Zone not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_zone**
> PostOrPutZoneResponse put_zone(zone_id, zone=zone)

Update an Intelligent DNS hosted zone

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import idns
from idns.models.post_or_put_zone_response import PostOrPutZoneResponse
from idns.models.zone import Zone
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
    api_instance = idns.ZonesApi(api_client)
    zone_id = 56 # int | The hosted zone id
    zone = {"name":"Update Intelligent DNS zone","domain":"other.domain.com","is_active":true} # Zone |  (optional)

    try:
        # Update an Intelligent DNS hosted zone
        api_response = api_instance.put_zone(zone_id, zone=zone)
        print("The response of ZonesApi->put_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ZonesApi->put_zone: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**| The hosted zone id | 
 **zone** | [**Zone**](Zone.md)|  | [optional] 

### Return type

[**PostOrPutZoneResponse**](PostOrPutZoneResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Zone updated |  -  |
**400** | Zone update error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

