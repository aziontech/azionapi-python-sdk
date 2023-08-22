# data_streaming.model.post_custom_data_streaming_response.PostCustomDataStreamingResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**data_source** | str,  | str,  | Options:  * &#x60;http&#x60; - Edge Applications  * &#x60;waf&#x60; - WAF Events  * &#x60;cells_console&#x60; - Edge Functions  * &#x60;rtm_activity&#x60; - Activity History    | [optional] must be one of ["http", "waf", "cells_console", "rtm_activity", ] 
**template_model** | str,  | str,  | Note:  * Add all variables and values that will be used to stream according to the data source you choose to use.    | [optional] 
**active** | bool,  | BoolClass,  |  | [optional] 
**endpoint** | str,  | str,  |  | [optional] 
**all_domains** | None, bool,  | NoneClass, BoolClass,  | Note:  * Field not used with the rtm_activity data source.  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

