# WAFEvents400


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[object]** |  | [optional] 
**schema_version** | **int** |  | [optional] 

## Example

```python
from waf.models.waf_events400 import WAFEvents400

# TODO update the JSON string below
json = "{}"
# create an instance of WAFEvents400 from a JSON string
waf_events400_instance = WAFEvents400.from_json(json)
# print the JSON string representation of the object
print WAFEvents400.to_json()

# convert the object into a dict
waf_events400_dict = waf_events400_instance.to_dict()
# create an instance of WAFEvents400 from a dict
waf_events400_form_dict = waf_events400.from_dict(waf_events400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


