# DnsSecDelegationSigner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digest_type** | [**DnsSecDelegationSignerDigestType**](DnsSecDelegationSignerDigestType.md) |  | [optional] 
**algorithm_type** | [**DnsSecDelegationSignerDigestType**](DnsSecDelegationSignerDigestType.md) |  | [optional] 
**digest** | **str** |  | [optional] 
**key_tag** | **int** |  | [optional] 

## Example

```python
from idns.models.dns_sec_delegation_signer import DnsSecDelegationSigner

# TODO update the JSON string below
json = "{}"
# create an instance of DnsSecDelegationSigner from a JSON string
dns_sec_delegation_signer_instance = DnsSecDelegationSigner.from_json(json)
# print the JSON string representation of the object
print DnsSecDelegationSigner.to_json()

# convert the object into a dict
dns_sec_delegation_signer_dict = dns_sec_delegation_signer_instance.to_dict()
# create an instance of DnsSecDelegationSigner from a dict
dns_sec_delegation_signer_form_dict = dns_sec_delegation_signer.from_dict(dns_sec_delegation_signer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


