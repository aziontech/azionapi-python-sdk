# DataStreamingPostBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**template_id** | **int** | Options:  * &#x60;2&#x60; - Edge Applications Event Collector  * &#x60;4&#x60; - WAF Event Collector  * &#x60;86&#x60; - Edge Functions Event Collector  * &#x60;184&#x60; - Edge Applications + WAF Event Collector  * &#x60;251&#x60; - Activity History Collector  | [optional] 
**data_source** | **str** | Options:  * &#x60;http&#x60; - Edge Applications (default)  * &#x60;waf&#x60; - WAF Events  * &#x60;cells_console&#x60; - Edge Functions  * &#x60;rtm_activity&#x60; - Activity History  | [optional] 
**active** | **bool** |  | [optional] [default to True]
**endpoint** | **str** | Options&#39; examples:  - &#x60;Standard HTTP/HTTPS POST&#x60; - { \&quot;endpoint_type\&quot;: \&quot;standard\&quot;, \&quot;url\&quot;: \&quot;http://example.com\&quot;, \&quot;log_line_separator\&quot;: \&quot;\\n\&quot;, \&quot;payload_format\&quot;: \&quot;$dataset\&quot;, \&quot;max_size\&quot;: 1000024 }  - &#x60;Apache Kafka&#x60; - { \&quot;endpoint_type\&quot;: \&quot;kafka\&quot;, \&quot;kafka_topic\&quot;: \&quot;example_topic\&quot;, \&quot;bootstrap_servers\&quot;: \&quot;kafka-server.com:9092,kafka-server-2.com:9092\&quot;, \&quot;use_tls\&quot;:true }  - &#x60;Simple Storage Service (S3)&#x60; - { \&quot;endpoint_type\&quot;: \&quot;s3\&quot;, \&quot;access_key\&quot;: \&quot;MYACCESSKEY\&quot;, \&quot;region\&quot;: \&quot;us-east-1\&quot;, \&quot;object_key_prefix\&quot;: \&quot;my_prefix_\&quot;, \&quot;bucket_name\&quot;: \&quot;bucket_example\&quot;, \&quot;content_type\&quot;: \&quot;plain/text\&quot;, \&quot;host_url\&quot;: \&quot;http://aws-host.com\&quot;, \&quot;secret_key\&quot;: \&quot;MYSECRETKEY\&quot; }  - &#x60;Google BigQuery&#x60; - { \&quot;endpoint_type\&quot;: \&quot;big_query\&quot;, \&quot;dataset_id\&quot;: \&quot;my_dataset\&quot;, \&quot;project_id\&quot;: \&quot;my_project\&quot;, \&quot;table_id\&quot;: \&quot;my_table\&quot;, \&quot;service_account_key\&quot;: \&quot;{ \&quot;service_account_key\&quot;: \&quot;key_content\&quot; }\&quot; }  - &#x60;Elasticsearch&#x60; - { “endpoint_type”: \&quot;elasticsearch\&quot;, “url”: “http://elasticsearch.com”, “api_key”: “XYZ_API_KEY” }  - &#x60;AWS Kinesis Data Firehose&#x60; -  { \&quot;endpoint_type\&quot;: \&quot;aws_kinesis_firehose\&quot;, \&quot;access_key\&quot;: \&quot;MYACCESSKEY\&quot;, \&quot;stream_name\&quot;: \&quot;my_stream_name\&quot;, \&quot;region\&quot;: \&quot;us-east-1\&quot;, \&quot;secret_key\&quot;: \&quot;MYSECRETKEY\&quot; }  - &#x60;Datadog&#x60; - { \&quot;endpoint_type\&quot;: \&quot;datadog\&quot;, \&quot;url\&quot;: \&quot;https://http-intake.logs.datadoghq.com/v1/input\&quot;, \&quot;api_key\&quot;: \&quot;MYAPIKEY\&quot; }  - &#x60;IBM QRadar&#x60; - { \&quot;endpoint_type\&quot;: \&quot;qradar\&quot;, \&quot;url\&quot;: \&quot;http://137.15.824.10:14440” }  - &#x60;Azure Monitor&#x60; - { \&quot;endpoint_type\&quot;: \&quot;azure_monitor\&quot;, \&quot;log_type\&quot;: \&quot;myLogType\&quot;, \&quot;shared_key\&quot;: \&quot;mysharedkey\&quot;, \&quot;time_generated_field\&quot;: \&quot;timeGeneratedField\&quot;, \&quot;workspace_id\&quot;: \&quot;anfhw-123sd-466gcs\&quot;}  - &#x60;Azure Blob Storage&#x60; - { \&quot;endpoint_type\&quot;: \&quot;azure_blob_storage\&quot;, \&quot;storage_account\&quot;: \&quot;mystorageaccount\&quot;, \&quot;container_name\&quot;: \&quot;log_container\&quot;, \&quot;blob_sas_token\&quot;: \&quot;fd56e23e1f12efe\&quot; }  - &#x60;Splunk&#x60; - { \&quot;endpoint_type\&quot;: \&quot;splunk\&quot;, \&quot;url\&quot;: \&quot;https://inputs.splunk-client.splunkcloud.com:1337/services/collector\&quot;, \&quot;api_key\&quot;: \&quot;MYAPIKEY\&quot; }  | [optional] 
**domains_ids** | **List[int]** | Note:  * Field not used with the rtm_activity data source.  | [optional] 
**all_domains** | **bool** | Note:  * Field not used with the rtm_activity data source.  | [optional] [default to False]
**sampling_percentage** | **int** | Note:  * &#x60;Range&#x60; - From 0 to 100.  * &#x60;To use:&#x60; [Contact the sales team](https://www.azion.com/en/contact-sales/) to activate this feature in your account.  | [optional] 

## Example

```python
from data_streaming.models.data_streaming_post_body import DataStreamingPostBody

# TODO update the JSON string below
json = "{}"
# create an instance of DataStreamingPostBody from a JSON string
data_streaming_post_body_instance = DataStreamingPostBody.from_json(json)
# print the JSON string representation of the object
print DataStreamingPostBody.to_json()

# convert the object into a dict
data_streaming_post_body_dict = data_streaming_post_body_instance.to_dict()
# create an instance of DataStreamingPostBody from a dict
data_streaming_post_body_form_dict = data_streaming_post_body.from_dict(data_streaming_post_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


