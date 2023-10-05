# Zone


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Hosted zone id | [optional] 
**name** | **str** | Hosted zone name | [optional] 
**domain** | **str** | Hosted zone domain | [optional] 
**is_active** | **bool** | If hosted zone is active | [optional] 
**retry** | **int** |  | [optional] 
**nx_ttl** | **int** |  | [optional] 
**soa_ttl** | **int** |  | [optional] 
**refresh** | **int** |  | [optional] 
**expiry** | **int** |  | [optional] 
**nameservers** | **List[str]** | List of nameservers | [optional] 

## Example

```python
from idns.models.zone import Zone

# TODO update the JSON string below
json = "{}"
# create an instance of Zone from a JSON string
zone_instance = Zone.from_json(json)
# print the JSON string representation of the object
print Zone.to_json()

# convert the object into a dict
zone_dict = zone_instance.to_dict()
# create an instance of Zone from a dict
zone_form_dict = zone.from_dict(zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


