# WAFEvents404


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[object]** |  | [optional] 
**schema_version** | **int** |  | [optional] 

## Example

```python
from waf.models.waf_events404 import WAFEvents404

# TODO update the JSON string below
json = "{}"
# create an instance of WAFEvents404 from a JSON string
waf_events404_instance = WAFEvents404.from_json(json)
# print the JSON string representation of the object
print WAFEvents404.to_json()

# convert the object into a dict
waf_events404_dict = waf_events404_instance.to_dict()
# create an instance of WAFEvents404 from a dict
waf_events404_form_dict = waf_events404.from_dict(waf_events404_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


