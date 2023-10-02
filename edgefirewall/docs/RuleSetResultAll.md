# RuleSetResultAll


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**last_editor** | **str** |  | [optional] 
**last_modified** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**behaviors** | [**List[Behaviors]**](Behaviors.md) |  | [optional] 
**criteria** | **List[List[SSLVerificationStatusCriteria]]** |  | [optional] 
**order** | **int** |  | [optional] 

## Example

```python
from edgefirewall.models.rule_set_result_all import RuleSetResultAll

# TODO update the JSON string below
json = "{}"
# create an instance of RuleSetResultAll from a JSON string
rule_set_result_all_instance = RuleSetResultAll.from_json(json)
# print the JSON string representation of the object
print RuleSetResultAll.to_json()

# convert the object into a dict
rule_set_result_all_dict = rule_set_result_all_instance.to_dict()
# create an instance of RuleSetResultAll from a dict
rule_set_result_all_form_dict = rule_set_result_all.from_dict(rule_set_result_all_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


