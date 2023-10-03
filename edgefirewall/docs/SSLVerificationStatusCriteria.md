# SSLVerificationStatusCriteria


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variable** | [**Variables**](Variables.md) |  | [optional] 
**operator** | [**SSLVerificationStatusOperators**](SSLVerificationStatusOperators.md) |  | [optional] 
**conditional** | [**Conditionals**](Conditionals.md) |  | [optional] 
**input_value** | [**SSLVerificationStatusArguments**](SSLVerificationStatusArguments.md) |  | [optional] 

## Example

```python
from edgefirewall.models.ssl_verification_status_criteria import SSLVerificationStatusCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of SSLVerificationStatusCriteria from a JSON string
ssl_verification_status_criteria_instance = SSLVerificationStatusCriteria.from_json(json)
# print the JSON string representation of the object
print SSLVerificationStatusCriteria.to_json()

# convert the object into a dict
ssl_verification_status_criteria_dict = ssl_verification_status_criteria_instance.to_dict()
# create an instance of SSLVerificationStatusCriteria from a dict
ssl_verification_status_criteria_form_dict = ssl_verification_status_criteria.from_dict(ssl_verification_status_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


