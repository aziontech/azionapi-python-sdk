# edgefirewall.model.edge_firewall.EdgeFirewall

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**name** | str,  | str,  |  | [optional] 
**is_active** | bool,  | BoolClass,  |  | [optional] 
**last_editor** | str,  | str,  |  | [optional] 
**last_modified** | str,  | str,  |  | [optional] 
**edge_functions_enabled** | bool,  | BoolClass,  |  | [optional] 
**network_protection_enabled** | bool,  | BoolClass,  |  | [optional] 
**waf_enabled** | bool,  | BoolClass,  |  | [optional] 
**debug_rules** | bool,  | BoolClass,  |  | [optional] 
**[domains](#domains)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# domains

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

