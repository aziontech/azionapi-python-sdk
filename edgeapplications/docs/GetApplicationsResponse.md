# GetApplicationsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**total_pages** | **int** |  | 
**schema_version** | **int** |  | 
**links** | [**ApplicationLinks**](ApplicationLinks.md) |  | 
**results** | [**List[ApplicationsResults]**](ApplicationsResults.md) |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 

## Example

```python
from edgeapplications.models.get_applications_response import GetApplicationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetApplicationsResponse from a JSON string
get_applications_response_instance = GetApplicationsResponse.from_json(json)
# print the JSON string representation of the object
print GetApplicationsResponse.to_json()

# convert the object into a dict
get_applications_response_dict = get_applications_response_instance.to_dict()
# create an instance of GetApplicationsResponse from a dict
get_applications_response_form_dict = get_applications_response.from_dict(get_applications_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


