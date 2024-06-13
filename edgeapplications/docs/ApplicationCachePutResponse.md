# ApplicationCachePutResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**ApplicationCacheResponseDetails**](ApplicationCacheResponseDetails.md) |  | 
**schema_version** | **int** |  | 

## Example

```python
from edgeapplications.models.application_cache_put_response import ApplicationCachePutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCachePutResponse from a JSON string
application_cache_put_response_instance = ApplicationCachePutResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationCachePutResponse.to_json())

# convert the object into a dict
application_cache_put_response_dict = application_cache_put_response_instance.to_dict()
# create an instance of ApplicationCachePutResponse from a dict
application_cache_put_response_from_dict = ApplicationCachePutResponse.from_dict(application_cache_put_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


