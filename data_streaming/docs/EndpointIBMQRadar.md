# EndpointIBMQRadar


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from data_streaming.models.endpoint_ibmq_radar import EndpointIBMQRadar

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointIBMQRadar from a JSON string
endpoint_ibmq_radar_instance = EndpointIBMQRadar.from_json(json)
# print the JSON string representation of the object
print EndpointIBMQRadar.to_json()

# convert the object into a dict
endpoint_ibmq_radar_dict = endpoint_ibmq_radar_instance.to_dict()
# create an instance of EndpointIBMQRadar from a dict
endpoint_ibmq_radar_form_dict = endpoint_ibmq_radar.from_dict(endpoint_ibmq_radar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


