# ApplicationCachePatchResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**ApplicationCacheResponseDetails**](ApplicationCacheResponseDetails.md) |  | [optional] 
**schema_version** | **int** |  | [optional] 

## Example

```python
from edgeapplications.models.application_cache_patch_response import ApplicationCachePatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCachePatchResponse from a JSON string
application_cache_patch_response_instance = ApplicationCachePatchResponse.from_json(json)
# print the JSON string representation of the object
print ApplicationCachePatchResponse.to_json()

# convert the object into a dict
application_cache_patch_response_dict = application_cache_patch_response_instance.to_dict()
# create an instance of ApplicationCachePatchResponse from a dict
application_cache_patch_response_form_dict = application_cache_patch_response.from_dict(application_cache_patch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


