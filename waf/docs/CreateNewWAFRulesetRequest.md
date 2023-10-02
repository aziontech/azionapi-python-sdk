# CreateNewWAFRulesetRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | Identification name for WAF Rule Set. | 
**mode** | **str** |  | 
**active** | **bool** |  | 
**sql_injection** | **bool** |  | 
**sql_injection_sensitivity** | [**WAFSensitivityChoices**](WAFSensitivityChoices.md) |  | 
**remote_file_inclusion** | **bool** |  | 
**remote_file_inclusion_sensitivity** | [**WAFSensitivityChoices**](WAFSensitivityChoices.md) |  | 
**directory_traversal** | **bool** |  | 
**directory_traversal_sensitivity** | [**WAFSensitivityChoices**](WAFSensitivityChoices.md) |  | 
**cross_site_scripting** | **bool** |  | 
**cross_site_scripting_sensitivity** | [**WAFSensitivityChoices**](WAFSensitivityChoices.md) |  | 
**evading_tricks** | **bool** |  | 
**evading_tricks_sensitivity** | [**WAFSensitivityChoices**](WAFSensitivityChoices.md) |  | 
**file_upload** | **bool** |  | 
**file_upload_sensitivity** | [**WAFSensitivityChoices**](WAFSensitivityChoices.md) |  | 
**unwanted_access** | **bool** |  | 
**unwanted_access_sensitivity** | [**WAFSensitivityChoices**](WAFSensitivityChoices.md) |  | 
**identified_attack** | **bool** |  | 
**identified_attack_sensitivity** | [**WAFSensitivityChoices**](WAFSensitivityChoices.md) |  | 
**bypass_addresses** | **List[str]** |  | 

## Example

```python
from waf.models.create_new_waf_ruleset_request import CreateNewWAFRulesetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNewWAFRulesetRequest from a JSON string
create_new_waf_ruleset_request_instance = CreateNewWAFRulesetRequest.from_json(json)
# print the JSON string representation of the object
print CreateNewWAFRulesetRequest.to_json()

# convert the object into a dict
create_new_waf_ruleset_request_dict = create_new_waf_ruleset_request_instance.to_dict()
# create an instance of CreateNewWAFRulesetRequest from a dict
create_new_waf_ruleset_request_form_dict = create_new_waf_ruleset_request.from_dict(create_new_waf_ruleset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


