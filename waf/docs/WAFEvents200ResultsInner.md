# WAFEvents200ResultsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_count** | **int** |  | [optional] 
**top_10_countries** | **List[str]** |  | [optional] 
**top_10_ips** | **List[str]** |  | [optional] 
**hit_count** | **int** |  | [optional] 
**rule_id** | **int** |  | [optional] 
**ip_count** | **int** |  | [optional] 
**match_zone** | **str** |  | [optional] 
**path_count** | **int** |  | [optional] 
**matches_on** | **str** |  | [optional] 
**rule_description** | **str** |  | [optional] 

## Example

```python
from waf.models.waf_events200_results_inner import WAFEvents200ResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of WAFEvents200ResultsInner from a JSON string
waf_events200_results_inner_instance = WAFEvents200ResultsInner.from_json(json)
# print the JSON string representation of the object
print WAFEvents200ResultsInner.to_json()

# convert the object into a dict
waf_events200_results_inner_dict = waf_events200_results_inner_instance.to_dict()
# create an instance of WAFEvents200ResultsInner from a dict
waf_events200_results_inner_form_dict = waf_events200_results_inner.from_dict(waf_events200_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


