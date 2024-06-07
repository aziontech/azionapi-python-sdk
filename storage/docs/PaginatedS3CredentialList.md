# PaginatedS3CredentialList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[S3Credential]**](S3Credential.md) |  | [optional] 

## Example

```python
from storage.models.paginated_s3_credential_list import PaginatedS3CredentialList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedS3CredentialList from a JSON string
paginated_s3_credential_list_instance = PaginatedS3CredentialList.from_json(json)
# print the JSON string representation of the object
print(PaginatedS3CredentialList.to_json())

# convert the object into a dict
paginated_s3_credential_list_dict = paginated_s3_credential_list_instance.to_dict()
# create an instance of PaginatedS3CredentialList from a dict
paginated_s3_credential_list_from_dict = PaginatedS3CredentialList.from_dict(paginated_s3_credential_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


