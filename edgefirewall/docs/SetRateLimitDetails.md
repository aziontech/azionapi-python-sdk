# SetRateLimitDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**limit_by** | **str** |  | [optional] 
**average_rate_limit** | **int** |  | [optional] 
**maximum_burst_size** | **int** |  | [optional] 

## Example

```python
from edgefirewall.models.set_rate_limit_details import SetRateLimitDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SetRateLimitDetails from a JSON string
set_rate_limit_details_instance = SetRateLimitDetails.from_json(json)
# print the JSON string representation of the object
print SetRateLimitDetails.to_json()

# convert the object into a dict
set_rate_limit_details_dict = set_rate_limit_details_instance.to_dict()
# create an instance of SetRateLimitDetails from a dict
set_rate_limit_details_form_dict = set_rate_limit_details.from_dict(set_rate_limit_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


