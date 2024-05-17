# PutDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**cnames** | **List[str]** |  | 
**cname_access_only** | **bool** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**edge_application_id** | **int** |  | 
**digital_certificate_id** | **str** |  | [optional] 
**environment** | **str** |  | [optional] 
**is_mtls_enabled** | **bool** |  | [optional] 
**mtls_trusted_ca_certificate_id** | **int** |  | [optional] 
**edge_firewall_id** | **int** |  | [optional] 
**mtls_verification** | **str** |  | [optional] 
**crl_list** | **List[int]** |  | [optional] 

## Example

```python
from domains.models.put_domain_request import PutDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutDomainRequest from a JSON string
put_domain_request_instance = PutDomainRequest.from_json(json)
# print the JSON string representation of the object
print(PutDomainRequest.to_json())

# convert the object into a dict
put_domain_request_dict = put_domain_request_instance.to_dict()
# create an instance of PutDomainRequest from a dict
put_domain_request_from_dict = PutDomainRequest.from_dict(put_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


