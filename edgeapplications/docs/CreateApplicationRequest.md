# CreateApplicationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**application_acceleration** | **bool** |  | [optional] 
**delivery_protocol** | **str** |  | [optional] 
**origin_type** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**minimum_tls_version** | **str** |  | [optional] 
**origin_protocol_policy** | **str** |  | [optional] 
**host_header** | **str** |  | [optional] 
**browser_cache_settings** | **str** |  | [optional] 
**cdn_cache_settings** | **str** |  | [optional] 
**browser_cache_settings_maximum_ttl** | **int** |  | [optional] 
**cdn_cache_settings_maximum_ttl** | **int** |  | [optional] 
**debug_rules** | **bool** |  | [optional] 
**supported_ciphers** | **str** |  | [optional] 
**http_port** | **object** |  | [optional] 
**https_port** | **object** |  | [optional] 
**l2_caching** | **bool** |  | [optional] 
**http3** | **bool** |  | [optional] 
**websocket** | **bool** |  | [optional] 

## Example

```python
from edgeapplications.models.create_application_request import CreateApplicationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApplicationRequest from a JSON string
create_application_request_instance = CreateApplicationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateApplicationRequest.to_json())

# convert the object into a dict
create_application_request_dict = create_application_request_instance.to_dict()
# create an instance of CreateApplicationRequest from a dict
create_application_request_from_dict = CreateApplicationRequest.from_dict(create_application_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


