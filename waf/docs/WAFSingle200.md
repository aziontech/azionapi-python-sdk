# WAFSingle200


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**SingleWAF**](SingleWAF.md) |  | [optional] 
**schema_version** | **int** |  | [optional] 

## Example

```python
from waf.models.waf_single200 import WAFSingle200

# TODO update the JSON string below
json = "{}"
# create an instance of WAFSingle200 from a JSON string
waf_single200_instance = WAFSingle200.from_json(json)
# print the JSON string representation of the object
print WAFSingle200.to_json()

# convert the object into a dict
waf_single200_dict = waf_single200_instance.to_dict()
# create an instance of WAFSingle200 from a dict
waf_single200_form_dict = waf_single200.from_dict(waf_single200_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


