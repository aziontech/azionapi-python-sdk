# RulesEngineBehaviorEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**target** | [**RulesEngineBehaviorObjectTarget**](RulesEngineBehaviorObjectTarget.md) |  | 

## Example

```python
from edgeapplications.models.rules_engine_behavior_entry import RulesEngineBehaviorEntry

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineBehaviorEntry from a JSON string
rules_engine_behavior_entry_instance = RulesEngineBehaviorEntry.from_json(json)
# print the JSON string representation of the object
print(RulesEngineBehaviorEntry.to_json())

# convert the object into a dict
rules_engine_behavior_entry_dict = rules_engine_behavior_entry_instance.to_dict()
# create an instance of RulesEngineBehaviorEntry from a dict
rules_engine_behavior_entry_from_dict = RulesEngineBehaviorEntry.from_dict(rules_engine_behavior_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


