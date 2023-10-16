# SetRateLimitBehavior


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**argument** | [**SetRateLimitBehaviorArgument**](SetRateLimitBehaviorArgument.md) |  | [optional] 

## Example

```python
from edgefirewall.models.set_rate_limit_behavior import SetRateLimitBehavior

# TODO update the JSON string below
json = "{}"
# create an instance of SetRateLimitBehavior from a JSON string
set_rate_limit_behavior_instance = SetRateLimitBehavior.from_json(json)
# print the JSON string representation of the object
print SetRateLimitBehavior.to_json()

# convert the object into a dict
set_rate_limit_behavior_dict = set_rate_limit_behavior_instance.to_dict()
# create an instance of SetRateLimitBehavior from a dict
set_rate_limit_behavior_form_dict = set_rate_limit_behavior.from_dict(set_rate_limit_behavior_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


