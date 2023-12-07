# PatchedBucket


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**edge_access** | [**EdgeAccessEnum**](EdgeAccessEnum.md) |  | [optional] 

## Example

```python
from storage.models.patched_bucket import PatchedBucket

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedBucket from a JSON string
patched_bucket_instance = PatchedBucket.from_json(json)
# print the JSON string representation of the object
print PatchedBucket.to_json()

# convert the object into a dict
patched_bucket_dict = patched_bucket_instance.to_dict()
# create an instance of PatchedBucket from a dict
patched_bucket_form_dict = patched_bucket.from_dict(patched_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


