# DataStreamingResponseWithResultsResultsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**template_id** | **int** |  | [optional] 
**data_source** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**endpoint** | [**DataStreamingEndpointTypeKafka**](DataStreamingEndpointTypeKafka.md) |  | [optional] 
**all_domains** | **bool** |  | [optional] 
**template_model** | **str** |  | [optional] 

## Example

```python
from data_streaming.models.data_streaming_response_with_results_results_inner import DataStreamingResponseWithResultsResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DataStreamingResponseWithResultsResultsInner from a JSON string
data_streaming_response_with_results_results_inner_instance = DataStreamingResponseWithResultsResultsInner.from_json(json)
# print the JSON string representation of the object
print DataStreamingResponseWithResultsResultsInner.to_json()

# convert the object into a dict
data_streaming_response_with_results_results_inner_dict = data_streaming_response_with_results_results_inner_instance.to_dict()
# create an instance of DataStreamingResponseWithResultsResultsInner from a dict
data_streaming_response_with_results_results_inner_form_dict = data_streaming_response_with_results_results_inner.from_dict(data_streaming_response_with_results_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


