# EdgeFunctionsInstanceResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**EdgeFunctionsInstance**](EdgeFunctionsInstance.md) |  | [optional] 
**schema_version** | **float** |  | [optional] 

## Example

```python
from edgefunctionsinstance_edgefirewall.models.edge_functions_instance_response import EdgeFunctionsInstanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeFunctionsInstanceResponse from a JSON string
edge_functions_instance_response_instance = EdgeFunctionsInstanceResponse.from_json(json)
# print the JSON string representation of the object
print EdgeFunctionsInstanceResponse.to_json()

# convert the object into a dict
edge_functions_instance_response_dict = edge_functions_instance_response_instance.to_dict()
# create an instance of EdgeFunctionsInstanceResponse from a dict
edge_functions_instance_response_form_dict = edge_functions_instance_response.from_dict(edge_functions_instance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


