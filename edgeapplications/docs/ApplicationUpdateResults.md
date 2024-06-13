# ApplicationUpdateResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**delivery_protocol** | **str** |  | 
**http_port** | **object** |  | 
**https_port** | **object** |  | 
**minimum_tls_version** | **str** |  | 
**active** | **bool** |  | 
**debug_rules** | **bool** |  | 
**http3** | **bool** |  | 
**supported_ciphers** | **str** |  | 
**application_acceleration** | **bool** |  | 
**caching** | **bool** |  | 
**device_detection** | **bool** |  | 
**edge_firewall** | **bool** |  | 
**edge_functions** | **bool** |  | 
**image_optimization** | **bool** |  | 
**l2_caching** | **bool** |  | 
**load_balancer** | **bool** |  | 
**raw_logs** | **bool** |  | 
**web_application_firewall** | **bool** |  | 

## Example

```python
from edgeapplications.models.application_update_results import ApplicationUpdateResults

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationUpdateResults from a JSON string
application_update_results_instance = ApplicationUpdateResults.from_json(json)
# print the JSON string representation of the object
print(ApplicationUpdateResults.to_json())

# convert the object into a dict
application_update_results_dict = application_update_results_instance.to_dict()
# create an instance of ApplicationUpdateResults from a dict
application_update_results_from_dict = ApplicationUpdateResults.from_dict(application_update_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


