# DeviceGroupsIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**DeviceGroupsResultResponse**](DeviceGroupsResultResponse.md) |  | 
**schema_version** | **int** |  | 

## Example

```python
from edgeapplications.models.device_groups_id_response import DeviceGroupsIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceGroupsIdResponse from a JSON string
device_groups_id_response_instance = DeviceGroupsIdResponse.from_json(json)
# print the JSON string representation of the object
print(DeviceGroupsIdResponse.to_json())

# convert the object into a dict
device_groups_id_response_dict = device_groups_id_response_instance.to_dict()
# create an instance of DeviceGroupsIdResponse from a dict
device_groups_id_response_from_dict = DeviceGroupsIdResponse.from_dict(device_groups_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


