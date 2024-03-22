# ResponseBucket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**StateEnum**](StateEnum.md) |  | 
**data** | [**Bucket**](Bucket.md) |  | 

## Example

```python
from storage.models.response_bucket import ResponseBucket

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseBucket from a JSON string
response_bucket_instance = ResponseBucket.from_json(json)
# print the JSON string representation of the object
print(ResponseBucket.to_json())

# convert the object into a dict
response_bucket_dict = response_bucket_instance.to_dict()
# create an instance of ResponseBucket from a dict
response_bucket_form_dict = response_bucket.from_dict(response_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


