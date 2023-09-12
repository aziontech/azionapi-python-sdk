# ApplicationInstancesGetResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**total_pages** | **int** |  | 
**schema_version** | **int** |  | 
**links** | [**ApplicationLinks**](ApplicationLinks.md) |  | 
**results** | [**List[ApplicationInstancesResults]**](ApplicationInstancesResults.md) |  | 

## Example

```python
from edgeapplications.models.application_instances_get_response import ApplicationInstancesGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationInstancesGetResponse from a JSON string
application_instances_get_response_instance = ApplicationInstancesGetResponse.from_json(json)
# print the JSON string representation of the object
print ApplicationInstancesGetResponse.to_json()

# convert the object into a dict
application_instances_get_response_dict = application_instances_get_response_instance.to_dict()
# create an instance of ApplicationInstancesGetResponse from a dict
application_instances_get_response_form_dict = application_instances_get_response.from_dict(application_instances_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


