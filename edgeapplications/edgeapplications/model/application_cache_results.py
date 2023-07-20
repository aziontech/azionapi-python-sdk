# coding: utf-8

"""
    Edge Application API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.0.0
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


class ApplicationCacheResults(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "enable_stale_cache",
            "cache_by_cookies",
            "device_group",
            "enable_query_string_sort",
            "l2_caching_enabled",
            "browser_cache_settings",
            "cdn_cache_settings",
            "enable_caching_for_options",
            "adaptive_delivery_action",
            "query_string_fields",
            "name",
            "enable_caching_for_post",
            "cookie_names",
            "id",
            "cache_by_query_string",
            "l2_region",
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
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'query_string_fields':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            enable_query_string_sort = schemas.BoolSchema
            cache_by_cookies = schemas.StrSchema
            
            
            class cookie_names(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cookie_names':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
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
            enable_caching_for_post = schemas.BoolSchema
            l2_caching_enabled = schemas.BoolSchema
            enable_caching_for_options = schemas.BoolSchema
            enable_stale_cache = schemas.BoolSchema
            l2_region = schemas.StrSchema
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
                "adaptive_delivery_action": adaptive_delivery_action,
                "device_group": device_group,
                "enable_caching_for_post": enable_caching_for_post,
                "l2_caching_enabled": l2_caching_enabled,
                "enable_caching_for_options": enable_caching_for_options,
                "enable_stale_cache": enable_stale_cache,
                "l2_region": l2_region,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    enable_stale_cache: MetaOapg.properties.enable_stale_cache
    cache_by_cookies: MetaOapg.properties.cache_by_cookies
    device_group: MetaOapg.properties.device_group
    enable_query_string_sort: MetaOapg.properties.enable_query_string_sort
    l2_caching_enabled: MetaOapg.properties.l2_caching_enabled
    browser_cache_settings: MetaOapg.properties.browser_cache_settings
    cdn_cache_settings: MetaOapg.properties.cdn_cache_settings
    enable_caching_for_options: MetaOapg.properties.enable_caching_for_options
    adaptive_delivery_action: MetaOapg.properties.adaptive_delivery_action
    query_string_fields: MetaOapg.properties.query_string_fields
    name: MetaOapg.properties.name
    enable_caching_for_post: MetaOapg.properties.enable_caching_for_post
    cookie_names: MetaOapg.properties.cookie_names
    id: MetaOapg.properties.id
    cache_by_query_string: MetaOapg.properties.cache_by_query_string
    l2_region: MetaOapg.properties.l2_region
    browser_cache_settings_maximum_ttl: MetaOapg.properties.browser_cache_settings_maximum_ttl
    cdn_cache_settings_maximum_ttl: MetaOapg.properties.cdn_cache_settings_maximum_ttl
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_stale_cache"]) -> MetaOapg.properties.enable_stale_cache: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cache_by_cookies"]) -> MetaOapg.properties.cache_by_cookies: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_group"]) -> MetaOapg.properties.device_group: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_query_string_sort"]) -> MetaOapg.properties.enable_query_string_sort: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["l2_caching_enabled"]) -> MetaOapg.properties.l2_caching_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["browser_cache_settings"]) -> MetaOapg.properties.browser_cache_settings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cdn_cache_settings"]) -> MetaOapg.properties.cdn_cache_settings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_caching_for_options"]) -> MetaOapg.properties.enable_caching_for_options: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["adaptive_delivery_action"]) -> MetaOapg.properties.adaptive_delivery_action: ...
    
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
    def __getitem__(self, name: typing_extensions.Literal["l2_region"]) -> MetaOapg.properties.l2_region: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["browser_cache_settings_maximum_ttl"]) -> MetaOapg.properties.browser_cache_settings_maximum_ttl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cdn_cache_settings_maximum_ttl"]) -> MetaOapg.properties.cdn_cache_settings_maximum_ttl: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["enable_stale_cache"], typing_extensions.Literal["cache_by_cookies"], typing_extensions.Literal["device_group"], typing_extensions.Literal["enable_query_string_sort"], typing_extensions.Literal["l2_caching_enabled"], typing_extensions.Literal["browser_cache_settings"], typing_extensions.Literal["cdn_cache_settings"], typing_extensions.Literal["enable_caching_for_options"], typing_extensions.Literal["adaptive_delivery_action"], typing_extensions.Literal["query_string_fields"], typing_extensions.Literal["name"], typing_extensions.Literal["enable_caching_for_post"], typing_extensions.Literal["cookie_names"], typing_extensions.Literal["id"], typing_extensions.Literal["cache_by_query_string"], typing_extensions.Literal["l2_region"], typing_extensions.Literal["browser_cache_settings_maximum_ttl"], typing_extensions.Literal["cdn_cache_settings_maximum_ttl"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_stale_cache"]) -> MetaOapg.properties.enable_stale_cache: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cache_by_cookies"]) -> MetaOapg.properties.cache_by_cookies: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_group"]) -> MetaOapg.properties.device_group: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_query_string_sort"]) -> MetaOapg.properties.enable_query_string_sort: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["l2_caching_enabled"]) -> MetaOapg.properties.l2_caching_enabled: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["browser_cache_settings"]) -> MetaOapg.properties.browser_cache_settings: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cdn_cache_settings"]) -> MetaOapg.properties.cdn_cache_settings: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_caching_for_options"]) -> MetaOapg.properties.enable_caching_for_options: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["adaptive_delivery_action"]) -> MetaOapg.properties.adaptive_delivery_action: ...
    
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
    def get_item_oapg(self, name: typing_extensions.Literal["l2_region"]) -> MetaOapg.properties.l2_region: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["browser_cache_settings_maximum_ttl"]) -> MetaOapg.properties.browser_cache_settings_maximum_ttl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cdn_cache_settings_maximum_ttl"]) -> MetaOapg.properties.cdn_cache_settings_maximum_ttl: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["enable_stale_cache"], typing_extensions.Literal["cache_by_cookies"], typing_extensions.Literal["device_group"], typing_extensions.Literal["enable_query_string_sort"], typing_extensions.Literal["l2_caching_enabled"], typing_extensions.Literal["browser_cache_settings"], typing_extensions.Literal["cdn_cache_settings"], typing_extensions.Literal["enable_caching_for_options"], typing_extensions.Literal["adaptive_delivery_action"], typing_extensions.Literal["query_string_fields"], typing_extensions.Literal["name"], typing_extensions.Literal["enable_caching_for_post"], typing_extensions.Literal["cookie_names"], typing_extensions.Literal["id"], typing_extensions.Literal["cache_by_query_string"], typing_extensions.Literal["l2_region"], typing_extensions.Literal["browser_cache_settings_maximum_ttl"], typing_extensions.Literal["cdn_cache_settings_maximum_ttl"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        enable_stale_cache: typing.Union[MetaOapg.properties.enable_stale_cache, bool, ],
        cache_by_cookies: typing.Union[MetaOapg.properties.cache_by_cookies, str, ],
        device_group: typing.Union[MetaOapg.properties.device_group, list, tuple, ],
        enable_query_string_sort: typing.Union[MetaOapg.properties.enable_query_string_sort, bool, ],
        l2_caching_enabled: typing.Union[MetaOapg.properties.l2_caching_enabled, bool, ],
        browser_cache_settings: typing.Union[MetaOapg.properties.browser_cache_settings, str, ],
        cdn_cache_settings: typing.Union[MetaOapg.properties.cdn_cache_settings, str, ],
        enable_caching_for_options: typing.Union[MetaOapg.properties.enable_caching_for_options, bool, ],
        adaptive_delivery_action: typing.Union[MetaOapg.properties.adaptive_delivery_action, str, ],
        query_string_fields: typing.Union[MetaOapg.properties.query_string_fields, list, tuple, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        enable_caching_for_post: typing.Union[MetaOapg.properties.enable_caching_for_post, bool, ],
        cookie_names: typing.Union[MetaOapg.properties.cookie_names, list, tuple, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        cache_by_query_string: typing.Union[MetaOapg.properties.cache_by_query_string, str, ],
        l2_region: typing.Union[MetaOapg.properties.l2_region, str, ],
        browser_cache_settings_maximum_ttl: typing.Union[MetaOapg.properties.browser_cache_settings_maximum_ttl, decimal.Decimal, int, ],
        cdn_cache_settings_maximum_ttl: typing.Union[MetaOapg.properties.cdn_cache_settings_maximum_ttl, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ApplicationCacheResults':
        return super().__new__(
            cls,
            *_args,
            enable_stale_cache=enable_stale_cache,
            cache_by_cookies=cache_by_cookies,
            device_group=device_group,
            enable_query_string_sort=enable_query_string_sort,
            l2_caching_enabled=l2_caching_enabled,
            browser_cache_settings=browser_cache_settings,
            cdn_cache_settings=cdn_cache_settings,
            enable_caching_for_options=enable_caching_for_options,
            adaptive_delivery_action=adaptive_delivery_action,
            query_string_fields=query_string_fields,
            name=name,
            enable_caching_for_post=enable_caching_for_post,
            cookie_names=cookie_names,
            id=id,
            cache_by_query_string=cache_by_query_string,
            l2_region=l2_region,
            browser_cache_settings_maximum_ttl=browser_cache_settings_maximum_ttl,
            cdn_cache_settings_maximum_ttl=cdn_cache_settings_maximum_ttl,
            _configuration=_configuration,
        )
