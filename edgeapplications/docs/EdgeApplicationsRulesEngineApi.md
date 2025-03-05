# edgeapplications.EdgeApplicationsRulesEngineApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edge_applications_edge_application_id_rules_engine_phase_rules_get**](EdgeApplicationsRulesEngineApi.md#edge_applications_edge_application_id_rules_engine_phase_rules_get) | **GET** /edge_applications/{edge_application_id}/rules_engine/{phase}/rules | /edge_applications/{edge_application_id}/rules_engine/{phase}/rules
[**edge_applications_edge_application_id_rules_engine_phase_rules_post**](EdgeApplicationsRulesEngineApi.md#edge_applications_edge_application_id_rules_engine_phase_rules_post) | **POST** /edge_applications/{edge_application_id}/rules_engine/{phase}/rules | /edge_applications/{edge_application_id}/rules_engine/{phase}/rules
[**edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete**](EdgeApplicationsRulesEngineApi.md#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete) | **DELETE** /edge_applications/{edge_application_id}/rules_engine/{phase}/rules/{rule_id} | /edge_applications/{edge_application_id}/rules_engine/{phase}/rules
[**edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get**](EdgeApplicationsRulesEngineApi.md#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get) | **GET** /edge_applications/{edge_application_id}/rules_engine/{phase}/rules/{rule_id} | /edge_applications/{edge_application_id}/rules_engine/{phase}/rules
[**edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch**](EdgeApplicationsRulesEngineApi.md#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch) | **PATCH** /edge_applications/{edge_application_id}/rules_engine/{phase}/rules/{rule_id} | /edge_applications/:edge_application_id:/rules_engine/:phase:/rules/:rule_id:
[**edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put**](EdgeApplicationsRulesEngineApi.md#edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put) | **PUT** /edge_applications/{edge_application_id}/rules_engine/{phase}/rules/{rule_id} | /edge_applications/:edge_application_id:/rules_engine/:phase:/rules/:rule_id:


# **edge_applications_edge_application_id_rules_engine_phase_rules_get**
> RulesEngineResponse edge_applications_edge_application_id_rules_engine_phase_rules_get(edge_application_id, phase, page=page, page_size=page_size, filter=filter, order_by=order_by, sort=sort, accept=accept)

/edge_applications/{edge_application_id}/rules_engine/{phase}/rules

### Example

* Api Key Authentication (tokenAuth):

```python
import edgeapplications
from edgeapplications.models.rules_engine_response import RulesEngineResponse
from edgeapplications.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgeapplications.Configuration(
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
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgeapplications.EdgeApplicationsRulesEngineApi(api_client)
    edge_application_id = 56 # int | 
    phase = 'phase_example' # str | 
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    filter = 'filter_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    sort = 'sort_example' # str |  (optional)
    accept = 'application/json; version=3' # str |  (optional)

    try:
        # /edge_applications/{edge_application_id}/rules_engine/{phase}/rules
        api_response = api_instance.edge_applications_edge_application_id_rules_engine_phase_rules_get(edge_application_id, phase, page=page, page_size=page_size, filter=filter, order_by=order_by, sort=sort, accept=accept)
        print("The response of EdgeApplicationsRulesEngineApi->edge_applications_edge_application_id_rules_engine_phase_rules_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsRulesEngineApi->edge_applications_edge_application_id_rules_engine_phase_rules_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **int**|  | 
 **phase** | **str**|  | 
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**RulesEngineResponse**](RulesEngineResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; version=3

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_applications_edge_application_id_rules_engine_phase_rules_post**
> RulesEngineIdResponse edge_applications_edge_application_id_rules_engine_phase_rules_post(edge_application_id, phase, accept=accept, content_type=content_type, create_rules_engine_request=create_rules_engine_request)

/edge_applications/{edge_application_id}/rules_engine/{phase}/rules

Check below the list of behaviors that can be applied:

| Name                                | Behavior               |
| ----------------------------------- | ---------------------- |
| Add Request Cookie                  | add_request_cookie     |
| Add Request Header                  | add_request_header     |
| Add Response Cookie                 | set_cookie             |
| Add Response Header                 | add_response_header    |
| Bypass Cache                        | bypass_cache_phase     |
| Capture Match Groups                | capture_match_groups   |
| Deliver                             | deliver                |
| Deny (403 Forbidden)                | deny                   |
| Enable Gzip                         | enable_gzip            |
| Filter Request Cookie               | filter_request_cookie  |
| Filter Request Header               | filter_request_header  |
| Filter Response Cookie              | filter_response_cookie |
| Filter Response Header              | filter_response_header |
| Finish Request Phase                | finish_request_phase   |
| Forward Cookies                     | forward_cookies        |
| Optimize Images                     | optimize_images        |
| Redirect HTTP to HTTPS              | redirect_http_to_https |
| Redirect To (301 Moved Permanently) | redirect_to_301        |
| Redirect To (302 Found)             | redirect_to_302        |
| Rewrite Request                     | rewrite_request        |
| Run Function                        | run_function           |
| Set Cache Policy                    | set_cache_policy       |
| Set Origin                          | set_origin             |

### Example

* Api Key Authentication (tokenAuth):

```python
import edgeapplications
from edgeapplications.models.create_rules_engine_request import CreateRulesEngineRequest
from edgeapplications.models.rules_engine_id_response import RulesEngineIdResponse
from edgeapplications.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgeapplications.Configuration(
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
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgeapplications.EdgeApplicationsRulesEngineApi(api_client)
    edge_application_id = 56 # int | 
    phase = 'phase_example' # str | 
    accept = 'application/json; version=3' # str |  (optional)
    content_type = 'application/json' # str | The type of coding used in the Body (application/json). <br>  Example: Content-Type: application/json (optional)
    create_rules_engine_request = edgeapplications.CreateRulesEngineRequest() # CreateRulesEngineRequest |  (optional)

    try:
        # /edge_applications/{edge_application_id}/rules_engine/{phase}/rules
        api_response = api_instance.edge_applications_edge_application_id_rules_engine_phase_rules_post(edge_application_id, phase, accept=accept, content_type=content_type, create_rules_engine_request=create_rules_engine_request)
        print("The response of EdgeApplicationsRulesEngineApi->edge_applications_edge_application_id_rules_engine_phase_rules_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsRulesEngineApi->edge_applications_edge_application_id_rules_engine_phase_rules_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **int**|  | 
 **phase** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **content_type** | **str**| The type of coding used in the Body (application/json). &lt;br&gt;  Example: Content-Type: application/json | [optional] 
 **create_rules_engine_request** | [**CreateRulesEngineRequest**](CreateRulesEngineRequest.md)|  | [optional] 

### Return type

[**RulesEngineIdResponse**](RulesEngineIdResponse.md)

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
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete**
> edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete(edge_application_id, phase, rule_id, accept=accept)

/edge_applications/{edge_application_id}/rules_engine/{phase}/rules

### Example

* Api Key Authentication (tokenAuth):

```python
import edgeapplications
from edgeapplications.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgeapplications.Configuration(
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
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgeapplications.EdgeApplicationsRulesEngineApi(api_client)
    edge_application_id = 56 # int | The id of the edge application you plan to delete. 
    phase = 'phase_example' # str | 
    rule_id = 56 # int | The id of the rule you plan to delete. 
    accept = 'application/json; version=3' # str |  (optional)

    try:
        # /edge_applications/{edge_application_id}/rules_engine/{phase}/rules
        api_instance.edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete(edge_application_id, phase, rule_id, accept=accept)
    except Exception as e:
        print("Exception when calling EdgeApplicationsRulesEngineApi->edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **int**| The id of the edge application you plan to delete.  | 
 **phase** | **str**|  | 
 **rule_id** | **int**| The id of the rule you plan to delete.  | 
 **accept** | **str**|  | [optional] 

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
**204** | No response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get**
> RulesEngineIdResponse edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get(edge_application_id, phase, rule_id, accept=accept)

/edge_applications/{edge_application_id}/rules_engine/{phase}/rules

### Example

* Api Key Authentication (tokenAuth):

```python
import edgeapplications
from edgeapplications.models.rules_engine_id_response import RulesEngineIdResponse
from edgeapplications.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgeapplications.Configuration(
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
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgeapplications.EdgeApplicationsRulesEngineApi(api_client)
    edge_application_id = 56 # int | The id of the edge application you want to get. 
    phase = 'phase_example' # str | 
    rule_id = 56 # int | The id of the rule you plan to delete. 
    accept = 'application/json; version=3' # str |  (optional)

    try:
        # /edge_applications/{edge_application_id}/rules_engine/{phase}/rules
        api_response = api_instance.edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get(edge_application_id, phase, rule_id, accept=accept)
        print("The response of EdgeApplicationsRulesEngineApi->edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsRulesEngineApi->edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **int**| The id of the edge application you want to get.  | 
 **phase** | **str**|  | 
 **rule_id** | **int**| The id of the rule you plan to delete.  | 
 **accept** | **str**|  | [optional] 

### Return type

[**RulesEngineIdResponse**](RulesEngineIdResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; version=3

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch**
> RulesEngineIdResponse edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch(edge_application_id, phase, rule_id, accept=accept, content_type=content_type, patch_rules_engine_request=patch_rules_engine_request)

/edge_applications/:edge_application_id:/rules_engine/:phase:/rules/:rule_id:

### Example

* Api Key Authentication (tokenAuth):

```python
import edgeapplications
from edgeapplications.models.patch_rules_engine_request import PatchRulesEngineRequest
from edgeapplications.models.rules_engine_id_response import RulesEngineIdResponse
from edgeapplications.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgeapplications.Configuration(
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
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgeapplications.EdgeApplicationsRulesEngineApi(api_client)
    edge_application_id = 56 # int | 
    phase = 'phase_example' # str | 
    rule_id = 56 # int | 
    accept = 'application/json; version=3' # str |  (optional)
    content_type = 'application/json' # str | The type of coding used in the Body (application/json). <br>  Example: Content-Type: application/json (optional)
    patch_rules_engine_request = edgeapplications.PatchRulesEngineRequest() # PatchRulesEngineRequest |  (optional)

    try:
        # /edge_applications/:edge_application_id:/rules_engine/:phase:/rules/:rule_id:
        api_response = api_instance.edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch(edge_application_id, phase, rule_id, accept=accept, content_type=content_type, patch_rules_engine_request=patch_rules_engine_request)
        print("The response of EdgeApplicationsRulesEngineApi->edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsRulesEngineApi->edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **int**|  | 
 **phase** | **str**|  | 
 **rule_id** | **int**|  | 
 **accept** | **str**|  | [optional] 
 **content_type** | **str**| The type of coding used in the Body (application/json). &lt;br&gt;  Example: Content-Type: application/json | [optional] 
 **patch_rules_engine_request** | [**PatchRulesEngineRequest**](PatchRulesEngineRequest.md)|  | [optional] 

### Return type

[**RulesEngineIdResponse**](RulesEngineIdResponse.md)

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
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put**
> RulesEngineIdResponse edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put(edge_application_id, phase, rule_id, accept=accept, content_type=content_type, update_rules_engine_request=update_rules_engine_request)

/edge_applications/:edge_application_id:/rules_engine/:phase:/rules/:rule_id:

### Example

* Api Key Authentication (tokenAuth):

```python
import edgeapplications
from edgeapplications.models.rules_engine_id_response import RulesEngineIdResponse
from edgeapplications.models.update_rules_engine_request import UpdateRulesEngineRequest
from edgeapplications.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = edgeapplications.Configuration(
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
with edgeapplications.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = edgeapplications.EdgeApplicationsRulesEngineApi(api_client)
    edge_application_id = 56 # int | 
    phase = 'phase_example' # str | 
    rule_id = 56 # int | 
    accept = 'application/json; version=3' # str |  (optional)
    content_type = 'application/json' # str | The type of coding used in the Body (application/json). <br>  Example: Content-Type: application/json (optional)
    update_rules_engine_request = edgeapplications.UpdateRulesEngineRequest() # UpdateRulesEngineRequest |  (optional)

    try:
        # /edge_applications/:edge_application_id:/rules_engine/:phase:/rules/:rule_id:
        api_response = api_instance.edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put(edge_application_id, phase, rule_id, accept=accept, content_type=content_type, update_rules_engine_request=update_rules_engine_request)
        print("The response of EdgeApplicationsRulesEngineApi->edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApplicationsRulesEngineApi->edge_applications_edge_application_id_rules_engine_phase_rules_rule_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_application_id** | **int**|  | 
 **phase** | **str**|  | 
 **rule_id** | **int**|  | 
 **accept** | **str**|  | [optional] 
 **content_type** | **str**| The type of coding used in the Body (application/json). &lt;br&gt;  Example: Content-Type: application/json | [optional] 
 **update_rules_engine_request** | [**UpdateRulesEngineRequest**](UpdateRulesEngineRequest.md)|  | [optional] 

### Return type

[**RulesEngineIdResponse**](RulesEngineIdResponse.md)

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
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

