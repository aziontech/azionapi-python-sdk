# ApplicationCacheCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**ApplicationCacheCreateResults**](ApplicationCacheCreateResults.md) |  | [optional] 
**schema_version** | **int** |  | [optional] 

## Example

```python
from edgeapplications.models.application_cache_create_response import ApplicationCacheCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCacheCreateResponse from a JSON string
application_cache_create_response_instance = ApplicationCacheCreateResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationCacheCreateResponse.to_json())

# convert the object into a dict
application_cache_create_response_dict = application_cache_create_response_instance.to_dict()
# create an instance of ApplicationCacheCreateResponse from a dict
application_cache_create_response_from_dict = ApplicationCacheCreateResponse.from_dict(application_cache_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


