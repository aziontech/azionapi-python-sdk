# ApplicationCacheCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**browser_cache_settings** | **str** |  | [optional] 
**browser_cache_settings_maximum_ttl** | **int** |  | [optional] 
**cdn_cache_settings** | **str** |  | [optional] 
**cdn_cache_settings_maximum_ttl** | **int** |  | [optional] 
**cache_by_query_string** | **str** |  | [optional] 
**query_string_fields** | **List[str]** |  | [optional] 
**enable_query_string_sort** | **bool** |  | [optional] 
**cache_by_cookies** | **str** |  | [optional] 
**cookie_names** | **List[str]** |  | [optional] 
**adaptive_delivery_action** | **str** |  | [optional] 
**device_group** | **List[int]** |  | [optional] 
**enable_caching_for_post** | **bool** |  | [optional] 
**l2_caching_enabled** | **bool** |  | [optional] 
**is_slice_configuration_enabled** | **bool** |  | [optional] 
**is_slice_edge_caching_enabled** | **bool** |  | [optional] 
**is_slice_l2_caching_enabled** | **bool** |  | [optional] 
**slice_configuration_range** | **int** |  | [optional] 
**enable_caching_for_options** | **bool** |  | [optional] 
**enable_stale_cache** | **bool** |  | [optional] 
**l2_region** | **str** |  | [optional] 

## Example

```python
from edgeapplications.models.application_cache_create_request import ApplicationCacheCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCacheCreateRequest from a JSON string
application_cache_create_request_instance = ApplicationCacheCreateRequest.from_json(json)
# print the JSON string representation of the object
print ApplicationCacheCreateRequest.to_json()

# convert the object into a dict
application_cache_create_request_dict = application_cache_create_request_instance.to_dict()
# create an instance of ApplicationCacheCreateRequest from a dict
application_cache_create_request_form_dict = application_cache_create_request.from_dict(application_cache_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


