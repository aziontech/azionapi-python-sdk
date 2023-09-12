# DataStreamingEndpointTypeStandard


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**log_line_separator** | **str** |  | [optional] 
**payload_format** | **str** |  | [optional] 
**max_size** | **int** |  | [optional] 
**headers** | [**DataStreamingEndpointTypeStandardHeadersExample**](DataStreamingEndpointTypeStandardHeadersExample.md) |  | [optional] 

## Example

```python
from data_streaming.models.data_streaming_endpoint_type_standard import DataStreamingEndpointTypeStandard

# TODO update the JSON string below
json = "{}"
# create an instance of DataStreamingEndpointTypeStandard from a JSON string
data_streaming_endpoint_type_standard_instance = DataStreamingEndpointTypeStandard.from_json(json)
# print the JSON string representation of the object
print DataStreamingEndpointTypeStandard.to_json()

# convert the object into a dict
data_streaming_endpoint_type_standard_dict = data_streaming_endpoint_type_standard_instance.to_dict()
# create an instance of DataStreamingEndpointTypeStandard from a dict
data_streaming_endpoint_type_standard_form_dict = data_streaming_endpoint_type_standard.from_dict(data_streaming_endpoint_type_standard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


