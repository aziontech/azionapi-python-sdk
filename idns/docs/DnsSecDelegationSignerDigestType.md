# DnsSecDelegationSignerDigestType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**slug** | **str** |  | [optional] 

## Example

```python
from idns.models.dns_sec_delegation_signer_digest_type import DnsSecDelegationSignerDigestType

# TODO update the JSON string below
json = "{}"
# create an instance of DnsSecDelegationSignerDigestType from a JSON string
dns_sec_delegation_signer_digest_type_instance = DnsSecDelegationSignerDigestType.from_json(json)
# print the JSON string representation of the object
print DnsSecDelegationSignerDigestType.to_json()

# convert the object into a dict
dns_sec_delegation_signer_digest_type_dict = dns_sec_delegation_signer_digest_type_instance.to_dict()
# create an instance of DnsSecDelegationSignerDigestType from a dict
dns_sec_delegation_signer_digest_type_form_dict = dns_sec_delegation_signer_digest_type.from_dict(dns_sec_delegation_signer_digest_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


