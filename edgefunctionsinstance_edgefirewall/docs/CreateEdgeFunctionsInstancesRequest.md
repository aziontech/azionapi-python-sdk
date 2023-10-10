# CreateEdgeFunctionsInstancesRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**edge_function** | **int** |  | [optional] 
**json_args** | **object** |  | [optional] 

## Example

```python
from edgefunctionsinstance_edgefirewall.models.create_edge_functions_instances_request import CreateEdgeFunctionsInstancesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEdgeFunctionsInstancesRequest from a JSON string
create_edge_functions_instances_request_instance = CreateEdgeFunctionsInstancesRequest.from_json(json)
# print the JSON string representation of the object
print CreateEdgeFunctionsInstancesRequest.to_json()

# convert the object into a dict
create_edge_functions_instances_request_dict = create_edge_functions_instances_request_instance.to_dict()
# create an instance of CreateEdgeFunctionsInstancesRequest from a dict
create_edge_functions_instances_request_form_dict = create_edge_functions_instances_request.from_dict(create_edge_functions_instances_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


