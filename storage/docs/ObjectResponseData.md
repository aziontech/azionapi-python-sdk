# ObjectResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_key** | **str** |  | 

## Example

```python
from storage.models.object_response_data import ObjectResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectResponseData from a JSON string
object_response_data_instance = ObjectResponseData.from_json(json)
# print the JSON string representation of the object
print(ObjectResponseData.to_json())

# convert the object into a dict
object_response_data_dict = object_response_data_instance.to_dict()
# create an instance of ObjectResponseData from a dict
object_response_data_from_dict = ObjectResponseData.from_dict(object_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


