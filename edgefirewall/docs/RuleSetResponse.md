# RuleSetResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**behaviors** | [**List[Behaviors]**](Behaviors.md) |  | [optional] 
**criteria** | **List[List[SSLVerificationStatusCriteria]]** |  | [optional] 
**last_modified** | **datetime** |  | [optional] 
**last_editor** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**order** | **int** |  | [optional] 

## Example

```python
from edgefirewall.models.rule_set_response import RuleSetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RuleSetResponse from a JSON string
rule_set_response_instance = RuleSetResponse.from_json(json)
# print the JSON string representation of the object
print RuleSetResponse.to_json()

# convert the object into a dict
rule_set_response_dict = rule_set_response_instance.to_dict()
# create an instance of RuleSetResponse from a dict
rule_set_response_form_dict = rule_set_response.from_dict(rule_set_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


