# SetWAFRuleSetDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**waf_id** | **int** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from edgefirewall.models.set_waf_rule_set_details import SetWAFRuleSetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SetWAFRuleSetDetails from a JSON string
set_waf_rule_set_details_instance = SetWAFRuleSetDetails.from_json(json)
# print the JSON string representation of the object
print SetWAFRuleSetDetails.to_json()

# convert the object into a dict
set_waf_rule_set_details_dict = set_waf_rule_set_details_instance.to_dict()
# create an instance of SetWAFRuleSetDetails from a dict
set_waf_rule_set_details_form_dict = set_waf_rule_set_details.from_dict(set_waf_rule_set_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


