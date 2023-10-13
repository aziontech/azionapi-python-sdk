# Behaviors


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**argument** | [**BehaviorsArgument**](BehaviorsArgument.md) |  | [optional] 

## Example

```python
from edgefirewall.models.behaviors import Behaviors

# TODO update the JSON string below
json = "{}"
# create an instance of Behaviors from a JSON string
behaviors_instance = Behaviors.from_json(json)
# print the JSON string representation of the object
print Behaviors.to_json()

# convert the object into a dict
behaviors_dict = behaviors_instance.to_dict()
# create an instance of Behaviors from a dict
behaviors_form_dict = behaviors.from_dict(behaviors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


