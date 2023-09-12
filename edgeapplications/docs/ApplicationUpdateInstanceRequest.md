# ApplicationUpdateInstanceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**edge_function_id** | **int** |  | 
**args** | **object** |  | 

## Example

```python
from edgeapplications.models.application_update_instance_request import ApplicationUpdateInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationUpdateInstanceRequest from a JSON string
application_update_instance_request_instance = ApplicationUpdateInstanceRequest.from_json(json)
# print the JSON string representation of the object
print ApplicationUpdateInstanceRequest.to_json()

# convert the object into a dict
application_update_instance_request_dict = application_update_instance_request_instance.to_dict()
# create an instance of ApplicationUpdateInstanceRequest from a dict
application_update_instance_request_form_dict = application_update_instance_request.from_dict(application_update_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


