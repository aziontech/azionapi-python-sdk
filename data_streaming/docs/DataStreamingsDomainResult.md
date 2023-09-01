# DataStreamingsDomainResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**selected** | **bool** |  | [optional] 

## Example

```python
from data_streaming.models.data_streamings_domain_result import DataStreamingsDomainResult

# TODO update the JSON string below
json = "{}"
# create an instance of DataStreamingsDomainResult from a JSON string
data_streamings_domain_result_instance = DataStreamingsDomainResult.from_json(json)
# print the JSON string representation of the object
print DataStreamingsDomainResult.to_json()

# convert the object into a dict
data_streamings_domain_result_dict = data_streamings_domain_result_instance.to_dict()
# create an instance of DataStreamingsDomainResult from a dict
data_streamings_domain_result_form_dict = data_streamings_domain_result.from_dict(data_streamings_domain_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


