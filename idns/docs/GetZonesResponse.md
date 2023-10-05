# GetZonesResponse

Object returned by get zones

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **int** | The schema version | [optional] 
**count** | **int** | Number of records | [optional] 
**total_pages** | **int** | The total pages | [optional] 
**links** | [**GetZonesResponseLinks**](GetZonesResponseLinks.md) |  | [optional] 
**results** | [**List[Zone]**](Zone.md) | Hosted zones collection | [optional] 

## Example

```python
from idns.models.get_zones_response import GetZonesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetZonesResponse from a JSON string
get_zones_response_instance = GetZonesResponse.from_json(json)
# print the JSON string representation of the object
print GetZonesResponse.to_json()

# convert the object into a dict
get_zones_response_dict = get_zones_response_instance.to_dict()
# create an instance of GetZonesResponse from a dict
get_zones_response_form_dict = get_zones_response.from_dict(get_zones_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


