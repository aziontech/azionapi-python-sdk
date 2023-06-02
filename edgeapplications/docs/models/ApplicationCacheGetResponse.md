# edgeapplications.model.application_cache_get_response.ApplicationCacheGetResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**schema_version** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**count** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**links** | [**ApplicationLinks**](ApplicationLinks.md) | [**ApplicationLinks**](ApplicationLinks.md) |  | 
**total_pages** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**[results](#results)** | list, tuple,  | tuple,  |  | 

# results

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApplicationCacheResults**](ApplicationCacheResults.md) | [**ApplicationCacheResults**](ApplicationCacheResults.md) | [**ApplicationCacheResults**](ApplicationCacheResults.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

