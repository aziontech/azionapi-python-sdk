# S3CredentialCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**capabilities** | **List[str]** |  | [optional] 
**bucket** | **str** |  | [optional] 
**expiration_date** | **datetime** |  | [optional] 

## Example

```python
from storage.models.s3_credential_create import S3CredentialCreate

# TODO update the JSON string below
json = "{}"
# create an instance of S3CredentialCreate from a JSON string
s3_credential_create_instance = S3CredentialCreate.from_json(json)
# print the JSON string representation of the object
print(S3CredentialCreate.to_json())

# convert the object into a dict
s3_credential_create_dict = s3_credential_create_instance.to_dict()
# create an instance of S3CredentialCreate from a dict
s3_credential_create_from_dict = S3CredentialCreate.from_dict(s3_credential_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


