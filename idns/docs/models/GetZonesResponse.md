# idns.model.get_zones_response.GetZonesResponse

Object returned by get zones

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object returned by get zones | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**schema_version** | decimal.Decimal, int,  | decimal.Decimal,  | The schema version | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  | Number of records | [optional] 
**total_pages** | decimal.Decimal, int,  | decimal.Decimal,  | The total pages | [optional] 
**links** | [**GetZonesResponseLinks**](GetZonesResponseLinks.md) | [**GetZonesResponseLinks**](GetZonesResponseLinks.md) |  | [optional] 
**[results](#results)** | list, tuple,  | tuple,  | Hosted zones collection | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# results

Hosted zones collection

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Hosted zones collection | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Zone**](Zone.md) | [**Zone**](Zone.md) | [**Zone**](Zone.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

