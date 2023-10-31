# NetworkListUuidResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**NetworkListUuidResponseEntry**](NetworkListUuidResponseEntry.md) |  | [optional] 
**schema_version** | **int** |  | [optional] 

## Example

```python
from networklist.models.network_list_uuid_response import NetworkListUuidResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkListUuidResponse from a JSON string
network_list_uuid_response_instance = NetworkListUuidResponse.from_json(json)
# print the JSON string representation of the object
print NetworkListUuidResponse.to_json()

# convert the object into a dict
network_list_uuid_response_dict = network_list_uuid_response_instance.to_dict()
# create an instance of NetworkListUuidResponse from a dict
network_list_uuid_response_form_dict = network_list_uuid_response.from_dict(network_list_uuid_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


