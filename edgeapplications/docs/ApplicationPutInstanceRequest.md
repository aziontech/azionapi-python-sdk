# ApplicationPutInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**edge_function_id** | **int** |  | 
**args** | [**ApplicationCreateInstanceRequestArgs**](ApplicationCreateInstanceRequestArgs.md) |  | 

## Example

```python
from edgeapplications.models.application_put_instance_request import ApplicationPutInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationPutInstanceRequest from a JSON string
application_put_instance_request_instance = ApplicationPutInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationPutInstanceRequest.to_json())

# convert the object into a dict
application_put_instance_request_dict = application_put_instance_request_instance.to_dict()
# create an instance of ApplicationPutInstanceRequest from a dict
application_put_instance_request_from_dict = ApplicationPutInstanceRequest.from_dict(application_put_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


