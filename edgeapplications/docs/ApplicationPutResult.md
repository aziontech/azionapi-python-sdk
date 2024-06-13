# ApplicationPutResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**ApplicationUpdateResults**](ApplicationUpdateResults.md) |  | 
**schema_version** | **int** |  | 

## Example

```python
from edgeapplications.models.application_put_result import ApplicationPutResult

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationPutResult from a JSON string
application_put_result_instance = ApplicationPutResult.from_json(json)
# print the JSON string representation of the object
print(ApplicationPutResult.to_json())

# convert the object into a dict
application_put_result_dict = application_put_result_instance.to_dict()
# create an instance of ApplicationPutResult from a dict
application_put_result_from_dict = ApplicationPutResult.from_dict(application_put_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


