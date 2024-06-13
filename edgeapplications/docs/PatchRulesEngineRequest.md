# PatchRulesEngineRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**criteria** | **List[List[RulesEngineCriteria]]** |  | [optional] 
**behaviors** | [**List[RulesEngineBehaviorEntry]**](RulesEngineBehaviorEntry.md) |  | [optional] 

## Example

```python
from edgeapplications.models.patch_rules_engine_request import PatchRulesEngineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchRulesEngineRequest from a JSON string
patch_rules_engine_request_instance = PatchRulesEngineRequest.from_json(json)
# print the JSON string representation of the object
print(PatchRulesEngineRequest.to_json())

# convert the object into a dict
patch_rules_engine_request_dict = patch_rules_engine_request_instance.to_dict()
# create an instance of PatchRulesEngineRequest from a dict
patch_rules_engine_request_from_dict = PatchRulesEngineRequest.from_dict(patch_rules_engine_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


