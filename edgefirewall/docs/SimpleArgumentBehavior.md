# SimpleArgumentBehavior


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**argument** | [**SimpleArgumentBehaviorArgument**](SimpleArgumentBehaviorArgument.md) |  | [optional] 

## Example

```python
from edgefirewall.models.simple_argument_behavior import SimpleArgumentBehavior

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleArgumentBehavior from a JSON string
simple_argument_behavior_instance = SimpleArgumentBehavior.from_json(json)
# print the JSON string representation of the object
print SimpleArgumentBehavior.to_json()

# convert the object into a dict
simple_argument_behavior_dict = simple_argument_behavior_instance.to_dict()
# create an instance of SimpleArgumentBehavior from a dict
simple_argument_behavior_form_dict = simple_argument_behavior.from_dict(simple_argument_behavior_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


