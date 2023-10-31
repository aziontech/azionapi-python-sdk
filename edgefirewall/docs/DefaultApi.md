# edgefirewall.DefaultApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edge_firewall_edge_firewall_id_rules_engine_get**](DefaultApi.md#edge_firewall_edge_firewall_id_rules_engine_get) | **GET** /edge_firewall/{edge_firewall_id}/rules_engine | List all rule sets.
[**edge_firewall_edge_firewall_id_rules_engine_post**](DefaultApi.md#edge_firewall_edge_firewall_id_rules_engine_post) | **POST** /edge_firewall/{edge_firewall_id}/rules_engine | Create rule set.
[**edge_firewall_edge_firewall_id_rules_engine_rule_set_id_delete**](DefaultApi.md#edge_firewall_edge_firewall_id_rules_engine_rule_set_id_delete) | **DELETE** /edge_firewall/{edge_firewall_id}/rules_engine/{rule_set_id} | Delete rule set.
[**edge_firewall_edge_firewall_id_rules_engine_rule_set_id_get**](DefaultApi.md#edge_firewall_edge_firewall_id_rules_engine_rule_set_id_get) | **GET** /edge_firewall/{edge_firewall_id}/rules_engine/{rule_set_id} | Retrieve rule set by ID.
[**edge_firewall_edge_firewall_id_rules_engine_rule_set_id_patch**](DefaultApi.md#edge_firewall_edge_firewall_id_rules_engine_rule_set_id_patch) | **PATCH** /edge_firewall/{edge_firewall_id}/rules_engine/{rule_set_id} | Edit rule set.
[**edge_firewall_edge_firewall_id_rules_engine_rule_set_id_put**](DefaultApi.md#edge_firewall_edge_firewall_id_rules_engine_rule_set_id_put) | **PUT** /edge_firewall/{edge_firewall_id}/rules_engine/{rule_set_id} | Overwrite rule set
[**edge_firewall_get**](DefaultApi.md#edge_firewall_get) | **GET** /edge_firewall | List all user edge firewall
[**edge_firewall_post**](DefaultApi.md#edge_firewall_post) | **POST** /edge_firewall | Create a edge firewall
[**edge_firewall_uuid_delete**](DefaultApi.md#edge_firewall_uuid_delete) | **DELETE** /edge_firewall/{uuid} | Delete an edge firewall by uuid
[**edge_firewall_uuid_get**](DefaultApi.md#edge_firewall_uuid_get) | **GET** /edge_firewall/{uuid} | Retrieve an edge firewall set by uuid
[**edge_firewall_uuid_patch**](DefaultApi.md#edge_firewall_uuid_patch) | **PATCH** /edge_firewall/{uuid} | Update some edge firewall attributes, like \&quot;active\&quot;
[**edge_firewall_uuid_put**](DefaultApi.md#edge_firewall_uuid_put) | **PUT** /edge_firewall/{uuid} | Overwrite some edge firewall attributes, like \&quot;active\&quot;


# **edge_firewall_edge_firewall_id_rules_engine_get**
> RuleSetResponseAll edge_firewall_edge_firewall_id_rules_engine_get(edge_firewall_id, page=page, page_size=page_size, sort=sort, order_by=order_by)

List all rule sets.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgefirewall
from edgefirewall.models.rule_set_response_all import RuleSetResponseAll
from edgefirewall.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefirewall.Configuration(
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
with edgefirewall.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgefirewall.DefaultApi(api_client)
    edge_firewall_id = 56 # int | 
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    sort = 'sort_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)

    try:
        # List all rule sets.
        api_response = api_instance.edge_firewall_edge_firewall_id_rules_engine_get(edge_firewall_id, page=page, page_size=page_size, sort=sort, order_by=order_by)
        print("The response of DefaultApi->edge_firewall_edge_firewall_id_rules_engine_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->edge_firewall_edge_firewall_id_rules_engine_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_firewall_id** | **int**|  | 
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**RuleSetResponseAll**](RuleSetResponseAll.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all rule sets. |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_firewall_edge_firewall_id_rules_engine_post**
> RuleSetResponse edge_firewall_edge_firewall_id_rules_engine_post(edge_firewall_id, create_rule_set_request=create_rule_set_request)

Create rule set.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgefirewall
from edgefirewall.models.create_rule_set_request import CreateRuleSetRequest
from edgefirewall.models.rule_set_response import RuleSetResponse
from edgefirewall.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefirewall.Configuration(
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
with edgefirewall.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgefirewall.DefaultApi(api_client)
    edge_firewall_id = 56 # int | 
    create_rule_set_request = edgefirewall.CreateRuleSetRequest() # CreateRuleSetRequest |  (optional)

    try:
        # Create rule set.
        api_response = api_instance.edge_firewall_edge_firewall_id_rules_engine_post(edge_firewall_id, create_rule_set_request=create_rule_set_request)
        print("The response of DefaultApi->edge_firewall_edge_firewall_id_rules_engine_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->edge_firewall_edge_firewall_id_rules_engine_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_firewall_id** | **int**|  | 
 **create_rule_set_request** | [**CreateRuleSetRequest**](CreateRuleSetRequest.md)|  | [optional] 

### Return type

[**RuleSetResponse**](RuleSetResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json; version=3
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create rule set. |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_firewall_edge_firewall_id_rules_engine_rule_set_id_delete**
> edge_firewall_edge_firewall_id_rules_engine_rule_set_id_delete(edge_firewall_id, rule_set_id)

Delete rule set.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgefirewall
from edgefirewall.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefirewall.Configuration(
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
with edgefirewall.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgefirewall.DefaultApi(api_client)
    edge_firewall_id = 56 # int | 
    rule_set_id = 56 # int | 

    try:
        # Delete rule set.
        api_instance.edge_firewall_edge_firewall_id_rules_engine_rule_set_id_delete(edge_firewall_id, rule_set_id)
    except Exception as e:
        print("Exception when calling DefaultApi->edge_firewall_edge_firewall_id_rules_engine_rule_set_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_firewall_id** | **int**|  | 
 **rule_set_id** | **int**|  | 

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
**204** | Delete rule set. |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_firewall_edge_firewall_id_rules_engine_rule_set_id_get**
> RuleSetResult edge_firewall_edge_firewall_id_rules_engine_rule_set_id_get(edge_firewall_id, rule_set_id, order_by=order_by, sort=sort, page=page, page_size=page_size)

Retrieve rule set by ID.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgefirewall
from edgefirewall.models.rule_set_result import RuleSetResult
from edgefirewall.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefirewall.Configuration(
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
with edgefirewall.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgefirewall.DefaultApi(api_client)
    edge_firewall_id = 56 # int | 
    rule_set_id = 56 # int | 
    order_by = 'order_by_example' # str |  (optional)
    sort = 'sort_example' # str |  (optional)
    page = 1 # int |  (optional) (default to 1)
    page_size = 10 # int |  (optional) (default to 10)

    try:
        # Retrieve rule set by ID.
        api_response = api_instance.edge_firewall_edge_firewall_id_rules_engine_rule_set_id_get(edge_firewall_id, rule_set_id, order_by=order_by, sort=sort, page=page, page_size=page_size)
        print("The response of DefaultApi->edge_firewall_edge_firewall_id_rules_engine_rule_set_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->edge_firewall_edge_firewall_id_rules_engine_rule_set_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_firewall_id** | **int**|  | 
 **rule_set_id** | **int**|  | 
 **order_by** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 10]

### Return type

[**RuleSetResult**](RuleSetResult.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieve rule set by ID. |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_firewall_edge_firewall_id_rules_engine_rule_set_id_patch**
> RuleSetResult edge_firewall_edge_firewall_id_rules_engine_rule_set_id_patch(edge_firewall_id, rule_set_id, create_rule_set_request=create_rule_set_request)

Edit rule set.

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgefirewall
from edgefirewall.models.create_rule_set_request import CreateRuleSetRequest
from edgefirewall.models.rule_set_result import RuleSetResult
from edgefirewall.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefirewall.Configuration(
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
with edgefirewall.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgefirewall.DefaultApi(api_client)
    edge_firewall_id = 56 # int | 
    rule_set_id = 56 # int | 
    create_rule_set_request = edgefirewall.CreateRuleSetRequest() # CreateRuleSetRequest |  (optional)

    try:
        # Edit rule set.
        api_response = api_instance.edge_firewall_edge_firewall_id_rules_engine_rule_set_id_patch(edge_firewall_id, rule_set_id, create_rule_set_request=create_rule_set_request)
        print("The response of DefaultApi->edge_firewall_edge_firewall_id_rules_engine_rule_set_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->edge_firewall_edge_firewall_id_rules_engine_rule_set_id_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_firewall_id** | **int**|  | 
 **rule_set_id** | **int**|  | 
 **create_rule_set_request** | [**CreateRuleSetRequest**](CreateRuleSetRequest.md)|  | [optional] 

### Return type

[**RuleSetResult**](RuleSetResult.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json; version=3
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edit rule set. |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_firewall_edge_firewall_id_rules_engine_rule_set_id_put**
> RuleSetResult edge_firewall_edge_firewall_id_rules_engine_rule_set_id_put(edge_firewall_id, rule_set_id, create_rule_set_request=create_rule_set_request)

Overwrite rule set

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgefirewall
from edgefirewall.models.create_rule_set_request import CreateRuleSetRequest
from edgefirewall.models.rule_set_result import RuleSetResult
from edgefirewall.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefirewall.Configuration(
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
with edgefirewall.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgefirewall.DefaultApi(api_client)
    edge_firewall_id = 56 # int | 
    rule_set_id = 56 # int | 
    create_rule_set_request = edgefirewall.CreateRuleSetRequest() # CreateRuleSetRequest |  (optional)

    try:
        # Overwrite rule set
        api_response = api_instance.edge_firewall_edge_firewall_id_rules_engine_rule_set_id_put(edge_firewall_id, rule_set_id, create_rule_set_request=create_rule_set_request)
        print("The response of DefaultApi->edge_firewall_edge_firewall_id_rules_engine_rule_set_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->edge_firewall_edge_firewall_id_rules_engine_rule_set_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_firewall_id** | **int**|  | 
 **rule_set_id** | **int**|  | 
 **create_rule_set_request** | [**CreateRuleSetRequest**](CreateRuleSetRequest.md)|  | [optional] 

### Return type

[**RuleSetResult**](RuleSetResult.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json; version=3
 - **Accept**: application/json; version=3

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Overwrite rule set. |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_firewall_get**
> ListEdgeFirewallResponse edge_firewall_get(page=page, page_size=page_size, sort=sort, order_by=order_by)

List all user edge firewall

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgefirewall
from edgefirewall.models.list_edge_firewall_response import ListEdgeFirewallResponse
from edgefirewall.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefirewall.Configuration(
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
with edgefirewall.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgefirewall.DefaultApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    sort = 'sort_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)

    try:
        # List all user edge firewall
        api_response = api_instance.edge_firewall_get(page=page, page_size=page_size, sort=sort, order_by=order_by)
        print("The response of DefaultApi->edge_firewall_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->edge_firewall_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**ListEdgeFirewallResponse**](ListEdgeFirewallResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of edge firewalls |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_firewall_post**
> EdgeFirewallResponse edge_firewall_post(create_edge_firewall_request)

Create a edge firewall

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgefirewall
from edgefirewall.models.create_edge_firewall_request import CreateEdgeFirewallRequest
from edgefirewall.models.edge_firewall_response import EdgeFirewallResponse
from edgefirewall.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefirewall.Configuration(
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
with edgefirewall.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgefirewall.DefaultApi(api_client)
    create_edge_firewall_request = edgefirewall.CreateEdgeFirewallRequest() # CreateEdgeFirewallRequest | 

    try:
        # Create a edge firewall
        api_response = api_instance.edge_firewall_post(create_edge_firewall_request)
        print("The response of DefaultApi->edge_firewall_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->edge_firewall_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_edge_firewall_request** | [**CreateEdgeFirewallRequest**](CreateEdgeFirewallRequest.md)|  | 

### Return type

[**EdgeFirewallResponse**](EdgeFirewallResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Edge firewall created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_firewall_uuid_delete**
> edge_firewall_uuid_delete(uuid)

Delete an edge firewall by uuid

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgefirewall
from edgefirewall.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefirewall.Configuration(
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
with edgefirewall.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgefirewall.DefaultApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Delete an edge firewall by uuid
        api_instance.edge_firewall_uuid_delete(uuid)
    except Exception as e:
        print("Exception when calling DefaultApi->edge_firewall_uuid_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

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
**204** | Successfully deleted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_firewall_uuid_get**
> EdgeFirewallResponse edge_firewall_uuid_get(uuid)

Retrieve an edge firewall set by uuid

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgefirewall
from edgefirewall.models.edge_firewall_response import EdgeFirewallResponse
from edgefirewall.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefirewall.Configuration(
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
with edgefirewall.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgefirewall.DefaultApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Retrieve an edge firewall set by uuid
        api_response = api_instance.edge_firewall_uuid_get(uuid)
        print("The response of DefaultApi->edge_firewall_uuid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->edge_firewall_uuid_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**EdgeFirewallResponse**](EdgeFirewallResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An edge firewall object |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_firewall_uuid_patch**
> EdgeFirewallResponse edge_firewall_uuid_patch(uuid, update_edge_firewall_request)

Update some edge firewall attributes, like \"active\"

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgefirewall
from edgefirewall.models.edge_firewall_response import EdgeFirewallResponse
from edgefirewall.models.update_edge_firewall_request import UpdateEdgeFirewallRequest
from edgefirewall.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefirewall.Configuration(
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
with edgefirewall.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgefirewall.DefaultApi(api_client)
    uuid = 'uuid_example' # str | 
    update_edge_firewall_request = edgefirewall.UpdateEdgeFirewallRequest() # UpdateEdgeFirewallRequest | 

    try:
        # Update some edge firewall attributes, like \"active\"
        api_response = api_instance.edge_firewall_uuid_patch(uuid, update_edge_firewall_request)
        print("The response of DefaultApi->edge_firewall_uuid_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->edge_firewall_uuid_patch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **update_edge_firewall_request** | [**UpdateEdgeFirewallRequest**](UpdateEdgeFirewallRequest.md)|  | 

### Return type

[**EdgeFirewallResponse**](EdgeFirewallResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_firewall_uuid_put**
> EdgeFirewallResponse edge_firewall_uuid_put(uuid, update_edge_firewall_request)

Overwrite some edge firewall attributes, like \"active\"

### Example

* Api Key Authentication (tokenAuth):
```python
import time
import os
import edgefirewall
from edgefirewall.models.edge_firewall_response import EdgeFirewallResponse
from edgefirewall.models.update_edge_firewall_request import UpdateEdgeFirewallRequest
from edgefirewall.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgefirewall.Configuration(
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
with edgefirewall.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgefirewall.DefaultApi(api_client)
    uuid = 'uuid_example' # str | 
    update_edge_firewall_request = edgefirewall.UpdateEdgeFirewallRequest() # UpdateEdgeFirewallRequest | 

    try:
        # Overwrite some edge firewall attributes, like \"active\"
        api_response = api_instance.edge_firewall_uuid_put(uuid, update_edge_firewall_request)
        print("The response of DefaultApi->edge_firewall_uuid_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->edge_firewall_uuid_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **update_edge_firewall_request** | [**UpdateEdgeFirewallRequest**](UpdateEdgeFirewallRequest.md)|  | 

### Return type

[**EdgeFirewallResponse**](EdgeFirewallResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

