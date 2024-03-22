# SuccessObjectOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**StateEnum**](StateEnum.md) |  | 
**data** | [**ObjectResponseData**](ObjectResponseData.md) |  | 

## Example

```python
from storage.models.success_object_operation import SuccessObjectOperation

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessObjectOperation from a JSON string
success_object_operation_instance = SuccessObjectOperation.from_json(json)
# print the JSON string representation of the object
print(SuccessObjectOperation.to_json())

# convert the object into a dict
success_object_operation_dict = success_object_operation_instance.to_dict()
# create an instance of SuccessObjectOperation from a dict
success_object_operation_form_dict = success_object_operation.from_dict(success_object_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


