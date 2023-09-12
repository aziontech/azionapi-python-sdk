# EndpointDefault


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**log_line_separator** | **str** |  | [optional] 
**payload_format** | **str** |  | [optional] 
**max_size** | **int** |  | [optional] 
**headers** | **List[Dict[str, str]]** |  | [optional] 

## Example

```python
from data_streaming.models.endpoint_default import EndpointDefault

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointDefault from a JSON string
endpoint_default_instance = EndpointDefault.from_json(json)
# print the JSON string representation of the object
print EndpointDefault.to_json()

# convert the object into a dict
endpoint_default_dict = endpoint_default_instance.to_dict()
# create an instance of EndpointDefault from a dict
endpoint_default_form_dict = endpoint_default.from_dict(endpoint_default_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


