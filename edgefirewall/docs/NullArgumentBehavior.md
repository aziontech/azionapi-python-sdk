# NullArgumentBehavior


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**argument** | **int** |  | [optional] 

## Example

```python
from edgefirewall.models.null_argument_behavior import NullArgumentBehavior

# TODO update the JSON string below
json = "{}"
# create an instance of NullArgumentBehavior from a JSON string
null_argument_behavior_instance = NullArgumentBehavior.from_json(json)
# print the JSON string representation of the object
print NullArgumentBehavior.to_json()

# convert the object into a dict
null_argument_behavior_dict = null_argument_behavior_instance.to_dict()
# create an instance of NullArgumentBehavior from a dict
null_argument_behavior_form_dict = null_argument_behavior.from_dict(null_argument_behavior_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


