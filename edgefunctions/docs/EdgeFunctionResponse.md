# EdgeFunctionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**Results**](Results.md) |  | [optional] 
**schema_version** | **float** |  | [optional] 

## Example

```python
from edgefunctions.models.edge_function_response import EdgeFunctionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeFunctionResponse from a JSON string
edge_function_response_instance = EdgeFunctionResponse.from_json(json)
# print the JSON string representation of the object
print(EdgeFunctionResponse.to_json())

# convert the object into a dict
edge_function_response_dict = edge_function_response_instance.to_dict()
# create an instance of EdgeFunctionResponse from a dict
edge_function_response_from_dict = EdgeFunctionResponse.from_dict(edge_function_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


