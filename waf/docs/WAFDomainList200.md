# WAFDomainList200


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**cnames** | **List[str]** |  | [optional] 

## Example

```python
from waf.models.waf_domain_list200 import WAFDomainList200

# TODO update the JSON string below
json = "{}"
# create an instance of WAFDomainList200 from a JSON string
waf_domain_list200_instance = WAFDomainList200.from_json(json)
# print the JSON string representation of the object
print WAFDomainList200.to_json()

# convert the object into a dict
waf_domain_list200_dict = waf_domain_list200_instance.to_dict()
# create an instance of WAFDomainList200 from a dict
waf_domain_list200_form_dict = waf_domain_list200.from_dict(waf_domain_list200_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


