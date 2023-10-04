# WAFList200


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 
**results** | [**List[SingleWAF]**](SingleWAF.md) |  | [optional] 
**schema_version** | **int** |  | [optional] 

## Example

```python
from waf.models.waf_list200 import WAFList200

# TODO update the JSON string below
json = "{}"
# create an instance of WAFList200 from a JSON string
waf_list200_instance = WAFList200.from_json(json)
# print the JSON string representation of the object
print WAFList200.to_json()

# convert the object into a dict
waf_list200_dict = waf_list200_instance.to_dict()
# create an instance of WAFList200 from a dict
waf_list200_form_dict = waf_list200.from_dict(waf_list200_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


