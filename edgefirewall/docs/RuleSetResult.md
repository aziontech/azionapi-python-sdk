# RuleSetResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**RuleSetResultResults**](RuleSetResultResults.md) |  | [optional] 
**schema_version** | **int** |  | [optional] 

## Example

```python
from edgefirewall.models.rule_set_result import RuleSetResult

# TODO update the JSON string below
json = "{}"
# create an instance of RuleSetResult from a JSON string
rule_set_result_instance = RuleSetResult.from_json(json)
# print the JSON string representation of the object
print RuleSetResult.to_json()

# convert the object into a dict
rule_set_result_dict = rule_set_result_instance.to_dict()
# create an instance of RuleSetResult from a dict
rule_set_result_form_dict = rule_set_result.from_dict(rule_set_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


