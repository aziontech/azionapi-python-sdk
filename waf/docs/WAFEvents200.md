# WAFEvents200


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | **List[object]** |  | [optional] 
**schema_version** | **int** |  | [optional] 

## Example

```python
from waf.models.waf_events200 import WAFEvents200

# TODO update the JSON string below
json = "{}"
# create an instance of WAFEvents200 from a JSON string
waf_events200_instance = WAFEvents200.from_json(json)
# print the JSON string representation of the object
print WAFEvents200.to_json()

# convert the object into a dict
waf_events200_dict = waf_events200_instance.to_dict()
# create an instance of WAFEvents200 from a dict
waf_events200_form_dict = waf_events200.from_dict(waf_events200_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


