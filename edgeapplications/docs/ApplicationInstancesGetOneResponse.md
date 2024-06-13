# ApplicationInstancesGetOneResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**ApplicationInstancesResults**](ApplicationInstancesResults.md) |  | 
**schema_version** | **int** |  | 

## Example

```python
from edgeapplications.models.application_instances_get_one_response import ApplicationInstancesGetOneResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationInstancesGetOneResponse from a JSON string
application_instances_get_one_response_instance = ApplicationInstancesGetOneResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationInstancesGetOneResponse.to_json())

# convert the object into a dict
application_instances_get_one_response_dict = application_instances_get_one_response_instance.to_dict()
# create an instance of ApplicationInstancesGetOneResponse from a dict
application_instances_get_one_response_from_dict = ApplicationInstancesGetOneResponse.from_dict(application_instances_get_one_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


