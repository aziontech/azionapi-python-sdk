# BucketCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**edge_access** | [**EdgeAccessEnum**](EdgeAccessEnum.md) |  | 

## Example

```python
from storage.models.bucket_create import BucketCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BucketCreate from a JSON string
bucket_create_instance = BucketCreate.from_json(json)
# print the JSON string representation of the object
print(BucketCreate.to_json())

# convert the object into a dict
bucket_create_dict = bucket_create_instance.to_dict()
# create an instance of BucketCreate from a dict
bucket_create_form_dict = bucket_create.from_dict(bucket_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


