# ListEdgeFunctionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**schema_version** | **int** |  | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 
**results** | [**List[Results]**](Results.md) |  | [optional] 

## Example

```python
from edgefunctions.models.list_edge_function_response import ListEdgeFunctionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListEdgeFunctionResponse from a JSON string
list_edge_function_response_instance = ListEdgeFunctionResponse.from_json(json)
# print the JSON string representation of the object
print(ListEdgeFunctionResponse.to_json())

# convert the object into a dict
list_edge_function_response_dict = list_edge_function_response_instance.to_dict()
# create an instance of ListEdgeFunctionResponse from a dict
list_edge_function_response_from_dict = ListEdgeFunctionResponse.from_dict(list_edge_function_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


