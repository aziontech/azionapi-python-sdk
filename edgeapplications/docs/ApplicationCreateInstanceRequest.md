# ApplicationCreateInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**edge_function_id** | **int** |  | 
**args** | [**ApplicationCreateInstanceRequestArgs**](ApplicationCreateInstanceRequestArgs.md) |  | 

## Example

```python
from edgeapplications.models.application_create_instance_request import ApplicationCreateInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCreateInstanceRequest from a JSON string
application_create_instance_request_instance = ApplicationCreateInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationCreateInstanceRequest.to_json())

# convert the object into a dict
application_create_instance_request_dict = application_create_instance_request_instance.to_dict()
# create an instance of ApplicationCreateInstanceRequest from a dict
application_create_instance_request_from_dict = ApplicationCreateInstanceRequest.from_dict(application_create_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


