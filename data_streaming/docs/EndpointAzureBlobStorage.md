# EndpointAzureBlobStorage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_type** | **str** |  | [optional] 
**storage_account** | **str** |  | [optional] 
**container_name** | **str** |  | [optional] 
**blob_sas_token** | **str** |  | [optional] 

## Example

```python
from data_streaming.models.endpoint_azure_blob_storage import EndpointAzureBlobStorage

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAzureBlobStorage from a JSON string
endpoint_azure_blob_storage_instance = EndpointAzureBlobStorage.from_json(json)
# print the JSON string representation of the object
print EndpointAzureBlobStorage.to_json()

# convert the object into a dict
endpoint_azure_blob_storage_dict = endpoint_azure_blob_storage_instance.to_dict()
# create an instance of EndpointAzureBlobStorage from a dict
endpoint_azure_blob_storage_form_dict = endpoint_azure_blob_storage.from_dict(endpoint_azure_blob_storage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


