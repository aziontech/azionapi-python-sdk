# ApplicationUpdateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**delivery_protocol** | **str** |  | [optional] 
**http_port** | **object** |  | [optional] 
**https_port** | **object** |  | [optional] 
**minimum_tls_version** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**debug_rules** | **bool** |  | [optional] 
**application_acceleration** | **bool** |  | [optional] 
**device_detection** | **bool** |  | [optional] 
**edge_firewall** | **bool** |  | [optional] 
**edge_functions** | **bool** |  | [optional] 
**image_optimization** | **bool** |  | [optional] 
**l2_caching** | **bool** |  | [optional] 
**load_balancer** | **bool** |  | [optional] 
**raw_logs** | **bool** |  | [optional] 
**web_application_firewall** | **bool** |  | [optional] 
**websocket** | **bool** |  | [optional] 

## Example

```python
from edgeapplications.models.application_update_request import ApplicationUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationUpdateRequest from a JSON string
application_update_request_instance = ApplicationUpdateRequest.from_json(json)
# print the JSON string representation of the object
print ApplicationUpdateRequest.to_json()

# convert the object into a dict
application_update_request_dict = application_update_request_instance.to_dict()
# create an instance of ApplicationUpdateRequest from a dict
application_update_request_form_dict = application_update_request.from_dict(application_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


