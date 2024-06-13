# RulesEngineResultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**phase** | **str** |  | 
**behaviors** | [**List[RulesEngineBehaviorEntry]**](RulesEngineBehaviorEntry.md) |  | [optional] 
**criteria** | **List[List[RulesEngineCriteria]]** |  | 
**is_active** | **bool** |  | 
**order** | **int** |  | 

## Example

```python
from edgeapplications.models.rules_engine_result_response import RulesEngineResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineResultResponse from a JSON string
rules_engine_result_response_instance = RulesEngineResultResponse.from_json(json)
# print the JSON string representation of the object
print(RulesEngineResultResponse.to_json())

# convert the object into a dict
rules_engine_result_response_dict = rules_engine_result_response_instance.to_dict()
# create an instance of RulesEngineResultResponse from a dict
rules_engine_result_response_from_dict = RulesEngineResultResponse.from_dict(rules_engine_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


