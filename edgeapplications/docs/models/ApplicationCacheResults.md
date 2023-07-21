# edgeapplications.model.application_cache_results.ApplicationCacheResults

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**enable_stale_cache** | bool,  | BoolClass,  |  | 
**cache_by_cookies** | str,  | str,  |  | 
**[device_group](#device_group)** | list, tuple,  | tuple,  |  | 
**enable_query_string_sort** | bool,  | BoolClass,  |  | 
**l2_caching_enabled** | bool,  | BoolClass,  |  | 
**browser_cache_settings** | str,  | str,  |  | 
**cdn_cache_settings** | str,  | str,  |  | 
**enable_caching_for_options** | bool,  | BoolClass,  |  | 
**adaptive_delivery_action** | str,  | str,  |  | 
**[query_string_fields](#query_string_fields)** | list, tuple,  | tuple,  |  | 
**name** | str,  | str,  |  | 
**enable_caching_for_post** | bool,  | BoolClass,  |  | 
**[cookie_names](#cookie_names)** | list, tuple,  | tuple,  |  | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**cache_by_query_string** | str,  | str,  |  | 
**l2_region** | str,  | str,  |  | 
**browser_cache_settings_maximum_ttl** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**cdn_cache_settings_maximum_ttl** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# query_string_fields

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# cookie_names

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# device_group

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

