# DataStreamingsById


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**DataStreamingResponseGetResultTypeKafka**](DataStreamingResponseGetResultTypeKafka.md) |  | [optional] 
**schema_version** | **float** |  | [optional] 

## Example

```python
from data_streaming.models.data_streamings_by_id import DataStreamingsById

# TODO update the JSON string below
json = "{}"
# create an instance of DataStreamingsById from a JSON string
data_streamings_by_id_instance = DataStreamingsById.from_json(json)
# print the JSON string representation of the object
print DataStreamingsById.to_json()

# convert the object into a dict
data_streamings_by_id_dict = data_streamings_by_id_instance.to_dict()
# create an instance of DataStreamingsById from a dict
data_streamings_by_id_form_dict = data_streamings_by_id.from_dict(data_streamings_by_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


