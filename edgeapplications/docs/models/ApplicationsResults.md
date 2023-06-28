# edgeapplications.model.applications_results.ApplicationsResults

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**name** | str,  | str,  |  | [optional] 
**debug_rules** | bool,  | BoolClass,  |  | [optional] 
**last_editor** | str,  | str,  |  | [optional] 
**last_modified** | str,  | str,  |  | [optional] 
**active** | bool,  | BoolClass,  |  | [optional] 
**[origins](#origins)** | list, tuple,  | tuple,  |  | [optional] 

# origins

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApplicationOrigins**](ApplicationOrigins.md) | [**ApplicationOrigins**](ApplicationOrigins.md) | [**ApplicationOrigins**](ApplicationOrigins.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

