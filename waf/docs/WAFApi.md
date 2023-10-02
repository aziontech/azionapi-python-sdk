# waf.WAFApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_waf_ruleset**](WAFApi.md#create_new_waf_ruleset) | **POST** /waf/rulesets | Create a new WAF Rule Set in an account.
[**delete_waf_ruleset**](WAFApi.md#delete_waf_ruleset) | **DELETE** /waf/rulesets/{waf_rule_set_id} | Remove an WAF Rule Set from an account. Warning: this action cannot be undone.
[**get_waf_domains**](WAFApi.md#get_waf_domains) | **GET** /waf/{wafId}/domains | List all domains attached to a Web Application Firewall (WAF) in an account.
[**get_waf_events**](WAFApi.md#get_waf_events) | **GET** /waf/{wafId}/waf_events | Find WAF log events
[**get_waf_ruleset**](WAFApi.md#get_waf_ruleset) | **GET** /waf/rulesets/{waf_rule_set_id} | List a specific Rule Set associated to a Web Application Firewall (WAF) in an account.
[**list_all_waf**](WAFApi.md#list_all_waf) | **GET** /waf | List all Web Application Firewalls (WAFs) created in an account
[**list_all_waf_rulesets**](WAFApi.md#list_all_waf_rulesets) | **GET** /waf/rulesets | list all Rule Sets associated to a Web Application Firewall (WAF) in an account.
[**update_waf_ruleset**](WAFApi.md#update_waf_ruleset) | **PATCH** /waf/rulesets/{waf_rule_set_id} | Change only select settings of a WAF Rule Set


# **create_new_waf_ruleset**
> SingleWAF create_new_waf_ruleset(create_new_waf_ruleset_request=create_new_waf_ruleset_request)

Create a new WAF Rule Set in an account.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import waf
from waf.models.create_new_waf_ruleset_request import CreateNewWAFRulesetRequest
from waf.models.single_waf import SingleWAF
from waf.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = waf.Configuration(
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
with waf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = waf.WAFApi(api_client)
    create_new_waf_ruleset_request = waf.CreateNewWAFRulesetRequest() # CreateNewWAFRulesetRequest |  (optional)

    try:
        # Create a new WAF Rule Set in an account.
        api_response = api_instance.create_new_waf_ruleset(create_new_waf_ruleset_request=create_new_waf_ruleset_request)
        print("The response of WAFApi->create_new_waf_ruleset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WAFApi->create_new_waf_ruleset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_new_waf_ruleset_request** | [**CreateNewWAFRulesetRequest**](CreateNewWAFRulesetRequest.md)|  | [optional] 

### Return type

[**SingleWAF**](SingleWAF.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json; version=3
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**201** | Successful response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_waf_ruleset**
> delete_waf_ruleset(waf_rule_set_id)

Remove an WAF Rule Set from an account. Warning: this action cannot be undone.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import waf
from waf.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = waf.Configuration(
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
with waf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = waf.WAFApi(api_client)
    waf_rule_set_id = 'waf_rule_set_id_example' # str | 

    try:
        # Remove an WAF Rule Set from an account. Warning: this action cannot be undone.
        api_instance.delete_waf_ruleset(waf_rule_set_id)
    except Exception as e:
        print("Exception when calling WAFApi->delete_waf_ruleset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **waf_rule_set_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_waf_domains**
> WAFDomains200 get_waf_domains(waf_id, name=name)

List all domains attached to a Web Application Firewall (WAF) in an account.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import waf
from waf.models.waf_domains200 import WAFDomains200
from waf.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = waf.Configuration(
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
with waf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = waf.WAFApi(api_client)
    waf_id = 56 # int | ID of WAF to return
    name = 'name_example' # str | searches WAF for name (optional)

    try:
        # List all domains attached to a Web Application Firewall (WAF) in an account.
        api_response = api_instance.get_waf_domains(waf_id, name=name)
        print("The response of WAFApi->get_waf_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WAFApi->get_waf_domains: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **waf_id** | **int**| ID of WAF to return | 
 **name** | **str**| searches WAF for name | [optional] 

### Return type

[**WAFDomains200**](WAFDomains200.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad request |  -  |
**404** | data not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_waf_events**
> WAFEvents200 get_waf_events(waf_id, hour_range, domains_ids, network_list_id=network_list_id)

Find WAF log events

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import waf
from waf.models.waf_events200 import WAFEvents200
from waf.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = waf.Configuration(
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
with waf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = waf.WAFApi(api_client)
    waf_id = 56 # int | ID of WAF to return
    hour_range = 56 # int | Last log hours since now (it must be a integer number ranging between 1 and 72)
    domains_ids = 'domains_ids_example' # str | Multiple domain's id (they must be separated by comma like 1233,1234)
    network_list_id = 56 # int | Id of a network list (optional)

    try:
        # Find WAF log events
        api_response = api_instance.get_waf_events(waf_id, hour_range, domains_ids, network_list_id=network_list_id)
        print("The response of WAFApi->get_waf_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WAFApi->get_waf_events: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **waf_id** | **int**| ID of WAF to return | 
 **hour_range** | **int**| Last log hours since now (it must be a integer number ranging between 1 and 72) | 
 **domains_ids** | **str**| Multiple domain&#39;s id (they must be separated by comma like 1233,1234) | 
 **network_list_id** | **int**| Id of a network list | [optional] 

### Return type

[**WAFEvents200**](WAFEvents200.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad request |  -  |
**401** | unauthorized operation |  -  |
**404** | data not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_waf_ruleset**
> WAFSingle200 get_waf_ruleset(waf_rule_set_id)

List a specific Rule Set associated to a Web Application Firewall (WAF) in an account.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import waf
from waf.models.waf_single200 import WAFSingle200
from waf.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = waf.Configuration(
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
with waf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = waf.WAFApi(api_client)
    waf_rule_set_id = 56 # int | ID of WAF Ruleset to return

    try:
        # List a specific Rule Set associated to a Web Application Firewall (WAF) in an account.
        api_response = api_instance.get_waf_ruleset(waf_rule_set_id)
        print("The response of WAFApi->get_waf_ruleset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WAFApi->get_waf_ruleset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **waf_rule_set_id** | **int**| ID of WAF Ruleset to return | 

### Return type

[**WAFSingle200**](WAFSingle200.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad request |  -  |
**404** | data not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_waf**
> WAFList200 list_all_waf(page=page, page_size=page_size)

List all Web Application Firewalls (WAFs) created in an account

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import waf
from waf.models.waf_list200 import WAFList200
from waf.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = waf.Configuration(
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
with waf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = waf.WAFApi(api_client)
    page = 1 # int | Identifies which page should be returned, if the return is paginated. (optional) (default to 1)
    page_size = 10 # int | Identifies how many items should be returned per page. (optional) (default to 10)

    try:
        # List all Web Application Firewalls (WAFs) created in an account
        api_response = api_instance.list_all_waf(page=page, page_size=page_size)
        print("The response of WAFApi->list_all_waf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WAFApi->list_all_waf: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Identifies which page should be returned, if the return is paginated. | [optional] [default to 1]
 **page_size** | **int**| Identifies how many items should be returned per page. | [optional] [default to 10]

### Return type

[**WAFList200**](WAFList200.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad request |  -  |
**404** | data not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_waf_rulesets**
> WAFList200 list_all_waf_rulesets(order_by=order_by, sort=sort, page=page, page_size=page_size)

list all Rule Sets associated to a Web Application Firewall (WAF) in an account.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import waf
from waf.models.waf_list200 import WAFList200
from waf.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = waf.Configuration(
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
with waf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = waf.WAFApi(api_client)
    order_by = 'name' # str | Identifies which property the return should be sorted by. (optional) (default to 'name')
    sort = 'asc' # str | Defines whether objects are shown in ascending or descending order depending on the value set in order_by. (optional) (default to 'asc')
    page = 1 # int | Identifies which page should be returned, if the return is paginated. (optional) (default to 1)
    page_size = 10 # int | Identifies how many items should be returned per page. (optional) (default to 10)

    try:
        # list all Rule Sets associated to a Web Application Firewall (WAF) in an account.
        api_response = api_instance.list_all_waf_rulesets(order_by=order_by, sort=sort, page=page, page_size=page_size)
        print("The response of WAFApi->list_all_waf_rulesets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WAFApi->list_all_waf_rulesets: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_by** | **str**| Identifies which property the return should be sorted by. | [optional] [default to &#39;name&#39;]
 **sort** | **str**| Defines whether objects are shown in ascending or descending order depending on the value set in order_by. | [optional] [default to &#39;asc&#39;]
 **page** | **int**| Identifies which page should be returned, if the return is paginated. | [optional] [default to 1]
 **page_size** | **int**| Identifies how many items should be returned per page. | [optional] [default to 10]

### Return type

[**WAFList200**](WAFList200.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad request |  -  |
**404** | data not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_waf_ruleset**
> SingleWAF update_waf_ruleset(waf_rule_set_id, single_waf=single_waf)

Change only select settings of a WAF Rule Set

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import waf
from waf.models.single_waf import SingleWAF
from waf.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = waf.Configuration(
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
with waf.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = waf.WAFApi(api_client)
    waf_rule_set_id = 'waf_rule_set_id_example' # str | 
    single_waf = waf.SingleWAF() # SingleWAF |  (optional)

    try:
        # Change only select settings of a WAF Rule Set
        api_response = api_instance.update_waf_ruleset(waf_rule_set_id, single_waf=single_waf)
        print("The response of WAFApi->update_waf_ruleset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WAFApi->update_waf_ruleset: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **waf_rule_set_id** | **str**|  | 
 **single_waf** | [**SingleWAF**](SingleWAF.md)|  | [optional] 

### Return type

[**SingleWAF**](SingleWAF.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json; version=3
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method Not Allowed |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

