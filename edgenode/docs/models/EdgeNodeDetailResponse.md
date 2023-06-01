# edgenode.model.edge_node_detail_response.EdgeNodeDetailResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | 
**[groups](#groups)** | list, tuple,  | tuple,  |  | 
**has_services** | bool,  | BoolClass,  |  | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**modules** | [**EdgeNodeModules**](EdgeNodeModules.md) | [**EdgeNodeModules**](EdgeNodeModules.md) |  | 
**hash_id** | str,  | str,  |  | 

# groups

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NodeGroup**](NodeGroup.md) | [**NodeGroup**](NodeGroup.md) | [**NodeGroup**](NodeGroup.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

