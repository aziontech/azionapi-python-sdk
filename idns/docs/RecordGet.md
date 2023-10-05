# RecordGet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_id** | **int** |  | [optional] 
**entry** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**answers_list** | **List[str]** |  | [optional] 
**policy** | **str** |  | [optional] 
**weight** | **int** |  | [optional] 
**record_type** | **str** |  | [optional] 
**ttl** | **int** |  | [optional] 

## Example

```python
from idns.models.record_get import RecordGet

# TODO update the JSON string below
json = "{}"
# create an instance of RecordGet from a JSON string
record_get_instance = RecordGet.from_json(json)
# print the JSON string representation of the object
print RecordGet.to_json()

# convert the object into a dict
record_get_dict = record_get_instance.to_dict()
# create an instance of RecordGet from a dict
record_get_form_dict = record_get.from_dict(record_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


