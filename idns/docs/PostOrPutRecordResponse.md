# PostOrPutRecordResponse

Object returned by create or update zone record

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **int** | The schema version | [optional] 
**results** | [**RecordPostOrPut**](RecordPostOrPut.md) |  | [optional] 

## Example

```python
from idns.models.post_or_put_record_response import PostOrPutRecordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostOrPutRecordResponse from a JSON string
post_or_put_record_response_instance = PostOrPutRecordResponse.from_json(json)
# print the JSON string representation of the object
print PostOrPutRecordResponse.to_json()

# convert the object into a dict
post_or_put_record_response_dict = post_or_put_record_response_instance.to_dict()
# create an instance of PostOrPutRecordResponse from a dict
post_or_put_record_response_form_dict = post_or_put_record_response.from_dict(post_or_put_record_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


