# EndpointGoogleBigQuery


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_type** | **str** |  | [optional] 
**dataset_id** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**table_id** | **str** |  | [optional] 
**service_account_key** | [**EndpointGoogleBigQueryServiceAccountKey**](EndpointGoogleBigQueryServiceAccountKey.md) |  | [optional] 

## Example

```python
from data_streaming.models.endpoint_google_big_query import EndpointGoogleBigQuery

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointGoogleBigQuery from a JSON string
endpoint_google_big_query_instance = EndpointGoogleBigQuery.from_json(json)
# print the JSON string representation of the object
print EndpointGoogleBigQuery.to_json()

# convert the object into a dict
endpoint_google_big_query_dict = endpoint_google_big_query_instance.to_dict()
# create an instance of EndpointGoogleBigQuery from a dict
endpoint_google_big_query_form_dict = endpoint_google_big_query.from_dict(endpoint_google_big_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


