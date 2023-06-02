# edgeapplications.model.origins_result_response.OriginsResultResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**timeout_between_bytes** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**[addresses](#addresses)** | list, tuple,  | tuple,  |  | 
**hmac_secret_key** | str,  | str,  |  | 
**method** | str,  | str,  |  | 
**origin_path** | str,  | str,  |  | 
**hmac_region_name** | str,  | str,  |  | 
**origin_protocol_policy** | str,  | str,  |  | 
**hmac_access_key** | str,  | str,  |  | 
**is_origin_redirection_enabled** | bool,  | BoolClass,  |  | 
**origin_id** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**origin_type** | str,  | str,  |  | 
**host_header** | str,  | str,  |  | 
**origin_key** | str,  | str,  |  | 
**name** | str,  | str,  |  | 
**connection_timeout** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**hmac_authentication** | bool,  | BoolClass,  |  | 

# addresses

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OriginsResultResponseAddresses**](OriginsResultResponseAddresses.md) | [**OriginsResultResponseAddresses**](OriginsResultResponseAddresses.md) | [**OriginsResultResponseAddresses**](OriginsResultResponseAddresses.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

