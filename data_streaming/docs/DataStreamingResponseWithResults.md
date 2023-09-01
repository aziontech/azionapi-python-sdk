# DataStreamingResponseWithResults


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[DataStreamingResponseWithResultsResultsInner]**](DataStreamingResponseWithResultsResultsInner.md) |  | [optional] 
**schema_version** | **float** |  | [optional] 

## Example

```python
from data_streaming.models.data_streaming_response_with_results import DataStreamingResponseWithResults

# TODO update the JSON string below
json = "{}"
# create an instance of DataStreamingResponseWithResults from a JSON string
data_streaming_response_with_results_instance = DataStreamingResponseWithResults.from_json(json)
# print the JSON string representation of the object
print DataStreamingResponseWithResults.to_json()

# convert the object into a dict
data_streaming_response_with_results_dict = data_streaming_response_with_results_instance.to_dict()
# create an instance of DataStreamingResponseWithResults from a dict
data_streaming_response_with_results_form_dict = data_streaming_response_with_results.from_dict(data_streaming_response_with_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


