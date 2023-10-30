# PutEdgeFunctionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**json_args** | **object** |  | [optional] 
**active** | **bool** |  | [optional] 
**initiator_type** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**is_proprietary_code** | **bool** |  | [optional] 

## Example

```python
from edgefunctions.models.put_edge_function_request import PutEdgeFunctionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutEdgeFunctionRequest from a JSON string
put_edge_function_request_instance = PutEdgeFunctionRequest.from_json(json)
# print the JSON string representation of the object
print PutEdgeFunctionRequest.to_json()

# convert the object into a dict
put_edge_function_request_dict = put_edge_function_request_instance.to_dict()
# create an instance of PutEdgeFunctionRequest from a dict
put_edge_function_request_form_dict = put_edge_function_request.from_dict(put_edge_function_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


