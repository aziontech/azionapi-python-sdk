# SetWAFRuleSetBehaviorArgument


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**waf_id** | **int** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from edgefirewall.models.set_waf_rule_set_behavior_argument import SetWAFRuleSetBehaviorArgument

# TODO update the JSON string below
json = "{}"
# create an instance of SetWAFRuleSetBehaviorArgument from a JSON string
set_waf_rule_set_behavior_argument_instance = SetWAFRuleSetBehaviorArgument.from_json(json)
# print the JSON string representation of the object
print SetWAFRuleSetBehaviorArgument.to_json()

# convert the object into a dict
set_waf_rule_set_behavior_argument_dict = set_waf_rule_set_behavior_argument_instance.to_dict()
# create an instance of SetWAFRuleSetBehaviorArgument from a dict
set_waf_rule_set_behavior_argument_form_dict = set_waf_rule_set_behavior_argument.from_dict(set_waf_rule_set_behavior_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


