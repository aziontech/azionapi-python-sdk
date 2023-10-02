# CreateRuleSetRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**behaviors** | [**List[Behaviors]**](Behaviors.md) |  | [optional] 
**criteria** | **List[List[SSLVerificationStatusCriteria]]** |  | [optional] 

## Example

```python
from edgefirewall.models.create_rule_set_request import CreateRuleSetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRuleSetRequest from a JSON string
create_rule_set_request_instance = CreateRuleSetRequest.from_json(json)
# print the JSON string representation of the object
print CreateRuleSetRequest.to_json()

# convert the object into a dict
create_rule_set_request_dict = create_rule_set_request_instance.to_dict()
# create an instance of CreateRuleSetRequest from a dict
create_rule_set_request_form_dict = create_rule_set_request.from_dict(create_rule_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


