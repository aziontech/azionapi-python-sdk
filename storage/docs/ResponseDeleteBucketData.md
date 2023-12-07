# ResponseDeleteBucketData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [readonly] 
**edge_access** | [**EdgeAccessEnum**](EdgeAccessEnum.md) |  | 

## Example

```python
from storage.models.response_delete_bucket_data import ResponseDeleteBucketData

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseDeleteBucketData from a JSON string
response_delete_bucket_data_instance = ResponseDeleteBucketData.from_json(json)
# print the JSON string representation of the object
print ResponseDeleteBucketData.to_json()

# convert the object into a dict
response_delete_bucket_data_dict = response_delete_bucket_data_instance.to_dict()
# create an instance of ResponseDeleteBucketData from a dict
response_delete_bucket_data_form_dict = response_delete_bucket_data.from_dict(response_delete_bucket_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


