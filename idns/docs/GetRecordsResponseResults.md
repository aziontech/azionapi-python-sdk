# GetRecordsResponseResults


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_id** | **int** |  | [optional] 
**zone_domain** | **str** |  | [optional] 
**records** | [**List[RecordGet]**](RecordGet.md) | Zone records collection | [optional] 

## Example

```python
from idns.models.get_records_response_results import GetRecordsResponseResults

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecordsResponseResults from a JSON string
get_records_response_results_instance = GetRecordsResponseResults.from_json(json)
# print the JSON string representation of the object
print GetRecordsResponseResults.to_json()

# convert the object into a dict
get_records_response_results_dict = get_records_response_results_instance.to_dict()
# create an instance of GetRecordsResponseResults from a dict
get_records_response_results_form_dict = get_records_response_results.from_dict(get_records_response_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


