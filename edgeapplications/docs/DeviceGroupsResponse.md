# DeviceGroupsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**total_pages** | **int** |  | 
**schema_version** | **int** |  | 
**links** | [**DeviceGroupsResponseLinks**](DeviceGroupsResponseLinks.md) |  | 
**results** | [**List[DeviceGroupsResultResponse]**](DeviceGroupsResultResponse.md) |  | 

## Example

```python
from edgeapplications.models.device_groups_response import DeviceGroupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceGroupsResponse from a JSON string
device_groups_response_instance = DeviceGroupsResponse.from_json(json)
# print the JSON string representation of the object
print(DeviceGroupsResponse.to_json())

# convert the object into a dict
device_groups_response_dict = device_groups_response_instance.to_dict()
# create an instance of DeviceGroupsResponse from a dict
device_groups_response_from_dict = DeviceGroupsResponse.from_dict(device_groups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


