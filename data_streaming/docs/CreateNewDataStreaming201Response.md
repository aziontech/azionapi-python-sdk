# CreateNewDataStreaming201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PostCustomDataStreamingResponse]**](PostCustomDataStreamingResponse.md) |  | [optional] 
**schema_version** | **float** |  | [optional] 

## Example

```python
from data_streaming.models.create_new_data_streaming201_response import CreateNewDataStreaming201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNewDataStreaming201Response from a JSON string
create_new_data_streaming201_response_instance = CreateNewDataStreaming201Response.from_json(json)
# print the JSON string representation of the object
print CreateNewDataStreaming201Response.to_json()

# convert the object into a dict
create_new_data_streaming201_response_dict = create_new_data_streaming201_response_instance.to_dict()
# create an instance of CreateNewDataStreaming201Response from a dict
create_new_data_streaming201_response_form_dict = create_new_data_streaming201_response.from_dict(create_new_data_streaming201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


