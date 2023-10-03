# CreateEdgeFirewallRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**domains** | **List[int]** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**edge_functions_enabled** | **bool** |  | [optional] 
**network_protection_enabled** | **bool** |  | [optional] 
**waf_enabled** | **bool** |  | [optional] 

## Example

```python
from edgefirewall.models.create_edge_firewall_request import CreateEdgeFirewallRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEdgeFirewallRequest from a JSON string
create_edge_firewall_request_instance = CreateEdgeFirewallRequest.from_json(json)
# print the JSON string representation of the object
print CreateEdgeFirewallRequest.to_json()

# convert the object into a dict
create_edge_firewall_request_dict = create_edge_firewall_request_instance.to_dict()
# create an instance of CreateEdgeFirewallRequest from a dict
create_edge_firewall_request_form_dict = create_edge_firewall_request.from_dict(create_edge_firewall_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


