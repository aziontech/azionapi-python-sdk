# OriginsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**total_pages** | **int** |  | 
**schema_version** | **int** |  | 
**links** | [**OriginsResponseLinks**](OriginsResponseLinks.md) |  | 
**results** | [**List[OriginsResultResponse]**](OriginsResultResponse.md) |  | 

## Example

```python
from edgeapplications.models.origins_response import OriginsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OriginsResponse from a JSON string
origins_response_instance = OriginsResponse.from_json(json)
# print the JSON string representation of the object
print(OriginsResponse.to_json())

# convert the object into a dict
origins_response_dict = origins_response_instance.to_dict()
# create an instance of OriginsResponse from a dict
origins_response_from_dict = OriginsResponse.from_dict(origins_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


