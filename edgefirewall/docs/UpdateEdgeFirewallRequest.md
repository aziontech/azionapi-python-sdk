# UpdateEdgeFirewallRequest


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
from edgefirewall.models.update_edge_firewall_request import UpdateEdgeFirewallRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEdgeFirewallRequest from a JSON string
update_edge_firewall_request_instance = UpdateEdgeFirewallRequest.from_json(json)
# print the JSON string representation of the object
print UpdateEdgeFirewallRequest.to_json()

# convert the object into a dict
update_edge_firewall_request_dict = update_edge_firewall_request_instance.to_dict()
# create an instance of UpdateEdgeFirewallRequest from a dict
update_edge_firewall_request_form_dict = update_edge_firewall_request.from_dict(update_edge_firewall_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


