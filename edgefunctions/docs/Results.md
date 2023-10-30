# Results


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**json_args** | **object** |  | [optional] 
**function_to_run** | **str** |  | [optional] 
**initiator_type** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**last_editor** | **str** |  | [optional] 
**modified** | **str** |  | [optional] 
**reference_count** | **int** |  | [optional] 
**is_proprietary_code** | **bool** |  | [optional] 

## Example

```python
from edgefunctions.models.results import Results

# TODO update the JSON string below
json = "{}"
# create an instance of Results from a JSON string
results_instance = Results.from_json(json)
# print the JSON string representation of the object
print Results.to_json()

# convert the object into a dict
results_dict = results_instance.to_dict()
# create an instance of Results from a dict
results_form_dict = results.from_dict(results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


