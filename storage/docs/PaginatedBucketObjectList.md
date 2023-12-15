# PaginatedBucketObjectList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[BucketObject]**](BucketObject.md) |  | [optional] 

## Example

```python
from storage.models.paginated_bucket_object_list import PaginatedBucketObjectList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedBucketObjectList from a JSON string
paginated_bucket_object_list_instance = PaginatedBucketObjectList.from_json(json)
# print the JSON string representation of the object
print PaginatedBucketObjectList.to_json()

# convert the object into a dict
paginated_bucket_object_list_dict = paginated_bucket_object_list_instance.to_dict()
# create an instance of PaginatedBucketObjectList from a dict
paginated_bucket_object_list_form_dict = paginated_bucket_object_list.from_dict(paginated_bucket_object_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


