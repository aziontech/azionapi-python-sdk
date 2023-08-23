# data_streaming.model.data_streaming_response_with_results.DataStreamingResponseWithResults

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[results](#results)** | list, tuple,  | tuple,  |  | [optional] 
**schema_version** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# results

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
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[DataStreamingResponseGetResultTypeDatadogDTS](DataStreamingResponseGetResultTypeDatadogDTS.md) | [**DataStreamingResponseGetResultTypeDatadogDTS**](DataStreamingResponseGetResultTypeDatadogDTS.md) | [**DataStreamingResponseGetResultTypeDatadogDTS**](DataStreamingResponseGetResultTypeDatadogDTS.md) |  | 
[DataStreamingResponseGetResultTypeKafka](DataStreamingResponseGetResultTypeKafka.md) | [**DataStreamingResponseGetResultTypeKafka**](DataStreamingResponseGetResultTypeKafka.md) | [**DataStreamingResponseGetResultTypeKafka**](DataStreamingResponseGetResultTypeKafka.md) |  | 
[DataStreamingResponseGetResultTypeStandard](DataStreamingResponseGetResultTypeStandard.md) | [**DataStreamingResponseGetResultTypeStandard**](DataStreamingResponseGetResultTypeStandard.md) | [**DataStreamingResponseGetResultTypeStandard**](DataStreamingResponseGetResultTypeStandard.md) |  | 
[DataStreamingResponseGetResultTypeCustom](DataStreamingResponseGetResultTypeCustom.md) | [**DataStreamingResponseGetResultTypeCustom**](DataStreamingResponseGetResultTypeCustom.md) | [**DataStreamingResponseGetResultTypeCustom**](DataStreamingResponseGetResultTypeCustom.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

