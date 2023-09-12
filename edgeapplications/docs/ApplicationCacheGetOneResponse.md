# ApplicationCacheGetOneResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**ApplicationCacheResults**](ApplicationCacheResults.md) |  | 
**schema_version** | **int** |  | 

## Example

```python
from edgeapplications.models.application_cache_get_one_response import ApplicationCacheGetOneResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCacheGetOneResponse from a JSON string
application_cache_get_one_response_instance = ApplicationCacheGetOneResponse.from_json(json)
# print the JSON string representation of the object
print ApplicationCacheGetOneResponse.to_json()

# convert the object into a dict
application_cache_get_one_response_dict = application_cache_get_one_response_instance.to_dict()
# create an instance of ApplicationCacheGetOneResponse from a dict
application_cache_get_one_response_form_dict = application_cache_get_one_response.from_dict(application_cache_get_one_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


