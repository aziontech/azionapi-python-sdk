# NetworkListUuidResponseEntryString


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_editor** | **str** |  | [optional] 
**last_modified** | **str** |  | [optional] 
**list_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**items_values** | **List[str]** |  | [optional] 

## Example

```python
from networklist.models.network_list_uuid_response_entry_string import NetworkListUuidResponseEntryString

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkListUuidResponseEntryString from a JSON string
network_list_uuid_response_entry_string_instance = NetworkListUuidResponseEntryString.from_json(json)
# print the JSON string representation of the object
print NetworkListUuidResponseEntryString.to_json()

# convert the object into a dict
network_list_uuid_response_entry_string_dict = network_list_uuid_response_entry_string_instance.to_dict()
# create an instance of NetworkListUuidResponseEntryString from a dict
network_list_uuid_response_entry_string_form_dict = network_list_uuid_response_entry_string.from_dict(network_list_uuid_response_entry_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


