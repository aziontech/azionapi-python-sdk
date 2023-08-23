# edgeapplications.model.create_application_request.CreateApplicationRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | 
**application_acceleration** | bool,  | BoolClass,  |  | [optional] 
**delivery_protocol** | str,  | str,  |  | [optional] 
**origin_type** | str,  | str,  |  | [optional] 
**address** | str,  | str,  |  | [optional] 
**origin_protocol_policy** | str,  | str,  |  | [optional] 
**host_header** | str,  | str,  |  | [optional] 
**browser_cache_settings** | str,  | str,  |  | [optional] 
**cdn_cache_settings** | str,  | str,  |  | [optional] 
**browser_cache_settings_maximum_ttl** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**cdn_cache_settings_maximum_ttl** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**debug_rules** | bool,  | BoolClass,  |  | [optional] 
**supported_ciphers** | str,  | str,  |  | [optional] 
**http_port** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**https_port** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**l2_caching** | bool,  | BoolClass,  |  | [optional] 
**http3** | bool,  | BoolClass,  |  | [optional] 
**websocket** | bool,  | BoolClass,  |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

