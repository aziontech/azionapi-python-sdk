# VariableGet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [readonly] 
**key** | **str** |  | 
**value** | **str** | Given the *incoming* primitive data, return the value for this field that should be validated and transformed to a native value. | [readonly] 
**secret** | **bool** |  | [readonly] 
**last_editor** | **str** |  | [readonly] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from variables.models.variable_get import VariableGet

# TODO update the JSON string below
json = "{}"
# create an instance of VariableGet from a JSON string
variable_get_instance = VariableGet.from_json(json)
# print the JSON string representation of the object
print VariableGet.to_json()

# convert the object into a dict
variable_get_dict = variable_get_instance.to_dict()
# create an instance of VariableGet from a dict
variable_get_form_dict = variable_get.from_dict(variable_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


