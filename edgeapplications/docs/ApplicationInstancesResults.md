# ApplicationInstancesResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**edge_function_id** | **int** |  | 
**name** | **str** |  | 
**args** | **object** |  | 

## Example

```python
from edgeapplications.models.application_instances_results import ApplicationInstancesResults

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationInstancesResults from a JSON string
application_instances_results_instance = ApplicationInstancesResults.from_json(json)
# print the JSON string representation of the object
print(ApplicationInstancesResults.to_json())

# convert the object into a dict
application_instances_results_dict = application_instances_results_instance.to_dict()
# create an instance of ApplicationInstancesResults from a dict
application_instances_results_from_dict = ApplicationInstancesResults.from_dict(application_instances_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


