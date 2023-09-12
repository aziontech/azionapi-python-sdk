# OriginsResultResponseAddresses


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**weight** | **str** |  | 
**server_role** | **str** |  | 
**is_active** | **bool** |  | 

## Example

```python
from edgeapplications.models.origins_result_response_addresses import OriginsResultResponseAddresses

# TODO update the JSON string below
json = "{}"
# create an instance of OriginsResultResponseAddresses from a JSON string
origins_result_response_addresses_instance = OriginsResultResponseAddresses.from_json(json)
# print the JSON string representation of the object
print OriginsResultResponseAddresses.to_json()

# convert the object into a dict
origins_result_response_addresses_dict = origins_result_response_addresses_instance.to_dict()
# create an instance of OriginsResultResponseAddresses from a dict
origins_result_response_addresses_form_dict = origins_result_response_addresses.from_dict(origins_result_response_addresses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


