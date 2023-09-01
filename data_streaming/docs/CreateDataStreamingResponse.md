# CreateDataStreamingResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PostDataStreamingResponse]**](PostDataStreamingResponse.md) |  | [optional] 
**schema_version** | **float** |  | [optional] 

## Example

```python
from data_streaming.models.create_data_streaming_response import CreateDataStreamingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDataStreamingResponse from a JSON string
create_data_streaming_response_instance = CreateDataStreamingResponse.from_json(json)
# print the JSON string representation of the object
print CreateDataStreamingResponse.to_json()

# convert the object into a dict
create_data_streaming_response_dict = create_data_streaming_response_instance.to_dict()
# create an instance of CreateDataStreamingResponse from a dict
create_data_streaming_response_form_dict = create_data_streaming_response.from_dict(create_data_streaming_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


