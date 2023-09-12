# DataStreamingResponseGetResultTypeStandard


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**template_id** | **int** |  | [optional] 
**data_source** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**endpoint** | [**DataStreamingEndpointTypeStandard**](DataStreamingEndpointTypeStandard.md) |  | [optional] 
**all_domains** | **bool** |  | [optional] 

## Example

```python
from data_streaming.models.data_streaming_response_get_result_type_standard import DataStreamingResponseGetResultTypeStandard

# TODO update the JSON string below
json = "{}"
# create an instance of DataStreamingResponseGetResultTypeStandard from a JSON string
data_streaming_response_get_result_type_standard_instance = DataStreamingResponseGetResultTypeStandard.from_json(json)
# print the JSON string representation of the object
print DataStreamingResponseGetResultTypeStandard.to_json()

# convert the object into a dict
data_streaming_response_get_result_type_standard_dict = data_streaming_response_get_result_type_standard_instance.to_dict()
# create an instance of DataStreamingResponseGetResultTypeStandard from a dict
data_streaming_response_get_result_type_standard_form_dict = data_streaming_response_get_result_type_standard.from_dict(data_streaming_response_get_result_type_standard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


