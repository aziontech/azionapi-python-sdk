# ListNetworkListsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**schema_version** | **int** |  | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 
**results** | [**List[NetworkLists]**](NetworkLists.md) |  | [optional] 

## Example

```python
from networklist.models.list_network_lists_response import ListNetworkListsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListNetworkListsResponse from a JSON string
list_network_lists_response_instance = ListNetworkListsResponse.from_json(json)
# print the JSON string representation of the object
print ListNetworkListsResponse.to_json()

# convert the object into a dict
list_network_lists_response_dict = list_network_lists_response_instance.to_dict()
# create an instance of ListNetworkListsResponse from a dict
list_network_lists_response_form_dict = list_network_lists_response.from_dict(list_network_lists_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


