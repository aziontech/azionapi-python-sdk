# DomainData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**cnames** | **List[str]** |  | [optional] 
**cname_access_only** | **bool** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**edge_application_id** | **int** |  | [optional] 
**digital_certificate_id** | [**DomainDataDigitalCertificateId**](DomainDataDigitalCertificateId.md) |  | [optional] 
**environment** | **str** |  | [optional] 
**is_mtls_enabled** | **bool** |  | [optional] 
**mtls_trusted_ca_certificate_id** | **int** |  | [optional] 
**edge_firewall_id** | **int** |  | [optional] 
**mtls_verification** | **str** |  | [optional] 
**crl_list** | **List[int]** |  | [optional] 

## Example

```python
from domains.models.domain_data import DomainData

# TODO update the JSON string below
json = "{}"
# create an instance of DomainData from a JSON string
domain_data_instance = DomainData.from_json(json)
# print the JSON string representation of the object
print(DomainData.to_json())

# convert the object into a dict
domain_data_dict = domain_data_instance.to_dict()
# create an instance of DomainData from a dict
domain_data_from_dict = DomainData.from_dict(domain_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


