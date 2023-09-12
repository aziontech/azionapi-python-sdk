# RulesEngineBehaviorTarget


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**captured_array** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**regex** | **str** |  | [optional] 

## Example

```python
from edgeapplications.models.rules_engine_behavior_target import RulesEngineBehaviorTarget

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineBehaviorTarget from a JSON string
rules_engine_behavior_target_instance = RulesEngineBehaviorTarget.from_json(json)
# print the JSON string representation of the object
print RulesEngineBehaviorTarget.to_json()

# convert the object into a dict
rules_engine_behavior_target_dict = rules_engine_behavior_target_instance.to_dict()
# create an instance of RulesEngineBehaviorTarget from a dict
rules_engine_behavior_target_form_dict = rules_engine_behavior_target.from_dict(rules_engine_behavior_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


