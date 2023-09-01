# EndpointElasticsearch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**api_key** | **object** |  | [optional] 

## Example

```python
from data_streaming.models.endpoint_elasticsearch import EndpointElasticsearch

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointElasticsearch from a JSON string
endpoint_elasticsearch_instance = EndpointElasticsearch.from_json(json)
# print the JSON string representation of the object
print EndpointElasticsearch.to_json()

# convert the object into a dict
endpoint_elasticsearch_dict = endpoint_elasticsearch_instance.to_dict()
# create an instance of EndpointElasticsearch from a dict
endpoint_elasticsearch_form_dict = endpoint_elasticsearch.from_dict(endpoint_elasticsearch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


