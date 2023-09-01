# TemplateResults


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Template]**](Template.md) |  | [optional] 
**schema_version** | **float** |  | [optional] 

## Example

```python
from data_streaming.models.template_results import TemplateResults

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateResults from a JSON string
template_results_instance = TemplateResults.from_json(json)
# print the JSON string representation of the object
print TemplateResults.to_json()

# convert the object into a dict
template_results_dict = template_results_instance.to_dict()
# create an instance of TemplateResults from a dict
template_results_form_dict = template_results.from_dict(template_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


