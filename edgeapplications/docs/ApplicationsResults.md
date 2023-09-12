# ApplicationsResults


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**debug_rules** | **bool** |  | 
**last_editor** | **str** |  | 
**last_modified** | **str** |  | 
**active** | **bool** |  | 
**origins** | [**List[ApplicationOrigins]**](ApplicationOrigins.md) |  | 

## Example

```python
from edgeapplications.models.applications_results import ApplicationsResults

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationsResults from a JSON string
applications_results_instance = ApplicationsResults.from_json(json)
# print the JSON string representation of the object
print ApplicationsResults.to_json()

# convert the object into a dict
applications_results_dict = applications_results_instance.to_dict()
# create an instance of ApplicationsResults from a dict
applications_results_form_dict = applications_results.from_dict(applications_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


