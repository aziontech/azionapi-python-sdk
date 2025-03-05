# CreateEdgeFunctionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**json_args** | [**CreateEdgeFunctionRequestJsonArgs**](CreateEdgeFunctionRequestJsonArgs.md) |  | [optional] 
**initiator_type** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**is_proprietary_code** | **bool** |  | [optional] 

## Example

```python
from edgefunctions.models.create_edge_function_request import CreateEdgeFunctionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEdgeFunctionRequest from a JSON string
create_edge_function_request_instance = CreateEdgeFunctionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateEdgeFunctionRequest.to_json())

# convert the object into a dict
create_edge_function_request_dict = create_edge_function_request_instance.to_dict()
# create an instance of CreateEdgeFunctionRequest from a dict
create_edge_function_request_from_dict = CreateEdgeFunctionRequest.from_dict(create_edge_function_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


