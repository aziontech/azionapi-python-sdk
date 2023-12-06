# NetworkListsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**NetworkListResponseEntry**](NetworkListResponseEntry.md) |  | [optional] 
**schema_version** | **int** |  | [optional] 

## Example

```python
from networklist.models.network_lists_response import NetworkListsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkListsResponse from a JSON string
network_lists_response_instance = NetworkListsResponse.from_json(json)
# print the JSON string representation of the object
print NetworkListsResponse.to_json()

# convert the object into a dict
network_lists_response_dict = network_lists_response_instance.to_dict()
# create an instance of NetworkListsResponse from a dict
network_lists_response_form_dict = network_lists_response.from_dict(network_lists_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


