# PatchDeviceGroupsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 

## Example

```python
from edgeapplications.models.patch_device_groups_request import PatchDeviceGroupsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchDeviceGroupsRequest from a JSON string
patch_device_groups_request_instance = PatchDeviceGroupsRequest.from_json(json)
# print the JSON string representation of the object
print PatchDeviceGroupsRequest.to_json()

# convert the object into a dict
patch_device_groups_request_dict = patch_device_groups_request_instance.to_dict()
# create an instance of PatchDeviceGroupsRequest from a dict
patch_device_groups_request_form_dict = patch_device_groups_request.from_dict(patch_device_groups_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


