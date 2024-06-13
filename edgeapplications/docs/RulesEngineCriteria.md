# RulesEngineCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditional** | **str** |  | 
**variable** | **str** |  | 
**operator** | **str** |  | 
**input_value** | **str** |  | [optional] 

## Example

```python
from edgeapplications.models.rules_engine_criteria import RulesEngineCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of RulesEngineCriteria from a JSON string
rules_engine_criteria_instance = RulesEngineCriteria.from_json(json)
# print the JSON string representation of the object
print(RulesEngineCriteria.to_json())

# convert the object into a dict
rules_engine_criteria_dict = rules_engine_criteria_instance.to_dict()
# create an instance of RulesEngineCriteria from a dict
rules_engine_criteria_from_dict = RulesEngineCriteria.from_dict(rules_engine_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


