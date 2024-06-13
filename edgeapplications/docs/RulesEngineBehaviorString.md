# RulesEngineBehaviorString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**target** | **str** |  | 

## Example

```python
from edgeapplications.models.rules_engine_behavior_string import RulesEngineBehaviorString

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineBehaviorString from a JSON string
rules_engine_behavior_string_instance = RulesEngineBehaviorString.from_json(json)
# print the JSON string representation of the object
print(RulesEngineBehaviorString.to_json())

# convert the object into a dict
rules_engine_behavior_string_dict = rules_engine_behavior_string_instance.to_dict()
# create an instance of RulesEngineBehaviorString from a dict
rules_engine_behavior_string_from_dict = RulesEngineBehaviorString.from_dict(rules_engine_behavior_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


