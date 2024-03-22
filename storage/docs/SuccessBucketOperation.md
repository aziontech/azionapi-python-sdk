# SuccessBucketOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**StateEnum**](StateEnum.md) |  | 
**data** | [**Bucket**](Bucket.md) |  | 

## Example

```python
from storage.models.success_bucket_operation import SuccessBucketOperation

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessBucketOperation from a JSON string
success_bucket_operation_instance = SuccessBucketOperation.from_json(json)
# print the JSON string representation of the object
print(SuccessBucketOperation.to_json())

# convert the object into a dict
success_bucket_operation_dict = success_bucket_operation_instance.to_dict()
# create an instance of SuccessBucketOperation from a dict
success_bucket_operation_form_dict = success_bucket_operation.from_dict(success_bucket_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


