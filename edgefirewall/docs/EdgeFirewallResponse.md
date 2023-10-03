# EdgeFirewallResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**EdgeFirewall**](EdgeFirewall.md) |  | [optional] 
**schema_version** | **float** |  | [optional] 

## Example

```python
from edgefirewall.models.edge_firewall_response import EdgeFirewallResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeFirewallResponse from a JSON string
edge_firewall_response_instance = EdgeFirewallResponse.from_json(json)
# print the JSON string representation of the object
print EdgeFirewallResponse.to_json()

# convert the object into a dict
edge_firewall_response_dict = edge_firewall_response_instance.to_dict()
# create an instance of EdgeFirewallResponse from a dict
edge_firewall_response_form_dict = edge_firewall_response.from_dict(edge_firewall_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


