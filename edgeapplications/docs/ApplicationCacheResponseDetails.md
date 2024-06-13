# ApplicationCacheResponseDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**browser_cache_settings** | **str** |  | 
**browser_cache_settings_maximum_ttl** | **int** |  | 
**cdn_cache_settings** | **str** |  | 
**cdn_cache_settings_maximum_ttl** | **int** |  | 
**cache_by_query_string** | **str** |  | 
**query_string_fields** | **List[str]** |  | 
**enable_query_string_sort** | **bool** |  | 
**cache_by_cookies** | **str** |  | 
**cookie_names** | **List[str]** |  | 
**adaptive_delivery_action** | **str** |  | [optional] 
**device_group** | **List[int]** |  | [optional] 
**enable_caching_for_post** | **bool** |  | 
**enable_caching_for_options** | **bool** |  | [optional] 
**l2_caching_enabled** | **bool** |  | 
**is_slice_configuration_enabled** | **bool** |  | [optional] 
**is_slice_edge_caching_enabled** | **bool** |  | [optional] 
**is_slice_l2_caching_enabled** | **bool** |  | [optional] 
**slice_configuration_range** | **int** |  | [optional] 
**enable_stale_cache** | **bool** |  | [optional] 
**l2_region** | **str** |  | [optional] 

## Example

```python
from edgeapplications.models.application_cache_response_details import ApplicationCacheResponseDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCacheResponseDetails from a JSON string
application_cache_response_details_instance = ApplicationCacheResponseDetails.from_json(json)
# print the JSON string representation of the object
print(ApplicationCacheResponseDetails.to_json())

# convert the object into a dict
application_cache_response_details_dict = application_cache_response_details_instance.to_dict()
# create an instance of ApplicationCacheResponseDetails from a dict
application_cache_response_details_from_dict = ApplicationCacheResponseDetails.from_dict(application_cache_response_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


