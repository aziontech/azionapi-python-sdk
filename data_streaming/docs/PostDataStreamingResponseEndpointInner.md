# PostDataStreamingResponseEndpointInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**log_line_separator** | **str** |  | [optional] 
**payload_format** | **str** |  | [optional] 
**max_size** | **int** |  | [optional] 
**headers** | **List[Dict[str, str]]** |  | [optional] 
**kafka_topic** | **str** |  | [optional] 
**bootstrap_servers** | **str** |  | [optional] 
**use_tls** | **bool** |  | [optional] 
**access_key** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**object_key_prefix** | **str** |  | [optional] 
**bucket_name** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**host_url** | **str** |  | [optional] 
**secret_key** | **str** |  | [optional] 
**dataset_id** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**table_id** | **str** |  | [optional] 
**service_account_key** | [**EndpointGoogleBigQueryServiceAccountKey**](EndpointGoogleBigQueryServiceAccountKey.md) |  | [optional] 
**api_key** | **str** |  | [optional] 
**stream_name** | **str** |  | [optional] 
**log_type** | **str** |  | [optional] 
**shared_key** | **str** |  | [optional] 
**time_generated_field** | **str** |  | [optional] 
**workspace_id** | **str** |  | [optional] 
**storage_account** | **str** |  | [optional] 
**container_name** | **str** |  | [optional] 
**blob_sas_token** | **str** |  | [optional] 

## Example

```python
from data_streaming.models.post_data_streaming_response_endpoint_inner import PostDataStreamingResponseEndpointInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostDataStreamingResponseEndpointInner from a JSON string
post_data_streaming_response_endpoint_inner_instance = PostDataStreamingResponseEndpointInner.from_json(json)
# print the JSON string representation of the object
print PostDataStreamingResponseEndpointInner.to_json()

# convert the object into a dict
post_data_streaming_response_endpoint_inner_dict = post_data_streaming_response_endpoint_inner_instance.to_dict()
# create an instance of PostDataStreamingResponseEndpointInner from a dict
post_data_streaming_response_endpoint_inner_form_dict = post_data_streaming_response_endpoint_inner.from_dict(post_data_streaming_response_endpoint_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


