# BucketObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [readonly] 
**last_modified** | **datetime** |  | [readonly] 
**size** | **int** |  | [readonly] 
**etag** | **str** |  | [readonly] 

## Example

```python
from storage.models.bucket_object import BucketObject

# TODO update the JSON string below
json = "{}"
# create an instance of BucketObject from a JSON string
bucket_object_instance = BucketObject.from_json(json)
# print the JSON string representation of the object
print BucketObject.to_json()

# convert the object into a dict
bucket_object_dict = bucket_object_instance.to_dict()
# create an instance of BucketObject from a dict
bucket_object_form_dict = bucket_object.from_dict(bucket_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


