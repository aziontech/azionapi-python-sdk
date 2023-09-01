# DataStreamingEndpointTypeKafka


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_type** | **str** |  | [optional] 
**use_tls** | **bool** |  | [optional] 
**kafka_topic** | **str** |  | [optional] 
**bootstrap_servers** | **str** |  | [optional] 

## Example

```python
from data_streaming.models.data_streaming_endpoint_type_kafka import DataStreamingEndpointTypeKafka

# TODO update the JSON string below
json = "{}"
# create an instance of DataStreamingEndpointTypeKafka from a JSON string
data_streaming_endpoint_type_kafka_instance = DataStreamingEndpointTypeKafka.from_json(json)
# print the JSON string representation of the object
print DataStreamingEndpointTypeKafka.to_json()

# convert the object into a dict
data_streaming_endpoint_type_kafka_dict = data_streaming_endpoint_type_kafka_instance.to_dict()
# create an instance of DataStreamingEndpointTypeKafka from a dict
data_streaming_endpoint_type_kafka_form_dict = data_streaming_endpoint_type_kafka.from_dict(data_streaming_endpoint_type_kafka_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


