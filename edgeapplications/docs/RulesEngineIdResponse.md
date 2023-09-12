# RulesEngineIdResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**RulesEngineResultResponse**](RulesEngineResultResponse.md) |  | 
**schema_version** | **int** |  | 

## Example

```python
from edgeapplications.models.rules_engine_id_response import RulesEngineIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineIdResponse from a JSON string
rules_engine_id_response_instance = RulesEngineIdResponse.from_json(json)
# print the JSON string representation of the object
print RulesEngineIdResponse.to_json()

# convert the object into a dict
rules_engine_id_response_dict = rules_engine_id_response_instance.to_dict()
# create an instance of RulesEngineIdResponse from a dict
rules_engine_id_response_form_dict = rules_engine_id_response.from_dict(rules_engine_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


