# ApplicationCacheGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**total_pages** | **int** |  | 
**schema_version** | **int** |  | 
**links** | [**ApplicationLinks**](ApplicationLinks.md) |  | 
**results** | [**List[ApplicationCacheResults]**](ApplicationCacheResults.md) |  | 

## Example

```python
from edgeapplications.models.application_cache_get_response import ApplicationCacheGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCacheGetResponse from a JSON string
application_cache_get_response_instance = ApplicationCacheGetResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationCacheGetResponse.to_json())

# convert the object into a dict
application_cache_get_response_dict = application_cache_get_response_instance.to_dict()
# create an instance of ApplicationCacheGetResponse from a dict
application_cache_get_response_from_dict = ApplicationCacheGetResponse.from_dict(application_cache_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


