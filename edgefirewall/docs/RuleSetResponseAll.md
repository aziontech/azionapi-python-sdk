# RuleSetResponseAll


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**schema_version** | **int** |  | [optional] [default to 3]
**links** | [**Links**](Links.md) |  | [optional] 
**results** | [**List[RuleSetResultAll]**](RuleSetResultAll.md) |  | [optional] 

## Example

```python
from edgefirewall.models.rule_set_response_all import RuleSetResponseAll

# TODO update the JSON string below
json = "{}"
# create an instance of RuleSetResponseAll from a JSON string
rule_set_response_all_instance = RuleSetResponseAll.from_json(json)
# print the JSON string representation of the object
print RuleSetResponseAll.to_json()

# convert the object into a dict
rule_set_response_all_dict = rule_set_response_all_instance.to_dict()
# create an instance of RuleSetResponseAll from a dict
rule_set_response_all_form_dict = rule_set_response_all.from_dict(rule_set_response_all_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


