# CreateDeviceGroupsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**user_agent** | **str** |  | 
**addresses** | **str** |  | 

## Example

```python
from edgeapplications.models.create_device_groups_request import CreateDeviceGroupsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDeviceGroupsRequest from a JSON string
create_device_groups_request_instance = CreateDeviceGroupsRequest.from_json(json)
# print the JSON string representation of the object
print CreateDeviceGroupsRequest.to_json()

# convert the object into a dict
create_device_groups_request_dict = create_device_groups_request_instance.to_dict()
# create an instance of CreateDeviceGroupsRequest from a dict
create_device_groups_request_form_dict = create_device_groups_request.from_dict(create_device_groups_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


