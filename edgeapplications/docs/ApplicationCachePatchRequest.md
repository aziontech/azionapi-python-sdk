# ApplicationCachePatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**browser_cache_settings** | **str** |  | [optional] 
**browser_cache_settings_maximum_ttl** | **int** |  | [optional] 
**cdn_cache_settings** | **str** |  | [optional] 
**adaptive_delivery_action** | **str** |  | [optional] 
**enable_caching_for_options** | **bool** |  | [optional] 
**cdn_cache_settings_maximum_ttl** | **int** |  | [optional] 
**cache_by_query_string** | **str** |  | [optional] 
**query_string_fields** | **List[str]** |  | [optional] 
**enable_query_string_sort** | **bool** |  | [optional] 
**cache_by_cookies** | **str** |  | [optional] 
**cookie_names** | **List[str]** |  | [optional] 
**enable_caching_for_post** | **bool** |  | [optional] 
**l2_caching_enabled** | **bool** |  | [optional] 
**is_slice_configuration_enabled** | **bool** |  | [optional] 
**is_slice_edge_caching_enabled** | **bool** |  | [optional] 
**is_slice_l2_caching_enabled** | **bool** |  | [optional] 
**slice_configuration_range** | **int** |  | [optional] 

## Example

```python
from edgeapplications.models.application_cache_patch_request import ApplicationCachePatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCachePatchRequest from a JSON string
application_cache_patch_request_instance = ApplicationCachePatchRequest.from_json(json)
# print the JSON string representation of the object
print ApplicationCachePatchRequest.to_json()

# convert the object into a dict
application_cache_patch_request_dict = application_cache_patch_request_instance.to_dict()
# create an instance of ApplicationCachePatchRequest from a dict
application_cache_patch_request_form_dict = application_cache_patch_request.from_dict(application_cache_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


