# ApplicationCacheResults


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
**adaptive_delivery_action** | **str** |  | 
**device_group** | **List[int]** |  | 
**enable_caching_for_post** | **bool** |  | 
**l2_caching_enabled** | **bool** |  | 
**is_slice_configuration_enabled** | **bool** |  | [optional] 
**is_slice_edge_caching_enabled** | **bool** |  | [optional] 
**is_slice_l2_caching_enabled** | **bool** |  | [optional] 
**slice_configuration_range** | **int** |  | [optional] 
**enable_caching_for_options** | **bool** |  | 
**enable_stale_cache** | **bool** |  | 
**l2_region** | **str** |  | 

## Example

```python
from edgeapplications.models.application_cache_results import ApplicationCacheResults

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCacheResults from a JSON string
application_cache_results_instance = ApplicationCacheResults.from_json(json)
# print the JSON string representation of the object
print ApplicationCacheResults.to_json()

# convert the object into a dict
application_cache_results_dict = application_cache_results_instance.to_dict()
# create an instance of ApplicationCacheResults from a dict
application_cache_results_form_dict = application_cache_results.from_dict(application_cache_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


