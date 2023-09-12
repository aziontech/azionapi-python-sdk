# DeviceGroupsResultResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**user_agent** | **str** |  | 

## Example

```python
from edgeapplications.models.device_groups_result_response import DeviceGroupsResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceGroupsResultResponse from a JSON string
device_groups_result_response_instance = DeviceGroupsResultResponse.from_json(json)
# print the JSON string representation of the object
print DeviceGroupsResultResponse.to_json()

# convert the object into a dict
device_groups_result_response_dict = device_groups_result_response_instance.to_dict()
# create an instance of DeviceGroupsResultResponse from a dict
device_groups_result_response_form_dict = device_groups_result_response.from_dict(device_groups_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


