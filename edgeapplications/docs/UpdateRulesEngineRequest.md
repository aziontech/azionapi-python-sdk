# UpdateRulesEngineRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**criteria** | **List[List[RulesEngineCriteria]]** |  | 
**behaviors** | [**List[RulesEngineBehaviorEntry]**](RulesEngineBehaviorEntry.md) |  | 

## Example

```python
from edgeapplications.models.update_rules_engine_request import UpdateRulesEngineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRulesEngineRequest from a JSON string
update_rules_engine_request_instance = UpdateRulesEngineRequest.from_json(json)
# print the JSON string representation of the object
print UpdateRulesEngineRequest.to_json()

# convert the object into a dict
update_rules_engine_request_dict = update_rules_engine_request_instance.to_dict()
# create an instance of UpdateRulesEngineRequest from a dict
update_rules_engine_request_form_dict = update_rules_engine_request.from_dict(update_rules_engine_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


