# RulesEngineResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**total_pages** | **int** |  | 
**schema_version** | **int** |  | 
**links** | [**OriginsResponseLinks**](OriginsResponseLinks.md) |  | 
**results** | [**List[RulesEngineResultResponse]**](RulesEngineResultResponse.md) |  | 

## Example

```python
from edgeapplications.models.rules_engine_response import RulesEngineResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineResponse from a JSON string
rules_engine_response_instance = RulesEngineResponse.from_json(json)
# print the JSON string representation of the object
print RulesEngineResponse.to_json()

# convert the object into a dict
rules_engine_response_dict = rules_engine_response_instance.to_dict()
# create an instance of RulesEngineResponse from a dict
rules_engine_response_form_dict = rules_engine_response.from_dict(rules_engine_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


