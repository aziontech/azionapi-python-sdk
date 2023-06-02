# services.model.service_response.ServiceResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**updated_at** | str,  | str,  |  | 
**[permissions](#permissions)** | list, tuple,  | tuple,  |  | 
**last_editor** | str,  | str,  |  | 
**name** | str,  | str,  |  | 
**active** | bool,  | BoolClass,  |  | 
**bound_nodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**[variables](#variables)** | list, tuple,  | tuple,  |  | [optional] 

# permissions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# variables

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Variable**](Variable.md) | [**Variable**](Variable.md) | [**Variable**](Variable.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

