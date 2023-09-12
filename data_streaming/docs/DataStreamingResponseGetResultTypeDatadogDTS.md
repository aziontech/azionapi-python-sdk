# DataStreamingResponseGetResultTypeDatadogDTS


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**template_id** | **int** |  | [optional] 
**data_source** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**endpoint** | [**DataStreamingEndpointTypeDatadogDTS**](DataStreamingEndpointTypeDatadogDTS.md) |  | [optional] 
**all_domains** | **bool** |  | [optional] 

## Example

```python
from data_streaming.models.data_streaming_response_get_result_type_datadog_dts import DataStreamingResponseGetResultTypeDatadogDTS

# TODO update the JSON string below
json = "{}"
# create an instance of DataStreamingResponseGetResultTypeDatadogDTS from a JSON string
data_streaming_response_get_result_type_datadog_dts_instance = DataStreamingResponseGetResultTypeDatadogDTS.from_json(json)
# print the JSON string representation of the object
print DataStreamingResponseGetResultTypeDatadogDTS.to_json()

# convert the object into a dict
data_streaming_response_get_result_type_datadog_dts_dict = data_streaming_response_get_result_type_datadog_dts_instance.to_dict()
# create an instance of DataStreamingResponseGetResultTypeDatadogDTS from a dict
data_streaming_response_get_result_type_datadog_dts_form_dict = data_streaming_response_get_result_type_datadog_dts.from_dict(data_streaming_response_get_result_type_datadog_dts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


