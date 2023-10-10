# ListEdgeFunctionsInstancesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**schema_version** | **int** |  | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 
**results** | [**List[EdgeFunctionsInstance]**](EdgeFunctionsInstance.md) |  | [optional] 

## Example

```python
from edgefunctionsinstance_edgefirewall.models.list_edge_functions_instances_response import ListEdgeFunctionsInstancesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListEdgeFunctionsInstancesResponse from a JSON string
list_edge_functions_instances_response_instance = ListEdgeFunctionsInstancesResponse.from_json(json)
# print the JSON string representation of the object
print ListEdgeFunctionsInstancesResponse.to_json()

# convert the object into a dict
list_edge_functions_instances_response_dict = list_edge_functions_instances_response_instance.to_dict()
# create an instance of ListEdgeFunctionsInstancesResponse from a dict
list_edge_functions_instances_response_form_dict = list_edge_functions_instances_response.from_dict(list_edge_functions_instances_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


