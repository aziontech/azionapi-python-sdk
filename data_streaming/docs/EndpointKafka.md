# EndpointKafka


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_type** | **str** |  | [optional] 
**kafka_topic** | **str** |  | [optional] 
**bootstrap_servers** | **str** |  | [optional] 
**use_tls** | **bool** |  | [optional] 

## Example

```python
from data_streaming.models.endpoint_kafka import EndpointKafka

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointKafka from a JSON string
endpoint_kafka_instance = EndpointKafka.from_json(json)
# print the JSON string representation of the object
print EndpointKafka.to_json()

# convert the object into a dict
endpoint_kafka_dict = endpoint_kafka_instance.to_dict()
# create an instance of EndpointKafka from a dict
endpoint_kafka_form_dict = endpoint_kafka.from_dict(endpoint_kafka_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


