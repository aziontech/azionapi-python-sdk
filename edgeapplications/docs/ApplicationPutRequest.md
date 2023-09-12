# ApplicationPutRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**delivery_protocol** | **str** |  | [optional] 
**http_port** | **object** |  | [optional] 
**https_port** | **object** |  | [optional] 
**minimum_tls_version** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**application_acceleration** | **bool** |  | [optional] 
**caching** | **bool** |  | [optional] 
**device_detection** | **bool** |  | [optional] 
**edge_firewall** | **bool** |  | [optional] 
**edge_functions** | **bool** |  | [optional] 
**image_optimization** | **bool** |  | [optional] 
**l2_caching** | **bool** |  | [optional] 
**load_balancer** | **bool** |  | [optional] 
**raw_logs** | **bool** |  | [optional] 
**web_application_firewall** | **bool** |  | [optional] 
**debug_rules** | **bool** |  | [optional] 
**http3** | **bool** |  | [optional] 
**websocket** | **bool** |  | [optional] 
**supported_ciphers** | **str** |  | [optional] 

## Example

```python
from edgeapplications.models.application_put_request import ApplicationPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationPutRequest from a JSON string
application_put_request_instance = ApplicationPutRequest.from_json(json)
# print the JSON string representation of the object
print ApplicationPutRequest.to_json()

# convert the object into a dict
application_put_request_dict = application_put_request_instance.to_dict()
# create an instance of ApplicationPutRequest from a dict
application_put_request_form_dict = application_put_request.from_dict(application_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


