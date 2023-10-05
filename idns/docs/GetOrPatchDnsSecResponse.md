# GetOrPatchDnsSecResponse

Object returned by get zone DNSSEC

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **int** | The schema version | [optional] 
**results** | [**DnsSec**](DnsSec.md) |  | [optional] 

## Example

```python
from idns.models.get_or_patch_dns_sec_response import GetOrPatchDnsSecResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrPatchDnsSecResponse from a JSON string
get_or_patch_dns_sec_response_instance = GetOrPatchDnsSecResponse.from_json(json)
# print the JSON string representation of the object
print GetOrPatchDnsSecResponse.to_json()

# convert the object into a dict
get_or_patch_dns_sec_response_dict = get_or_patch_dns_sec_response_instance.to_dict()
# create an instance of GetOrPatchDnsSecResponse from a dict
get_or_patch_dns_sec_response_form_dict = get_or_patch_dns_sec_response.from_dict(get_or_patch_dns_sec_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


