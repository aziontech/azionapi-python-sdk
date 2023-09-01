# EndpointAzureMonitor


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_type** | **str** |  | [optional] 
**log_type** | **str** |  | [optional] 
**shared_key** | **str** |  | [optional] 
**time_generated_field** | **str** |  | [optional] 
**workspace_id** | **str** |  | [optional] 

## Example

```python
from data_streaming.models.endpoint_azure_monitor import EndpointAzureMonitor

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAzureMonitor from a JSON string
endpoint_azure_monitor_instance = EndpointAzureMonitor.from_json(json)
# print the JSON string representation of the object
print EndpointAzureMonitor.to_json()

# convert the object into a dict
endpoint_azure_monitor_dict = endpoint_azure_monitor_instance.to_dict()
# create an instance of EndpointAzureMonitor from a dict
endpoint_azure_monitor_form_dict = endpoint_azure_monitor.from_dict(endpoint_azure_monitor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


