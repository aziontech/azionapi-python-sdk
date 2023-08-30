# VariableCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**value** | **str** |  | 
**secret** | **bool** |  | [optional] 

## Example

```python
from variables.models.variable_create import VariableCreate

# TODO update the JSON string below
json = "{}"
# create an instance of VariableCreate from a JSON string
variable_create_instance = VariableCreate.from_json(json)
# print the JSON string representation of the object
print VariableCreate.to_json()

# convert the object into a dict
variable_create_dict = variable_create_instance.to_dict()
# create an instance of VariableCreate from a dict
variable_create_form_dict = variable_create.from_dict(variable_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


