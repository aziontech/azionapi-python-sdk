# BucketUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edge_access** | [**EdgeAccessEnum**](EdgeAccessEnum.md) |  | 

## Example

```python
from storage.models.bucket_update import BucketUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of BucketUpdate from a JSON string
bucket_update_instance = BucketUpdate.from_json(json)
# print the JSON string representation of the object
print(BucketUpdate.to_json())

# convert the object into a dict
bucket_update_dict = bucket_update_instance.to_dict()
# create an instance of BucketUpdate from a dict
bucket_update_form_dict = bucket_update.from_dict(bucket_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


