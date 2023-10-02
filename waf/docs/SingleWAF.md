# SingleWAF


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | Identification name for WAF Rule Set. | [optional] 
**mode** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**sql_injection** | **bool** |  | [optional] 
**sql_injection_sensitivity** | [**WAFSensitivityChoices**](WAFSensitivityChoices.md) |  | [optional] 
**remote_file_inclusion** | **bool** |  | [optional] 
**remote_file_inclusion_sensitivity** | [**WAFSensitivityChoices**](WAFSensitivityChoices.md) |  | [optional] 
**directory_traversal** | **bool** |  | [optional] 
**directory_traversal_sensitivity** | [**WAFSensitivityChoices**](WAFSensitivityChoices.md) |  | [optional] 
**cross_site_scripting** | **bool** |  | [optional] 
**cross_site_scripting_sensitivity** | [**WAFSensitivityChoices**](WAFSensitivityChoices.md) |  | [optional] 
**evading_tricks** | **bool** |  | [optional] 
**evading_tricks_sensitivity** | [**WAFSensitivityChoices**](WAFSensitivityChoices.md) |  | [optional] 
**file_upload** | **bool** |  | [optional] 
**file_upload_sensitivity** | [**WAFSensitivityChoices**](WAFSensitivityChoices.md) |  | [optional] 
**unwanted_access** | **bool** |  | [optional] 
**unwanted_access_sensitivity** | [**WAFSensitivityChoices**](WAFSensitivityChoices.md) |  | [optional] 
**identified_attack** | **bool** |  | [optional] 
**identified_attack_sensitivity** | [**WAFSensitivityChoices**](WAFSensitivityChoices.md) |  | [optional] 
**bypass_addresses** | **List[str]** |  | [optional] 

## Example

```python
from waf.models.single_waf import SingleWAF

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWAF from a JSON string
single_waf_instance = SingleWAF.from_json(json)
# print the JSON string representation of the object
print SingleWAF.to_json()

# convert the object into a dict
single_waf_dict = single_waf_instance.to_dict()
# create an instance of SingleWAF from a dict
single_waf_form_dict = single_waf.from_dict(single_waf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


