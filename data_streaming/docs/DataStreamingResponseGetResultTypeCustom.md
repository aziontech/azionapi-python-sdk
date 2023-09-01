# DataStreamingResponseGetResultTypeCustom


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**data_source** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**endpoint** | [**DataStreamingEndpointTypeKafka**](DataStreamingEndpointTypeKafka.md) |  | [optional] 
**all_domains** | **bool** |  | [optional] 
**template_model** | **str** |  | [optional] 

## Example

```python
from data_streaming.models.data_streaming_response_get_result_type_custom import DataStreamingResponseGetResultTypeCustom

# TODO update the JSON string below
json = "{}"
# create an instance of DataStreamingResponseGetResultTypeCustom from a JSON string
data_streaming_response_get_result_type_custom_instance = DataStreamingResponseGetResultTypeCustom.from_json(json)
# print the JSON string representation of the object
print DataStreamingResponseGetResultTypeCustom.to_json()

# convert the object into a dict
data_streaming_response_get_result_type_custom_dict = data_streaming_response_get_result_type_custom_instance.to_dict()
# create an instance of DataStreamingResponseGetResultTypeCustom from a dict
data_streaming_response_get_result_type_custom_form_dict = data_streaming_response_get_result_type_custom.from_dict(data_streaming_response_get_result_type_custom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


