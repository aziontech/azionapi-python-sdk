# ApplicationCachePutRequest


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
from edgeapplications.models.application_cache_put_request import ApplicationCachePutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCachePutRequest from a JSON string
application_cache_put_request_instance = ApplicationCachePutRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationCachePutRequest.to_json())

# convert the object into a dict
application_cache_put_request_dict = application_cache_put_request_instance.to_dict()
# create an instance of ApplicationCachePutRequest from a dict
application_cache_put_request_from_dict = ApplicationCachePutRequest.from_dict(application_cache_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


