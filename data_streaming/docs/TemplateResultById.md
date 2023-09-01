# TemplateResultById


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**Template**](Template.md) |  | [optional] 
**schema_version** | **float** |  | [optional] 

## Example

```python
from data_streaming.models.template_result_by_id import TemplateResultById

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateResultById from a JSON string
template_result_by_id_instance = TemplateResultById.from_json(json)
# print the JSON string representation of the object
print TemplateResultById.to_json()

# convert the object into a dict
template_result_by_id_dict = template_result_by_id_instance.to_dict()
# create an instance of TemplateResultById from a dict
template_result_by_id_form_dict = template_result_by_id.from_dict(template_result_by_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


