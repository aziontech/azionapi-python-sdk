# ApplicationUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**ApplicationUpdateResults**](ApplicationUpdateResults.md) |  | 
**schema_version** | **int** |  | 

## Example

```python
from edgeapplications.models.application_update_response import ApplicationUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationUpdateResponse from a JSON string
application_update_response_instance = ApplicationUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationUpdateResponse.to_json())

# convert the object into a dict
application_update_response_dict = application_update_response_instance.to_dict()
# create an instance of ApplicationUpdateResponse from a dict
application_update_response_from_dict = ApplicationUpdateResponse.from_dict(application_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


