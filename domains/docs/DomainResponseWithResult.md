# DomainResponseWithResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**links** | [**DomainLinks**](DomainLinks.md) |  | [optional] 
**results** | [**DomainEntityResponse**](DomainEntityResponse.md) |  | 
**total_pages** | **int** |  | [optional] 
**schema_version** | **int** |  | 

## Example

```python
from domains.models.domain_response_with_result import DomainResponseWithResult

# TODO update the JSON string below
json = "{}"
# create an instance of DomainResponseWithResult from a JSON string
domain_response_with_result_instance = DomainResponseWithResult.from_json(json)
# print the JSON string representation of the object
print(DomainResponseWithResult.to_json())

# convert the object into a dict
domain_response_with_result_dict = domain_response_with_result_instance.to_dict()
# create an instance of DomainResponseWithResult from a dict
domain_response_with_result_from_dict = DomainResponseWithResult.from_dict(domain_response_with_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


