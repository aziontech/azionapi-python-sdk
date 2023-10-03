# RuleSetResultResults


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
from edgefirewall.models.rule_set_result_results import RuleSetResultResults

# TODO update the JSON string below
json = "{}"
# create an instance of RuleSetResultResults from a JSON string
rule_set_result_results_instance = RuleSetResultResults.from_json(json)
# print the JSON string representation of the object
print RuleSetResultResults.to_json()

# convert the object into a dict
rule_set_result_results_dict = rule_set_result_results_instance.to_dict()
# create an instance of RuleSetResultResults from a dict
rule_set_result_results_form_dict = rule_set_result_results.from_dict(rule_set_result_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


