# NetworkListResponseEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**last_editor** | **str** |  | [optional] 
**last_modified** | **str** |  | [optional] 
**list_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**items_values** | **List[str]** |  | [optional] 

## Example

```python
from networklist.models.network_list_response_entry import NetworkListResponseEntry

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkListResponseEntry from a JSON string
network_list_response_entry_instance = NetworkListResponseEntry.from_json(json)
# print the JSON string representation of the object
print NetworkListResponseEntry.to_json()

# convert the object into a dict
network_list_response_entry_dict = network_list_response_entry_instance.to_dict()
# create an instance of NetworkListResponseEntry from a dict
network_list_response_entry_form_dict = network_list_response_entry.from_dict(network_list_response_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


