# NetworkLists


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**last_editor** | **str** |  | [optional] 
**last_modified** | **str** |  | [optional] 
**list_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**country_list** | **List[str]** |  | [optional] 
**ip_list** | **List[str]** |  | [optional] 

## Example

```python
from networklist.models.network_lists import NetworkLists

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkLists from a JSON string
network_lists_instance = NetworkLists.from_json(json)
# print the JSON string representation of the object
print NetworkLists.to_json()

# convert the object into a dict
network_lists_dict = network_lists_instance.to_dict()
# create an instance of NetworkLists from a dict
network_lists_form_dict = network_lists.from_dict(network_lists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


