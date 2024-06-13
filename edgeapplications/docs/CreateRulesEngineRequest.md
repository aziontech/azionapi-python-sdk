# CreateRulesEngineRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**order** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**criteria** | **List[List[RulesEngineCriteria]]** |  | 
**behaviors** | [**List[RulesEngineBehaviorEntry]**](RulesEngineBehaviorEntry.md) |  | 

## Example

```python
from edgeapplications.models.create_rules_engine_request import CreateRulesEngineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRulesEngineRequest from a JSON string
create_rules_engine_request_instance = CreateRulesEngineRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRulesEngineRequest.to_json())

# convert the object into a dict
create_rules_engine_request_dict = create_rules_engine_request_instance.to_dict()
# create an instance of CreateRulesEngineRequest from a dict
create_rules_engine_request_from_dict = CreateRulesEngineRequest.from_dict(create_rules_engine_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


