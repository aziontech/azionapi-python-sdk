# UpdateDeviceGroupsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 

## Example

```python
from edgeapplications.models.update_device_groups_request import UpdateDeviceGroupsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDeviceGroupsRequest from a JSON string
update_device_groups_request_instance = UpdateDeviceGroupsRequest.from_json(json)
# print the JSON string representation of the object
print UpdateDeviceGroupsRequest.to_json()

# convert the object into a dict
update_device_groups_request_dict = update_device_groups_request_instance.to_dict()
# create an instance of UpdateDeviceGroupsRequest from a dict
update_device_groups_request_form_dict = update_device_groups_request.from_dict(update_device_groups_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


