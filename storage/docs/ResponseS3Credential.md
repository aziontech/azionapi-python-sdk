# ResponseS3Credential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | [optional] 
**data** | [**S3Credential**](S3Credential.md) |  | [optional] 

## Example

```python
from storage.models.response_s3_credential import ResponseS3Credential

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseS3Credential from a JSON string
response_s3_credential_instance = ResponseS3Credential.from_json(json)
# print the JSON string representation of the object
print(ResponseS3Credential.to_json())

# convert the object into a dict
response_s3_credential_dict = response_s3_credential_instance.to_dict()
# create an instance of ResponseS3Credential from a dict
response_s3_credential_from_dict = ResponseS3Credential.from_dict(response_s3_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


