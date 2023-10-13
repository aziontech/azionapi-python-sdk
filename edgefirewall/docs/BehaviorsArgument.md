# BehaviorsArgument


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**limit_by** | **str** |  | [optional] 
**average_rate_limit** | **int** |  | [optional] 
**maximum_burst_size** | **int** |  | [optional] 
**waf_id** | **int** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from edgefirewall.models.behaviors_argument import BehaviorsArgument

# TODO update the JSON string below
json = "{}"
# create an instance of BehaviorsArgument from a JSON string
behaviors_argument_instance = BehaviorsArgument.from_json(json)
# print the JSON string representation of the object
print BehaviorsArgument.to_json()

# convert the object into a dict
behaviors_argument_dict = behaviors_argument_instance.to_dict()
# create an instance of BehaviorsArgument from a dict
behaviors_argument_form_dict = behaviors_argument.from_dict(behaviors_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


