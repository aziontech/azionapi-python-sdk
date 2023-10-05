# RecordPostOrPut


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**entry** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**answers_list** | **List[str]** |  | [optional] 
**policy** | **str** |  | [optional] 
**weight** | **int** |  | [optional] 
**record_type** | **str** |  | [optional] 
**ttl** | **int** |  | [optional] 

## Example

```python
from idns.models.record_post_or_put import RecordPostOrPut

# TODO update the JSON string below
json = "{}"
# create an instance of RecordPostOrPut from a JSON string
record_post_or_put_instance = RecordPostOrPut.from_json(json)
# print the JSON string representation of the object
print RecordPostOrPut.to_json()

# convert the object into a dict
record_post_or_put_dict = record_post_or_put_instance.to_dict()
# create an instance of RecordPostOrPut from a dict
record_post_or_put_form_dict = record_post_or_put.from_dict(record_post_or_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


