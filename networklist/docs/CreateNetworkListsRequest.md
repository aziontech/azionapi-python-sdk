# CreateNetworkListsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**items_values** | **List[str]** |  | [optional] 
**list_type** | **str** |  | [optional] 

## Example

```python
from networklist.models.create_network_lists_request import CreateNetworkListsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNetworkListsRequest from a JSON string
create_network_lists_request_instance = CreateNetworkListsRequest.from_json(json)
# print the JSON string representation of the object
print CreateNetworkListsRequest.to_json()

# convert the object into a dict
create_network_lists_request_dict = create_network_lists_request_instance.to_dict()
# create an instance of CreateNetworkListsRequest from a dict
create_network_lists_request_form_dict = create_network_lists_request.from_dict(create_network_lists_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


