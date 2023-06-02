# edgeapplications.model.patch_origins_request.PatchOriginsRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**origin_type** | str,  | str,  |  | [optional] 
**[addresses](#addresses)** | list, tuple,  | tuple,  |  | [optional] 
**origin_protocol_policy** | str,  | str,  |  | [optional] 
**host_header** | str,  | str,  |  | [optional] 
**origin_path** | str,  | str,  |  | [optional] 
**hmac_authentication** | bool,  | BoolClass,  |  | [optional] 
**hmac_region_name** | str,  | str,  |  | [optional] 
**hmac_access_key** | str,  | str,  |  | [optional] 
**hmac_secret_key** | str,  | str,  |  | [optional] 

# addresses

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CreateOriginsRequestAddresses**](CreateOriginsRequestAddresses.md) | [**CreateOriginsRequestAddresses**](CreateOriginsRequestAddresses.md) | [**CreateOriginsRequestAddresses**](CreateOriginsRequestAddresses.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

