# DeviceGroupsResponseLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous** | **str** |  | [optional] 
**next** | **str** |  | [optional] 

## Example

```python
from edgeapplications.models.device_groups_response_links import DeviceGroupsResponseLinks

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceGroupsResponseLinks from a JSON string
device_groups_response_links_instance = DeviceGroupsResponseLinks.from_json(json)
# print the JSON string representation of the object
print(DeviceGroupsResponseLinks.to_json())

# convert the object into a dict
device_groups_response_links_dict = device_groups_response_links_instance.to_dict()
# create an instance of DeviceGroupsResponseLinks from a dict
device_groups_response_links_from_dict = DeviceGroupsResponseLinks.from_dict(device_groups_response_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


