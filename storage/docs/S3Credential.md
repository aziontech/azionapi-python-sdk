# S3Credential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**access_key** | **str** |  | [optional] 
**secret_key** | **str** |  | [optional] 
**capabilities** | **List[str]** |  | [optional] 
**bucket** | **str** |  | [optional] 
**expiration_date** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from storage.models.s3_credential import S3Credential

# TODO update the JSON string below
json = "{}"
# create an instance of S3Credential from a JSON string
s3_credential_instance = S3Credential.from_json(json)
# print the JSON string representation of the object
print(S3Credential.to_json())

# convert the object into a dict
s3_credential_dict = s3_credential_instance.to_dict()
# create an instance of S3Credential from a dict
s3_credential_from_dict = S3Credential.from_dict(s3_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


