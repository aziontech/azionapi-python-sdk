# RulesEngineBehaviorObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**target** | [**RulesEngineBehaviorObjectTarget**](RulesEngineBehaviorObjectTarget.md) |  | 

## Example

```python
from edgeapplications.models.rules_engine_behavior_object import RulesEngineBehaviorObject

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineBehaviorObject from a JSON string
rules_engine_behavior_object_instance = RulesEngineBehaviorObject.from_json(json)
# print the JSON string representation of the object
print RulesEngineBehaviorObject.to_json()

# convert the object into a dict
rules_engine_behavior_object_dict = rules_engine_behavior_object_instance.to_dict()
# create an instance of RulesEngineBehaviorObject from a dict
rules_engine_behavior_object_form_dict = rules_engine_behavior_object.from_dict(rules_engine_behavior_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


