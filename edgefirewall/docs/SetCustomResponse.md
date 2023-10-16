# SetCustomResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**argument** | [**SetCustomResponseArgument**](SetCustomResponseArgument.md) |  | [optional] 

## Example

```python
from edgefirewall.models.set_custom_response import SetCustomResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetCustomResponse from a JSON string
set_custom_response_instance = SetCustomResponse.from_json(json)
# print the JSON string representation of the object
print SetCustomResponse.to_json()

# convert the object into a dict
set_custom_response_dict = set_custom_response_instance.to_dict()
# create an instance of SetCustomResponse from a dict
set_custom_response_form_dict = set_custom_response.from_dict(set_custom_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


