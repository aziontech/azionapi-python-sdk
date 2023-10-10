# EdgeFunctionsInstance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**last_editor** | **str** |  | [optional] 
**last_modified** | **str** |  | [optional] 
**json_args** | **object** |  | [optional] 
**edge_function** | **int** |  | [optional] 

## Example

```python
from edgefunctionsinstance_edgefirewall.models.edge_functions_instance import EdgeFunctionsInstance

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeFunctionsInstance from a JSON string
edge_functions_instance_instance = EdgeFunctionsInstance.from_json(json)
# print the JSON string representation of the object
print EdgeFunctionsInstance.to_json()

# convert the object into a dict
edge_functions_instance_dict = edge_functions_instance_instance.to_dict()
# create an instance of EdgeFunctionsInstance from a dict
edge_functions_instance_form_dict = edge_functions_instance.from_dict(edge_functions_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


