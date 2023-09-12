# EndpointSplunk


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**api_key** | **str** |  | [optional] 

## Example

```python
from data_streaming.models.endpoint_splunk import EndpointSplunk

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointSplunk from a JSON string
endpoint_splunk_instance = EndpointSplunk.from_json(json)
# print the JSON string representation of the object
print EndpointSplunk.to_json()

# convert the object into a dict
endpoint_splunk_dict = endpoint_splunk_instance.to_dict()
# create an instance of EndpointSplunk from a dict
endpoint_splunk_form_dict = endpoint_splunk.from_dict(endpoint_splunk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


