# domains.model.domain_results.DomainResults

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**content_type** | 
**updated_at** | 
**last_editor** | 
**name** | str,  | str,  |  | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**type** | 
**[cnames](#cnames)** | list, tuple,  | tuple,  |  | [optional] 
**cname_access_only** | bool,  | BoolClass,  |  | [optional] 
**is_active** | bool,  | BoolClass,  |  | [optional] 
**edge_application_id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**digital_certificate_id** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**domain_name** | str,  | str,  |  | [optional] 
**environment** | str,  | str,  |  | [optional] 

# cnames

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

