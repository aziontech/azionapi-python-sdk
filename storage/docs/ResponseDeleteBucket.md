# ResponseDeleteBucket


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**StateEnum**](StateEnum.md) |  | 
**data** | [**ResponseDeleteBucketData**](ResponseDeleteBucketData.md) |  | 

## Example

```python
from storage.models.response_delete_bucket import ResponseDeleteBucket

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseDeleteBucket from a JSON string
response_delete_bucket_instance = ResponseDeleteBucket.from_json(json)
# print the JSON string representation of the object
print ResponseDeleteBucket.to_json()

# convert the object into a dict
response_delete_bucket_dict = response_delete_bucket_instance.to_dict()
# create an instance of ResponseDeleteBucket from a dict
response_delete_bucket_form_dict = response_delete_bucket.from_dict(response_delete_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


