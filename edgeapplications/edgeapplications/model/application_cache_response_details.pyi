# coding: utf-8

"""
    Edge Application

    ## Welcome to the Azion API!  With the following APIs you can check, remove or update existing settings, besides creating new ones.  * * *  ## Overview  The Azion API is a RESTful API, based on HTTPS requests, that allows you to integrate your systems with our platform, simply, quickly, and securely.  Here you will find instructions on how our API works and what functionality is available.  This documentation is being constantly updated. Make sure you verify if there are any updates or changes before you perform any development in your application, even if you are familiar with our API.  * * *  Both HTTPS requests and responses must be in JavaScript Object Notation (JSON) format. All HTTPS requests and responses must follow these conventions.  **Base URL**  The base URL of the API, which must be used, is:  [**https://api.azionapi.net/**](https://api.azionapi.net/)  **HTTP Methods**  Each HTTP method defines the type of operation that will be run.  | HTTP Method | CRUD | Whole Collection (e.g. /items) | Specific Item (e.g. /items/:item_id) | | --- | --- | --- | --- | | GET | Read | It retrieves the list of items in a Collection. | It retrieves a specific item in a Collection. | | POST | Create | It creates a new item in the Collection. | \\- | | PUT | Update/Replace | It replaces a whole Collection with a new one. | It replaces an item in a Collection with a new one. | | PATCH | Update/Modify | It partially updates a Collection. | It partially updates an item in a Collection | | DELETE | Delete | It deletes a whole Collection. | It deletes an item in a Collection. |  * * *  **Status Codes**  The HTTP return code defines the status – successful or not – after the requested operation is run.  | Status Code | Meaning | | --- | --- | | 200 OK | General Status for a successful operation. | | 201 CREATED | Successfully created a collection or item, by means of POST or PUT. | | 204 NO CONTENT | Successful operation, but without any content to be return to the Body. Generally used for DELETE or PUT operations. | | 207 MULTI-STATUS | A batch of operations were triggered by a single request, which resulted in different return codes when it was run, for some of the operations. The codes are displayed in the “status” field, in the body of the response, for each sub-batch of operations for whichever are applicable. | | 400 BAD REQUEST | Request error, such as invalid parameters, missing mandatory parameters or others. | | 401 UNAUTHORIZED | Error caused by a missing HTTP Authentication header. | | 403 FORBIDDEN | User does not have the permissions to run the requested operation. | | 404 NOT FOUND | The requested resource does not exist. | | 405 METHOD NOT ALLOWED | The requested method is not applicable with the URL. | | 406 NOT ACCEPTABLE | Accept header missing from the HTTP request or the header contains formatting or the version is not supported by the API. | | 409 CONFLICT | Conflict generated in running the request, such as a request to create an already existing record. | | 429 TOO MANY REQUESTS | The request was temporarily rejected, due to exceeding the limit on operations. Wait for the time defined in the X-Ratelimit-Reset header and try again. | | 500 INTERNAL SERVER ERROR | Unintentional error, due to an unidentified failure in the request process. | | \\--- |  | | **HTTP Headers** |  |  All requests must be generated with the HTTP header specifying the desired code format for responses and the API version used. The current version of the API is 3 and the format is application/json.  ``` Accept: application/json; version=3  ```  * * *  **Rate Limit**  The limit of operations that can be run via the API is defined by 3 HTTP response headers:  *   **X-ratelimit-limit:** number of operations allowed in one time-frame; *   **X-ratelimit-remaining:** number of operations still available in one time-frame; *   **X-ratelimit-reset:** is the date and time, in IOS 8601 format, which represents the point in the future when the time-frame will be closed and when the limits will, therefore, be reset.       Example of HTTP response headers and a request:  ``` Date: Thu, 02 Nov 2017 12:30:28 GMT X-ratelimit-remaining: 199 X-ratelimit-limit: 200 X-ratelimit-reset: 2017-11-02T12:31:28.675446  ```  In the example provided, 200 operations are allowed within a 1-minute time frame. Of those, there are 199 still available, because one has already been run. The total limit will be reset after 1 minute.  When the X-ratelimit-limit is reached, or in other words, when the X-ratelimit-remaining reaches zero, the API will give the error, HTTP 429 TOO MANY REQUESTS. If your application receives this error, you will need to wait until the time defined in X-ratelimit-reset has passed, to make another request.  *   **X-ratelimit-limit by product**       The *X-ratelimit limit* variations by product are the following:  *   **Real-Time Metrics:** 20 requests per minute. *   **Real-Time Purge:** 200 requests per minute; except for the Wildcard, which is 2000 a day.       > The rate-limit values are based on the client_id.  * * *  **Optional Parameters**  In this version, it is possible to include some optional parameters as part of the GET method, which can help and modify the form in which your data will be returned.  You can combine these parameters to get the result you want.  They are:  | Parameter | Description | Accepted values: | | --- | --- | --- | | order_by | Identifies which field the return should be sorted by. The default ordering is ascending. | Depends on the fields available from the endpoint structure | | sort | Defines which ordering to be used: ascending or descending. | asc  <br>  <br>desc | | page | Identifies which page should be returned, if the return is paginated. The default value is 1. | Page number. | | page_size | Identifies how many items should be returned per page. The default value is 10. | Desired number of items. |  * * *  **Request Exemple**  You can use one parameter, or a combination. See the example below, which uses all of them in the same request.  ``` GET /domains?order_by=name&page_size=20&sort=desc&page=3 Accept: application/json; version=3 Authorization: token 2909f3932069047f4736dc87e72baaddd19c9f75  ```  * * *  # Authentication  Authentication and authorization of operations via Azion API is done through Tokens.  The first step is to create the Token through authenticating a user registered in [Real-Time Manager](https://sso.azion.com/login).  * * *  ## Encoding Username and Password in Base64  Only token creation and cancelling operations are performed through Basic Authentication, that is, with a username and password. You can create and cancel the token through the API itself, but for that you need to encode your username and password in base64.  Base64 encoding can be done from the command line on a Unix terminal:  ``` $ echo 'user@domain:password'|base64 dXNlckBkb21haW46cGFzc3dvcmQK  ```  If you do not have a Unix terminal available, you can use the free online service at [https://www.base64encode.org/](https://www.base64encode.org/)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from edgeapplications import schemas  # noqa: F401


class ApplicationCacheResponseDetails(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "cache_by_cookies",
            "enable_query_string_sort",
            "l2_caching_enabled",
            "browser_cache_settings",
            "cdn_cache_settings",
            "query_string_fields",
            "name",
            "enable_caching_for_post",
            "cookie_names",
            "id",
            "cache_by_query_string",
            "browser_cache_settings_maximum_ttl",
            "cdn_cache_settings_maximum_ttl",
        }
        
        class properties:
            id = schemas.Int64Schema
            name = schemas.StrSchema
            browser_cache_settings = schemas.StrSchema
            browser_cache_settings_maximum_ttl = schemas.Int64Schema
            cdn_cache_settings = schemas.StrSchema
            cdn_cache_settings_maximum_ttl = schemas.Int64Schema
            cache_by_query_string = schemas.StrSchema
            
            
            class query_string_fields(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'query_string_fields':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            enable_query_string_sort = schemas.BoolSchema
            cache_by_cookies = schemas.StrSchema
            
            
            class cookie_names(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cookie_names':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            enable_caching_for_post = schemas.BoolSchema
            l2_caching_enabled = schemas.BoolSchema
            adaptive_delivery_action = schemas.StrSchema
            
            
            class device_group(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'device_group':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            enable_caching_for_options = schemas.BoolSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "browser_cache_settings": browser_cache_settings,
                "browser_cache_settings_maximum_ttl": browser_cache_settings_maximum_ttl,
                "cdn_cache_settings": cdn_cache_settings,
                "cdn_cache_settings_maximum_ttl": cdn_cache_settings_maximum_ttl,
                "cache_by_query_string": cache_by_query_string,
                "query_string_fields": query_string_fields,
                "enable_query_string_sort": enable_query_string_sort,
                "cache_by_cookies": cache_by_cookies,
                "cookie_names": cookie_names,
                "enable_caching_for_post": enable_caching_for_post,
                "l2_caching_enabled": l2_caching_enabled,
                "adaptive_delivery_action": adaptive_delivery_action,
                "device_group": device_group,
                "enable_caching_for_options": enable_caching_for_options,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    cache_by_cookies: MetaOapg.properties.cache_by_cookies
    enable_query_string_sort: MetaOapg.properties.enable_query_string_sort
    l2_caching_enabled: MetaOapg.properties.l2_caching_enabled
    browser_cache_settings: MetaOapg.properties.browser_cache_settings
    cdn_cache_settings: MetaOapg.properties.cdn_cache_settings
    query_string_fields: MetaOapg.properties.query_string_fields
    name: MetaOapg.properties.name
    enable_caching_for_post: MetaOapg.properties.enable_caching_for_post
    cookie_names: MetaOapg.properties.cookie_names
    id: MetaOapg.properties.id
    cache_by_query_string: MetaOapg.properties.cache_by_query_string
    browser_cache_settings_maximum_ttl: MetaOapg.properties.browser_cache_settings_maximum_ttl
    cdn_cache_settings_maximum_ttl: MetaOapg.properties.cdn_cache_settings_maximum_ttl
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cache_by_cookies"]) -> MetaOapg.properties.cache_by_cookies: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_query_string_sort"]) -> MetaOapg.properties.enable_query_string_sort: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["l2_caching_enabled"]) -> MetaOapg.properties.l2_caching_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["browser_cache_settings"]) -> MetaOapg.properties.browser_cache_settings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cdn_cache_settings"]) -> MetaOapg.properties.cdn_cache_settings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["query_string_fields"]) -> MetaOapg.properties.query_string_fields: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_caching_for_post"]) -> MetaOapg.properties.enable_caching_for_post: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cookie_names"]) -> MetaOapg.properties.cookie_names: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cache_by_query_string"]) -> MetaOapg.properties.cache_by_query_string: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["browser_cache_settings_maximum_ttl"]) -> MetaOapg.properties.browser_cache_settings_maximum_ttl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cdn_cache_settings_maximum_ttl"]) -> MetaOapg.properties.cdn_cache_settings_maximum_ttl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["adaptive_delivery_action"]) -> MetaOapg.properties.adaptive_delivery_action: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_group"]) -> MetaOapg.properties.device_group: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_caching_for_options"]) -> MetaOapg.properties.enable_caching_for_options: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cache_by_cookies"], typing_extensions.Literal["enable_query_string_sort"], typing_extensions.Literal["l2_caching_enabled"], typing_extensions.Literal["browser_cache_settings"], typing_extensions.Literal["cdn_cache_settings"], typing_extensions.Literal["query_string_fields"], typing_extensions.Literal["name"], typing_extensions.Literal["enable_caching_for_post"], typing_extensions.Literal["cookie_names"], typing_extensions.Literal["id"], typing_extensions.Literal["cache_by_query_string"], typing_extensions.Literal["browser_cache_settings_maximum_ttl"], typing_extensions.Literal["cdn_cache_settings_maximum_ttl"], typing_extensions.Literal["adaptive_delivery_action"], typing_extensions.Literal["device_group"], typing_extensions.Literal["enable_caching_for_options"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cache_by_cookies"]) -> MetaOapg.properties.cache_by_cookies: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_query_string_sort"]) -> MetaOapg.properties.enable_query_string_sort: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["l2_caching_enabled"]) -> MetaOapg.properties.l2_caching_enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["browser_cache_settings"]) -> MetaOapg.properties.browser_cache_settings: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cdn_cache_settings"]) -> MetaOapg.properties.cdn_cache_settings: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["query_string_fields"]) -> MetaOapg.properties.query_string_fields: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_caching_for_post"]) -> MetaOapg.properties.enable_caching_for_post: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cookie_names"]) -> MetaOapg.properties.cookie_names: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cache_by_query_string"]) -> MetaOapg.properties.cache_by_query_string: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["browser_cache_settings_maximum_ttl"]) -> MetaOapg.properties.browser_cache_settings_maximum_ttl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cdn_cache_settings_maximum_ttl"]) -> MetaOapg.properties.cdn_cache_settings_maximum_ttl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["adaptive_delivery_action"]) -> typing.Union[MetaOapg.properties.adaptive_delivery_action, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_group"]) -> typing.Union[MetaOapg.properties.device_group, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_caching_for_options"]) -> typing.Union[MetaOapg.properties.enable_caching_for_options, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cache_by_cookies"], typing_extensions.Literal["enable_query_string_sort"], typing_extensions.Literal["l2_caching_enabled"], typing_extensions.Literal["browser_cache_settings"], typing_extensions.Literal["cdn_cache_settings"], typing_extensions.Literal["query_string_fields"], typing_extensions.Literal["name"], typing_extensions.Literal["enable_caching_for_post"], typing_extensions.Literal["cookie_names"], typing_extensions.Literal["id"], typing_extensions.Literal["cache_by_query_string"], typing_extensions.Literal["browser_cache_settings_maximum_ttl"], typing_extensions.Literal["cdn_cache_settings_maximum_ttl"], typing_extensions.Literal["adaptive_delivery_action"], typing_extensions.Literal["device_group"], typing_extensions.Literal["enable_caching_for_options"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        cache_by_cookies: typing.Union[MetaOapg.properties.cache_by_cookies, str, ],
        enable_query_string_sort: typing.Union[MetaOapg.properties.enable_query_string_sort, bool, ],
        l2_caching_enabled: typing.Union[MetaOapg.properties.l2_caching_enabled, bool, ],
        browser_cache_settings: typing.Union[MetaOapg.properties.browser_cache_settings, str, ],
        cdn_cache_settings: typing.Union[MetaOapg.properties.cdn_cache_settings, str, ],
        query_string_fields: typing.Union[MetaOapg.properties.query_string_fields, list, tuple, None, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        enable_caching_for_post: typing.Union[MetaOapg.properties.enable_caching_for_post, bool, ],
        cookie_names: typing.Union[MetaOapg.properties.cookie_names, list, tuple, None, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        cache_by_query_string: typing.Union[MetaOapg.properties.cache_by_query_string, str, ],
        browser_cache_settings_maximum_ttl: typing.Union[MetaOapg.properties.browser_cache_settings_maximum_ttl, decimal.Decimal, int, ],
        cdn_cache_settings_maximum_ttl: typing.Union[MetaOapg.properties.cdn_cache_settings_maximum_ttl, decimal.Decimal, int, ],
        adaptive_delivery_action: typing.Union[MetaOapg.properties.adaptive_delivery_action, str, schemas.Unset] = schemas.unset,
        device_group: typing.Union[MetaOapg.properties.device_group, list, tuple, schemas.Unset] = schemas.unset,
        enable_caching_for_options: typing.Union[MetaOapg.properties.enable_caching_for_options, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ApplicationCacheResponseDetails':
        return super().__new__(
            cls,
            *_args,
            cache_by_cookies=cache_by_cookies,
            enable_query_string_sort=enable_query_string_sort,
            l2_caching_enabled=l2_caching_enabled,
            browser_cache_settings=browser_cache_settings,
            cdn_cache_settings=cdn_cache_settings,
            query_string_fields=query_string_fields,
            name=name,
            enable_caching_for_post=enable_caching_for_post,
            cookie_names=cookie_names,
            id=id,
            cache_by_query_string=cache_by_query_string,
            browser_cache_settings_maximum_ttl=browser_cache_settings_maximum_ttl,
            cdn_cache_settings_maximum_ttl=cdn_cache_settings_maximum_ttl,
            adaptive_delivery_action=adaptive_delivery_action,
            device_group=device_group,
            enable_caching_for_options=enable_caching_for_options,
            _configuration=_configuration,
        )
