# domains.DomainsApi

All URIs are relative to *https://api.azionapi.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_domain**](DomainsApi.md#create_domain) | **POST** /domains | /domains
[**del_domain**](DomainsApi.md#del_domain) | **DELETE** /domains/{id} | /domains/:id
[**get_domain**](DomainsApi.md#get_domain) | **GET** /domains/{id} | /domains/:id
[**get_domains**](DomainsApi.md#get_domains) | **GET** /domains | /domains
[**put_domain**](DomainsApi.md#put_domain) | **PUT** /domains/{id} | /domains:/:id
[**update_domain**](DomainsApi.md#update_domain) | **PATCH** /domains/{id} | /domains/:id


# **create_domain**
> DomainResponseWithResult create_domain(accept=accept, content_type=content_type, create_domain_request=create_domain_request)

/domains

It enables you to include a new domain into an account.

### Example

* Api Key Authentication (tokenAuth):

```python
import domains
from domains.models.create_domain_request import CreateDomainRequest
from domains.models.domain_response_with_result import DomainResponseWithResult
from domains.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = domains.Configuration(
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
with domains.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = domains.DomainsApi(api_client)
    accept = 'application/json; version=3' # str |  (optional)
    content_type = 'application/json' # str |  (optional)
    create_domain_request = domains.CreateDomainRequest() # CreateDomainRequest |  (optional)

    try:
        # /domains
        api_response = api_instance.create_domain(accept=accept, content_type=content_type, create_domain_request=create_domain_request)
        print("The response of DomainsApi->create_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->create_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 
 **create_domain_request** | [**CreateDomainRequest**](CreateDomainRequest.md)|  | [optional] 

### Return type

[**DomainResponseWithResult**](DomainResponseWithResult.md)

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
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **del_domain**
> del_domain(id, accept=accept)

/domains/:id

It enables you to delete a domain.

### Example

* Api Key Authentication (tokenAuth):

```python
import domains
from domains.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = domains.Configuration(
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
with domains.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = domains.DomainsApi(api_client)
    id = 'id_example' # str | The id of the domain to be deleted. 
    accept = 'application/json; version=3' # str |  (optional)

    try:
        # /domains/:id
        api_instance.del_domain(id, accept=accept)
    except Exception as e:
        print("Exception when calling DomainsApi->del_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the domain to be deleted.  | 
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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain**
> DomainResponseWithResult get_domain(id, accept=accept)

/domains/:id

It returns details of a domain.

### Example

* Api Key Authentication (tokenAuth):

```python
import domains
from domains.models.domain_response_with_result import DomainResponseWithResult
from domains.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = domains.Configuration(
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
with domains.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = domains.DomainsApi(api_client)
    id = 'id_example' # str | The id of the domain to be consulted. 
    accept = 'application/json; version=3' # str |  (optional)

    try:
        # /domains/:id
        api_response = api_instance.get_domain(id, accept=accept)
        print("The response of DomainsApi->get_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->get_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the domain to be consulted.  | 
 **accept** | **str**|  | [optional] 

### Return type

[**DomainResponseWithResult**](DomainResponseWithResult.md)

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

# **get_domains**
> DomainResponseWithResults get_domains(page=page, page_size=page_size, sort=sort, order_by=order_by, accept=accept)

/domains

It returns the list of domains of an account.

### Example

* Api Key Authentication (tokenAuth):

```python
import domains
from domains.models.domain_response_with_results import DomainResponseWithResults
from domains.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = domains.Configuration(
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
with domains.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = domains.DomainsApi(api_client)
    page = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    sort = 'sort_example' # str |  (optional)
    order_by = 'order_by_example' # str |  (optional)
    accept = 'application/json; version=3' # str |  (optional)

    try:
        # /domains
        api_response = api_instance.get_domains(page=page, page_size=page_size, sort=sort, order_by=order_by, accept=accept)
        print("The response of DomainsApi->get_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->get_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 

### Return type

[**DomainResponseWithResults**](DomainResponseWithResults.md)

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

# **put_domain**
> DomainResponseWithResult put_domain(id, accept=accept, content_type=content_type, put_domain_request=put_domain_request)

/domains:/:id

It overwrites all fields of a domain, while preserving the id. Optional fields not filled in will be replaced by the default values.  To update only some fields in a domain, consider using the PATCH method instead of PUT.

### Example

* Api Key Authentication (tokenAuth):

```python
import domains
from domains.models.domain_response_with_result import DomainResponseWithResult
from domains.models.put_domain_request import PutDomainRequest
from domains.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = domains.Configuration(
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
with domains.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = domains.DomainsApi(api_client)
    id = 'id_example' # str | 
    accept = 'application/json; version=3' # str |  (optional)
    content_type = 'application/json' # str |  (optional)
    put_domain_request = domains.PutDomainRequest() # PutDomainRequest |  (optional)

    try:
        # /domains:/:id
        api_response = api_instance.put_domain(id, accept=accept, content_type=content_type, put_domain_request=put_domain_request)
        print("The response of DomainsApi->put_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->put_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 
 **put_domain_request** | [**PutDomainRequest**](PutDomainRequest.md)|  | [optional] 

### Return type

[**DomainResponseWithResult**](DomainResponseWithResult.md)

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

# **update_domain**
> DomainResponseWithResult update_domain(id, accept=accept, content_type=content_type, update_domain_request=update_domain_request)

/domains/:id

It updates one or more fields in a Domain, preserving the value of the fields not informed.

### Example

* Api Key Authentication (tokenAuth):

```python
import domains
from domains.models.domain_response_with_result import DomainResponseWithResult
from domains.models.update_domain_request import UpdateDomainRequest
from domains.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.azionapi.net
# See configuration.py for a list of all supported configuration parameters.
configuration = domains.Configuration(
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
with domains.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = domains.DomainsApi(api_client)
    id = 'id_example' # str | 
    accept = 'application/json; version=3' # str |  (optional)
    content_type = 'application/json' # str |  (optional)
    update_domain_request = domains.UpdateDomainRequest() # UpdateDomainRequest |  (optional)

    try:
        # /domains/:id
        api_response = api_instance.update_domain(id, accept=accept, content_type=content_type, update_domain_request=update_domain_request)
        print("The response of DomainsApi->update_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->update_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 
 **update_domain_request** | [**UpdateDomainRequest**](UpdateDomainRequest.md)|  | [optional] 

### Return type

[**DomainResponseWithResult**](DomainResponseWithResult.md)

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

