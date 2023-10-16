# SetCustomResponseArgument


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | [**SetCustomResponseArgumentStatusCode**](SetCustomResponseArgumentStatusCode.md) |  | 
**content_type** | **str** |  | 
**content_body** | **str** |  | 

## Example

```python
from edgefirewall.models.set_custom_response_argument import SetCustomResponseArgument

# TODO update the JSON string below
json = "{}"
# create an instance of SetCustomResponseArgument from a JSON string
set_custom_response_argument_instance = SetCustomResponseArgument.from_json(json)
# print the JSON string representation of the object
print SetCustomResponseArgument.to_json()

# convert the object into a dict
set_custom_response_argument_dict = set_custom_response_argument_instance.to_dict()
# create an instance of SetCustomResponseArgument from a dict
set_custom_response_argument_form_dict = set_custom_response_argument.from_dict(set_custom_response_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


