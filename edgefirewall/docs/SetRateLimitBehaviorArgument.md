# SetRateLimitBehaviorArgument


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**limit_by** | **str** |  | [optional] 
**average_rate_limit** | [**SetRateLimitBehaviorArgumentAverageRateLimit**](SetRateLimitBehaviorArgumentAverageRateLimit.md) |  | [optional] 
**maximum_burst_size** | [**SetRateLimitBehaviorArgumentAverageRateLimit**](SetRateLimitBehaviorArgumentAverageRateLimit.md) |  | [optional] 

## Example

```python
from edgefirewall.models.set_rate_limit_behavior_argument import SetRateLimitBehaviorArgument

# TODO update the JSON string below
json = "{}"
# create an instance of SetRateLimitBehaviorArgument from a JSON string
set_rate_limit_behavior_argument_instance = SetRateLimitBehaviorArgument.from_json(json)
# print the JSON string representation of the object
print SetRateLimitBehaviorArgument.to_json()

# convert the object into a dict
set_rate_limit_behavior_argument_dict = set_rate_limit_behavior_argument_instance.to_dict()
# create an instance of SetRateLimitBehaviorArgument from a dict
set_rate_limit_behavior_argument_form_dict = set_rate_limit_behavior_argument.from_dict(set_rate_limit_behavior_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


