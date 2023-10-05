# GetZonesResponseLinks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous** | **str** |  | [optional] 
**next** | **str** |  | [optional] 

## Example

```python
from idns.models.get_zones_response_links import GetZonesResponseLinks

# TODO update the JSON string below
json = "{}"
# create an instance of GetZonesResponseLinks from a JSON string
get_zones_response_links_instance = GetZonesResponseLinks.from_json(json)
# print the JSON string representation of the object
print GetZonesResponseLinks.to_json()

# convert the object into a dict
get_zones_response_links_dict = get_zones_response_links_instance.to_dict()
# create an instance of GetZonesResponseLinks from a dict
get_zones_response_links_form_dict = get_zones_response_links.from_dict(get_zones_response_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


