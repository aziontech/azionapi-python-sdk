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


class OriginsResultResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "timeout_between_bytes",
            "addresses",
            "hmac_secret_key",
            "method",
            "origin_path",
            "hmac_region_name",
            "origin_protocol_policy",
            "hmac_access_key",
            "is_origin_redirection_enabled",
            "origin_id",
            "origin_type",
            "host_header",
            "origin_key",
            "name",
            "connection_timeout",
            "hmac_authentication",
        }
        
        class properties:
            origin_id = schemas.Int64Schema
            origin_key = schemas.StrSchema
            name = schemas.StrSchema
            origin_type = schemas.StrSchema
            
            
            class addresses(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['OriginsResultResponseAddresses']:
                        return OriginsResultResponseAddresses
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['OriginsResultResponseAddresses'], typing.List['OriginsResultResponseAddresses']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'addresses':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'OriginsResultResponseAddresses':
                    return super().__getitem__(i)
            origin_protocol_policy = schemas.StrSchema
            is_origin_redirection_enabled = schemas.BoolSchema
            host_header = schemas.StrSchema
            method = schemas.StrSchema
            origin_path = schemas.StrSchema
            connection_timeout = schemas.Int64Schema
            timeout_between_bytes = schemas.Int64Schema
            hmac_authentication = schemas.BoolSchema
            hmac_region_name = schemas.StrSchema
            hmac_access_key = schemas.StrSchema
            hmac_secret_key = schemas.StrSchema
            __annotations__ = {
                "origin_id": origin_id,
                "origin_key": origin_key,
                "name": name,
                "origin_type": origin_type,
                "addresses": addresses,
                "origin_protocol_policy": origin_protocol_policy,
                "is_origin_redirection_enabled": is_origin_redirection_enabled,
                "host_header": host_header,
                "method": method,
                "origin_path": origin_path,
                "connection_timeout": connection_timeout,
                "timeout_between_bytes": timeout_between_bytes,
                "hmac_authentication": hmac_authentication,
                "hmac_region_name": hmac_region_name,
                "hmac_access_key": hmac_access_key,
                "hmac_secret_key": hmac_secret_key,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    timeout_between_bytes: MetaOapg.properties.timeout_between_bytes
    addresses: MetaOapg.properties.addresses
    hmac_secret_key: MetaOapg.properties.hmac_secret_key
    method: MetaOapg.properties.method
    origin_path: MetaOapg.properties.origin_path
    hmac_region_name: MetaOapg.properties.hmac_region_name
    origin_protocol_policy: MetaOapg.properties.origin_protocol_policy
    hmac_access_key: MetaOapg.properties.hmac_access_key
    is_origin_redirection_enabled: MetaOapg.properties.is_origin_redirection_enabled
    origin_id: MetaOapg.properties.origin_id
    origin_type: MetaOapg.properties.origin_type
    host_header: MetaOapg.properties.host_header
    origin_key: MetaOapg.properties.origin_key
    name: MetaOapg.properties.name
    connection_timeout: MetaOapg.properties.connection_timeout
    hmac_authentication: MetaOapg.properties.hmac_authentication
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeout_between_bytes"]) -> MetaOapg.properties.timeout_between_bytes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addresses"]) -> MetaOapg.properties.addresses: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hmac_secret_key"]) -> MetaOapg.properties.hmac_secret_key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["method"]) -> MetaOapg.properties.method: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["origin_path"]) -> MetaOapg.properties.origin_path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hmac_region_name"]) -> MetaOapg.properties.hmac_region_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["origin_protocol_policy"]) -> MetaOapg.properties.origin_protocol_policy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hmac_access_key"]) -> MetaOapg.properties.hmac_access_key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_origin_redirection_enabled"]) -> MetaOapg.properties.is_origin_redirection_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["origin_id"]) -> MetaOapg.properties.origin_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["origin_type"]) -> MetaOapg.properties.origin_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["host_header"]) -> MetaOapg.properties.host_header: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["origin_key"]) -> MetaOapg.properties.origin_key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connection_timeout"]) -> MetaOapg.properties.connection_timeout: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hmac_authentication"]) -> MetaOapg.properties.hmac_authentication: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["timeout_between_bytes"], typing_extensions.Literal["addresses"], typing_extensions.Literal["hmac_secret_key"], typing_extensions.Literal["method"], typing_extensions.Literal["origin_path"], typing_extensions.Literal["hmac_region_name"], typing_extensions.Literal["origin_protocol_policy"], typing_extensions.Literal["hmac_access_key"], typing_extensions.Literal["is_origin_redirection_enabled"], typing_extensions.Literal["origin_id"], typing_extensions.Literal["origin_type"], typing_extensions.Literal["host_header"], typing_extensions.Literal["origin_key"], typing_extensions.Literal["name"], typing_extensions.Literal["connection_timeout"], typing_extensions.Literal["hmac_authentication"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeout_between_bytes"]) -> MetaOapg.properties.timeout_between_bytes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addresses"]) -> MetaOapg.properties.addresses: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hmac_secret_key"]) -> MetaOapg.properties.hmac_secret_key: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["method"]) -> MetaOapg.properties.method: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["origin_path"]) -> MetaOapg.properties.origin_path: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hmac_region_name"]) -> MetaOapg.properties.hmac_region_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["origin_protocol_policy"]) -> MetaOapg.properties.origin_protocol_policy: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hmac_access_key"]) -> MetaOapg.properties.hmac_access_key: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_origin_redirection_enabled"]) -> MetaOapg.properties.is_origin_redirection_enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["origin_id"]) -> MetaOapg.properties.origin_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["origin_type"]) -> MetaOapg.properties.origin_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["host_header"]) -> MetaOapg.properties.host_header: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["origin_key"]) -> MetaOapg.properties.origin_key: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connection_timeout"]) -> MetaOapg.properties.connection_timeout: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hmac_authentication"]) -> MetaOapg.properties.hmac_authentication: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["timeout_between_bytes"], typing_extensions.Literal["addresses"], typing_extensions.Literal["hmac_secret_key"], typing_extensions.Literal["method"], typing_extensions.Literal["origin_path"], typing_extensions.Literal["hmac_region_name"], typing_extensions.Literal["origin_protocol_policy"], typing_extensions.Literal["hmac_access_key"], typing_extensions.Literal["is_origin_redirection_enabled"], typing_extensions.Literal["origin_id"], typing_extensions.Literal["origin_type"], typing_extensions.Literal["host_header"], typing_extensions.Literal["origin_key"], typing_extensions.Literal["name"], typing_extensions.Literal["connection_timeout"], typing_extensions.Literal["hmac_authentication"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        timeout_between_bytes: typing.Union[MetaOapg.properties.timeout_between_bytes, decimal.Decimal, int, ],
        addresses: typing.Union[MetaOapg.properties.addresses, list, tuple, ],
        hmac_secret_key: typing.Union[MetaOapg.properties.hmac_secret_key, str, ],
        method: typing.Union[MetaOapg.properties.method, str, ],
        origin_path: typing.Union[MetaOapg.properties.origin_path, str, ],
        hmac_region_name: typing.Union[MetaOapg.properties.hmac_region_name, str, ],
        origin_protocol_policy: typing.Union[MetaOapg.properties.origin_protocol_policy, str, ],
        hmac_access_key: typing.Union[MetaOapg.properties.hmac_access_key, str, ],
        is_origin_redirection_enabled: typing.Union[MetaOapg.properties.is_origin_redirection_enabled, bool, ],
        origin_id: typing.Union[MetaOapg.properties.origin_id, decimal.Decimal, int, ],
        origin_type: typing.Union[MetaOapg.properties.origin_type, str, ],
        host_header: typing.Union[MetaOapg.properties.host_header, str, ],
        origin_key: typing.Union[MetaOapg.properties.origin_key, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        connection_timeout: typing.Union[MetaOapg.properties.connection_timeout, decimal.Decimal, int, ],
        hmac_authentication: typing.Union[MetaOapg.properties.hmac_authentication, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OriginsResultResponse':
        return super().__new__(
            cls,
            *_args,
            timeout_between_bytes=timeout_between_bytes,
            addresses=addresses,
            hmac_secret_key=hmac_secret_key,
            method=method,
            origin_path=origin_path,
            hmac_region_name=hmac_region_name,
            origin_protocol_policy=origin_protocol_policy,
            hmac_access_key=hmac_access_key,
            is_origin_redirection_enabled=is_origin_redirection_enabled,
            origin_id=origin_id,
            origin_type=origin_type,
            host_header=host_header,
            origin_key=origin_key,
            name=name,
            connection_timeout=connection_timeout,
            hmac_authentication=hmac_authentication,
            _configuration=_configuration,
        )

from edgeapplications.model.origins_result_response_addresses import OriginsResultResponseAddresses
