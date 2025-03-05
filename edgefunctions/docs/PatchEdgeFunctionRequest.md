# PatchEdgeFunctionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**json_args** | **object** |  | [optional] 
**active** | **bool** |  | [optional] 
**is_proprietary_code** | **bool** |  | [optional] 

## Example

```python
from edgefunctions.models.patch_edge_function_request import PatchEdgeFunctionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchEdgeFunctionRequest from a JSON string
patch_edge_function_request_instance = PatchEdgeFunctionRequest.from_json(json)
# print the JSON string representation of the object
print(PatchEdgeFunctionRequest.to_json())

# convert the object into a dict
patch_edge_function_request_dict = patch_edge_function_request_instance.to_dict()
# create an instance of PatchEdgeFunctionRequest from a dict
patch_edge_function_request_from_dict = PatchEdgeFunctionRequest.from_dict(patch_edge_function_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


