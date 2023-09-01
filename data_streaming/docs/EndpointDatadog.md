# EndpointDatadog


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**api_key** | **object** |  | [optional] 

## Example

```python
from data_streaming.models.endpoint_datadog import EndpointDatadog

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointDatadog from a JSON string
endpoint_datadog_instance = EndpointDatadog.from_json(json)
# print the JSON string representation of the object
print EndpointDatadog.to_json()

# convert the object into a dict
endpoint_datadog_dict = endpoint_datadog_instance.to_dict()
# create an instance of EndpointDatadog from a dict
endpoint_datadog_form_dict = endpoint_datadog.from_dict(endpoint_datadog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


