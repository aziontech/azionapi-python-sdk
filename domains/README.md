# domains
## Welcome to the Azion API!

With the following APIs you can check, remove or update existing settings, besides creating new ones.

* * *

## Overview

The Azion API is a RESTful API, based on HTTPS requests, that allows you to integrate your systems with our platform, simply, quickly, and securely.

Here you will find instructions on how our API works and what functionality is available.

This documentation is being constantly updated. Make sure you verify if there are any updates or changes before you perform any development in your application, even if you are familiar with our API.

* * *

Both HTTPS requests and responses must be in JavaScript Object Notation (JSON) format. All HTTPS requests and responses must follow these conventions.

**Base URL**

The base URL of the API, which must be used, is:

[**https://api.azionapi.net/**](https://api.azionapi.net/)

**HTTP Methods**

Each HTTP method defines the type of operation that will be run.

| HTTP Method | CRUD | Whole Collection (e.g. /items) | Specific Item (e.g. /items/:item_id) |
| --- | --- | --- | --- |
| GET | Read | It retrieves the list of items in a Collection. | It retrieves a specific item in a Collection. |
| POST | Create | It creates a new item in the Collection. | \\- |
| PUT | Update/Replace | It replaces a whole Collection with a new one. | It replaces an item in a Collection with a new one. |
| PATCH | Update/Modify | It partially updates a Collection. | It partially updates an item in a Collection |
| DELETE | Delete | It deletes a whole Collection. | It deletes an item in a Collection. |

* * *

**Status Codes**

The HTTP return code defines the status – successful or not – after the requested operation is run.

| Status Code | Meaning |
| --- | --- |
| 200 OK | General Status for a successful operation. |
| 201 CREATED | Successfully created a collection or item, by means of POST or PUT. |
| 204 NO CONTENT | Successful operation, but without any content to be return to the Body. Generally used for DELETE or PUT operations. |
| 207 MULTI-STATUS | A batch of operations were triggered by a single request, which resulted in different return codes when it was run, for some of the operations. The codes are displayed in the “status” field, in the body of the response, for each sub-batch of operations for whichever are applicable. |
| 400 BAD REQUEST | Request error, such as invalid parameters, missing mandatory parameters or others. |
| 401 UNAUTHORIZED | Error caused by a missing HTTP Authentication header. |
| 403 FORBIDDEN | User does not have the permissions to run the requested operation. |
| 404 NOT FOUND | The requested resource does not exist. |
| 405 METHOD NOT ALLOWED | The requested method is not applicable with the URL. |
| 406 NOT ACCEPTABLE | Accept header missing from the HTTP request or the header contains formatting or the version is not supported by the API. |
| 409 CONFLICT | Conflict generated in running the request, such as a request to create an already existing record. |
| 429 TOO MANY REQUESTS | The request was temporarily rejected, due to exceeding the limit on operations. Wait for the time defined in the X-Ratelimit-Reset header and try again. |
| 500 INTERNAL SERVER ERROR | Unintentional error, due to an unidentified failure in the request process. |
| \\--- |  |
| **HTTP Headers** |  |

All requests must be generated with the HTTP header specifying the desired code format for responses and the API version used. The current version of the API is 3 and the format is application/json.

```
Accept: application/json; version=3

```

* * *

**Rate Limit**

The limit of operations that can be run via the API is defined by 3 HTTP response headers:

*   **X-ratelimit-limit:** number of operations allowed in one time-frame;
*   **X-ratelimit-remaining:** number of operations still available in one time-frame;
*   **X-ratelimit-reset:** is the date and time, in IOS 8601 format, which represents the point in the future when the time-frame will be closed and when the limits will, therefore, be reset.
    

Example of HTTP response headers and a request:

```
Date: Thu, 02 Nov 2017 12:30:28 GMT
X-ratelimit-remaining: 199
X-ratelimit-limit: 200
X-ratelimit-reset: 2017-11-02T12:31:28.675446

```

In the example provided, 200 operations are allowed within a 1-minute time frame. Of those, there are 199 still available, because one has already been run. The total limit will be reset after 1 minute.

When the X-ratelimit-limit is reached, or in other words, when the X-ratelimit-remaining reaches zero, the API will give the error, HTTP 429 TOO MANY REQUESTS. If your application receives this error, you will need to wait until the time defined in X-ratelimit-reset has passed, to make another request.

*   **X-ratelimit-limit by product**
    

The *X-ratelimit limit* variations by product are the following:

*   **Real-Time Metrics:** 20 requests per minute.
*   **Real-Time Purge:** 200 requests per minute; except for the Wildcard, which is 2000 a day.
    

> The rate-limit values are based on the client_id.

* * *

**Optional Parameters**

In this version, it is possible to include some optional parameters as part of the GET method, which can help and modify the form in which your data will be returned.

You can combine these parameters to get the result you want.

They are:

| Parameter | Description | Accepted values: |
| --- | --- | --- |
| order_by | Identifies which field the return should be sorted by. The default ordering is ascending. | Depends on the fields available from the endpoint structure |
| sort | Defines which ordering to be used: ascending or descending. | asc  <br>  <br>desc |
| page | Identifies which page should be returned, if the return is paginated. The default value is 1. | Page number. |
| page_size | Identifies how many items should be returned per page. The default value is 10. | Desired number of items. |

* * *

**Request Exemple**

You can use one parameter, or a combination. See the example below, which uses all of them in the same request.

```
GET /domains?order_by=name&page_size=20&sort=desc&page=3
Accept: application/json; version=3
Authorization: token 2909f3932069047f4736dc87e72baaddd19c9f75

```

* * *

# Authentication

Authentication and authorization of operations via Azion API is done through Tokens.

The first step is to create the Token through authenticating a user registered in [Real-Time Manager](https://sso.azion.com/login).

* * *

## Encoding Username and Password in Base64

Only token creation and cancelling operations are performed through Basic Authentication, that is, with a username and password. You can create and cancel the token through the API itself, but for that you need to encode your username and password in base64.

Base64 encoding can be done from the command line on a Unix terminal:

```
$ echo 'user@domain:password'|base64
dXNlckBkb21haW46cGFzc3dvcmQK

```

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import domains
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import domains
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import domains
from pprint import pprint
from domains.apis.tags import domains_api
from domains.model.create_domain_request import CreateDomainRequest
from domains.model.domain_response_with_result import DomainResponseWithResult
from domains.model.domain_response_with_results import DomainResponseWithResults
from domains.model.put_domain_request import PutDomainRequest
from domains.model.update_domain_request import UpdateDomainRequest
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
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with domains.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = domains_api.DomainsApi(api_client)
    accept = "application/json; version=3" # str |  (optional)
content_type = "application/json" # str |  (optional)
create_domain_request = CreateDomainRequest(
        cnames=[
            "cnames_example"
        ],
        cname_access_only=True,
        name="name_example",
        is_active=True,
        edge_application_id=1,
        digital_certificate_id=1,
    ) # CreateDomainRequest |  (optional)

    try:
        # /domains
        api_response = api_instance.create_domain(accept=acceptcontent_type=content_typecreate_domain_request=create_domain_request)
        pprint(api_response)
    except domains.ApiException as e:
        print("Exception when calling DomainsApi->create_domain: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.azionapi.net*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DomainsApi* | [**create_domain**](docs/apis/tags/DomainsApi.md#create_domain) | **post** /domains | /domains
*DomainsApi* | [**del_domain**](docs/apis/tags/DomainsApi.md#del_domain) | **delete** /domains/{id} | /domains/:id
*DomainsApi* | [**get_domain**](docs/apis/tags/DomainsApi.md#get_domain) | **get** /domains/{id} | /domains/:id
*DomainsApi* | [**get_domains**](docs/apis/tags/DomainsApi.md#get_domains) | **get** /domains | /domains
*DomainsApi* | [**put_domain**](docs/apis/tags/DomainsApi.md#put_domain) | **put** /domains/{id} | /domains:/:id
*DomainsApi* | [**update_domain**](docs/apis/tags/DomainsApi.md#update_domain) | **patch** /domains/{id} | /domains/:id

## Documentation For Models

 - [CreateDomainRequest](docs/models/CreateDomainRequest.md)
 - [DomainLinks](docs/models/DomainLinks.md)
 - [DomainResponseWithResult](docs/models/DomainResponseWithResult.md)
 - [DomainResponseWithResults](docs/models/DomainResponseWithResults.md)
 - [DomainResults](docs/models/DomainResults.md)
 - [PutDomainRequest](docs/models/PutDomainRequest.md)
 - [UpdateDomainRequest](docs/models/UpdateDomainRequest.md)

## Documentation For Authorization

Authentication schemes defined for the API:
<a id="tokenAuth"></a>
### tokenAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author



## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in domains.apis and domains.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from domains.apis.default_api import DefaultApi`
- `from domains.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import domains
from domains.apis import *
from domains.models import *
```
