# idns.model.zone.Zone

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  | Hosted zone id | [optional] 
**name** | str,  | str,  | Hosted zone name | [optional] 
**domain** | str,  | str,  | Hosted zone domain | [optional] 
**is_active** | bool,  | BoolClass,  | If hosted zone is active | [optional] 
**retry** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] 
**nx_ttl** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] 
**soa_ttl** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] 
**refresh** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] 
**expiry** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] 
**[nameservers](#nameservers)** | list, tuple, None,  | tuple, NoneClass,  | List of nameservers | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# nameservers

List of nameservers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  | List of nameservers | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

