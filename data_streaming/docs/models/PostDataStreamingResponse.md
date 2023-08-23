# data_streaming.model.post_data_streaming_response.PostDataStreamingResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**template_id** | decimal.Decimal, int,  | decimal.Decimal,  | Options:  * &#x60;2&#x60; - Edge Applications Event Collector  * &#x60;4&#x60; - WAF Event Collector  * &#x60;86&#x60; - Edge Functions Event Collector  * &#x60;184&#x60; - Edge Applications + WAF Event Collector  * &#x60;251&#x60; - Activity History Collector  | [optional] must be one of [2, 4, 86, 184, 251, ] 
**data_source** | str,  | str,  | Options:  * &#x60;http&#x60; - Edge Applications  * &#x60;waf&#x60; - WAF Events  * &#x60;cells_console&#x60; - Edge Functions  * &#x60;rtm_activity&#x60; - Activity History  | [optional] must be one of ["http", "waf", "cells_console", "rtm_activity", ] 
**active** | bool,  | BoolClass,  |  | [optional] 
**[endpoint](#endpoint)** | list, tuple,  | tuple,  |  | [optional] 
**all_domains** | None, bool,  | NoneClass, BoolClass,  | Note:  * Field not used with the rtm_activity data source.  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# endpoint

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[EndpointDefault](EndpointDefault.md) | [**EndpointDefault**](EndpointDefault.md) | [**EndpointDefault**](EndpointDefault.md) |  | 
[EndpointKafka](EndpointKafka.md) | [**EndpointKafka**](EndpointKafka.md) | [**EndpointKafka**](EndpointKafka.md) |  | 
[EndpoinrtS3](EndpoinrtS3.md) | [**EndpoinrtS3**](EndpoinrtS3.md) | [**EndpoinrtS3**](EndpoinrtS3.md) |  | 
[EndpointGoogleBigQuery](EndpointGoogleBigQuery.md) | [**EndpointGoogleBigQuery**](EndpointGoogleBigQuery.md) | [**EndpointGoogleBigQuery**](EndpointGoogleBigQuery.md) |  | 
[EndpointElasticsearch](EndpointElasticsearch.md) | [**EndpointElasticsearch**](EndpointElasticsearch.md) | [**EndpointElasticsearch**](EndpointElasticsearch.md) |  | 
[EndpointAWSKinesisFirehose](EndpointAWSKinesisFirehose.md) | [**EndpointAWSKinesisFirehose**](EndpointAWSKinesisFirehose.md) | [**EndpointAWSKinesisFirehose**](EndpointAWSKinesisFirehose.md) |  | 
[EndpointDatadog](EndpointDatadog.md) | [**EndpointDatadog**](EndpointDatadog.md) | [**EndpointDatadog**](EndpointDatadog.md) |  | 
[EndpointIBMQRadar](EndpointIBMQRadar.md) | [**EndpointIBMQRadar**](EndpointIBMQRadar.md) | [**EndpointIBMQRadar**](EndpointIBMQRadar.md) |  | 
[EndpointAzureMonitor](EndpointAzureMonitor.md) | [**EndpointAzureMonitor**](EndpointAzureMonitor.md) | [**EndpointAzureMonitor**](EndpointAzureMonitor.md) |  | 
[EndpointAzureBlobStorage](EndpointAzureBlobStorage.md) | [**EndpointAzureBlobStorage**](EndpointAzureBlobStorage.md) | [**EndpointAzureBlobStorage**](EndpointAzureBlobStorage.md) |  | 
[EndpointSplunk](EndpointSplunk.md) | [**EndpointSplunk**](EndpointSplunk.md) | [**EndpointSplunk**](EndpointSplunk.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

