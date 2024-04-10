# DomainResponseWithResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**total_pages** | **int** |  | 
**schema_version** | **int** |  | 
**links** | [**DomainLinks**](DomainLinks.md) |  | 
**results** | [**List[DomainEntity]**](DomainEntity.md) |  | 

## Example

```python
from domains.models.domain_response_with_results import DomainResponseWithResults

# TODO update the JSON string below
json = "{}"
# create an instance of DomainResponseWithResults from a JSON string
domain_response_with_results_instance = DomainResponseWithResults.from_json(json)
# print the JSON string representation of the object
print(DomainResponseWithResults.to_json())

# convert the object into a dict
domain_response_with_results_dict = domain_response_with_results_instance.to_dict()
# create an instance of DomainResponseWithResults from a dict
domain_response_with_results_form_dict = domain_response_with_results.from_dict(domain_response_with_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


