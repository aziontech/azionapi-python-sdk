# CreateApplicationResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**ApplicationResultsCreate**](ApplicationResultsCreate.md) |  | 
**schema_version** | **int** |  | 

## Example

```python
from edgeapplications.models.create_application_result import CreateApplicationResult

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApplicationResult from a JSON string
create_application_result_instance = CreateApplicationResult.from_json(json)
# print the JSON string representation of the object
print CreateApplicationResult.to_json()

# convert the object into a dict
create_application_result_dict = create_application_result_instance.to_dict()
# create an instance of CreateApplicationResult from a dict
create_application_result_form_dict = create_application_result.from_dict(create_application_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


