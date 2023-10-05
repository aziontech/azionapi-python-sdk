# GetZoneResponse

Object returned by get zone

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **int** | The schema version | [optional] 
**results** | [**Zone**](Zone.md) |  | [optional] 

## Example

```python
from idns.models.get_zone_response import GetZoneResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetZoneResponse from a JSON string
get_zone_response_instance = GetZoneResponse.from_json(json)
# print the JSON string representation of the object
print GetZoneResponse.to_json()

# convert the object into a dict
get_zone_response_dict = get_zone_response_instance.to_dict()
# create an instance of GetZoneResponse from a dict
get_zone_response_form_dict = get_zone_response.from_dict(get_zone_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


