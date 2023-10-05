# DnsSec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**delegation_signer** | [**DnsSecDelegationSigner**](DnsSecDelegationSigner.md) |  | [optional] 

## Example

```python
from idns.models.dns_sec import DnsSec

# TODO update the JSON string below
json = "{}"
# create an instance of DnsSec from a JSON string
dns_sec_instance = DnsSec.from_json(json)
# print the JSON string representation of the object
print DnsSec.to_json()

# convert the object into a dict
dns_sec_dict = dns_sec_instance.to_dict()
# create an instance of DnsSec from a dict
dns_sec_form_dict = dns_sec.from_dict(dns_sec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


