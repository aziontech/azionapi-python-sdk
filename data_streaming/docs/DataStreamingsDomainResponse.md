# DataStreamingsDomainResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**schema_version** | **float** |  | [optional] 
**links** | [**DataStreamingsDomainResponseLinks**](DataStreamingsDomainResponseLinks.md) |  | [optional] 
**results** | [**List[DataStreamingsDomainResult]**](DataStreamingsDomainResult.md) |  | [optional] 

## Example

```python
from data_streaming.models.data_streamings_domain_response import DataStreamingsDomainResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DataStreamingsDomainResponse from a JSON string
data_streamings_domain_response_instance = DataStreamingsDomainResponse.from_json(json)
# print the JSON string representation of the object
print DataStreamingsDomainResponse.to_json()

# convert the object into a dict
data_streamings_domain_response_dict = data_streamings_domain_response_instance.to_dict()
# create an instance of DataStreamingsDomainResponse from a dict
data_streamings_domain_response_form_dict = data_streamings_domain_response.from_dict(data_streamings_domain_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


