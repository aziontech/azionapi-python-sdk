# PostOrPutZoneResponse

Object returned by create or update zone

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **int** | The schema version | [optional] 
**results** | [**List[Zone]**](Zone.md) | The created hosted zone | [optional] 

## Example

```python
from idns.models.post_or_put_zone_response import PostOrPutZoneResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostOrPutZoneResponse from a JSON string
post_or_put_zone_response_instance = PostOrPutZoneResponse.from_json(json)
# print the JSON string representation of the object
print PostOrPutZoneResponse.to_json()

# convert the object into a dict
post_or_put_zone_response_dict = post_or_put_zone_response_instance.to_dict()
# create an instance of PostOrPutZoneResponse from a dict
post_or_put_zone_response_form_dict = post_or_put_zone_response.from_dict(post_or_put_zone_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


