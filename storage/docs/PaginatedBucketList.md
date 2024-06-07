# PaginatedBucketList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Bucket]**](Bucket.md) |  | [optional] 

## Example

```python
from storage.models.paginated_bucket_list import PaginatedBucketList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedBucketList from a JSON string
paginated_bucket_list_instance = PaginatedBucketList.from_json(json)
# print the JSON string representation of the object
print(PaginatedBucketList.to_json())

# convert the object into a dict
paginated_bucket_list_dict = paginated_bucket_list_instance.to_dict()
# create an instance of PaginatedBucketList from a dict
paginated_bucket_list_from_dict = PaginatedBucketList.from_dict(paginated_bucket_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


