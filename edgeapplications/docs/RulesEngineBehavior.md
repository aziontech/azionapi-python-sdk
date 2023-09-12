# RulesEngineBehavior


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**target** | [**RulesEngineBehaviorTarget**](RulesEngineBehaviorTarget.md) |  | [optional] 

## Example

```python
from edgeapplications.models.rules_engine_behavior import RulesEngineBehavior

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineBehavior from a JSON string
rules_engine_behavior_instance = RulesEngineBehavior.from_json(json)
# print the JSON string representation of the object
print RulesEngineBehavior.to_json()

# convert the object into a dict
rules_engine_behavior_dict = rules_engine_behavior_instance.to_dict()
# create an instance of RulesEngineBehavior from a dict
rules_engine_behavior_form_dict = rules_engine_behavior.from_dict(rules_engine_behavior_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


