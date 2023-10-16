# SetWAFRuleSetAndWafModeBehavior


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**argument** | [**SetWAFRuleSetAndWafModeBehaviorArgument**](SetWAFRuleSetAndWafModeBehaviorArgument.md) |  | [optional] 

## Example

```python
from edgefirewall.models.set_waf_rule_set_and_waf_mode_behavior import SetWAFRuleSetAndWafModeBehavior

# TODO update the JSON string below
json = "{}"
# create an instance of SetWAFRuleSetAndWafModeBehavior from a JSON string
set_waf_rule_set_and_waf_mode_behavior_instance = SetWAFRuleSetAndWafModeBehavior.from_json(json)
# print the JSON string representation of the object
print SetWAFRuleSetAndWafModeBehavior.to_json()

# convert the object into a dict
set_waf_rule_set_and_waf_mode_behavior_dict = set_waf_rule_set_and_waf_mode_behavior_instance.to_dict()
# create an instance of SetWAFRuleSetAndWafModeBehavior from a dict
set_waf_rule_set_and_waf_mode_behavior_form_dict = set_waf_rule_set_and_waf_mode_behavior.from_dict(set_waf_rule_set_and_waf_mode_behavior_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


