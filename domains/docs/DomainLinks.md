# DomainLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous** | **str** |  | 
**next** | **str** |  | 

## Example

```python
from domains.models.domain_links import DomainLinks

# TODO update the JSON string below
json = "{}"
# create an instance of DomainLinks from a JSON string
domain_links_instance = DomainLinks.from_json(json)
# print the JSON string representation of the object
print(DomainLinks.to_json())

# convert the object into a dict
domain_links_dict = domain_links_instance.to_dict()
# create an instance of DomainLinks from a dict
domain_links_from_dict = DomainLinks.from_dict(domain_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


