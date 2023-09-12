# PatchOriginsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**origin_type** | **str** |  | [optional] 
**addresses** | [**List[CreateOriginsRequestAddresses]**](CreateOriginsRequestAddresses.md) |  | [optional] 
**origin_protocol_policy** | **str** |  | [optional] 
**host_header** | **str** |  | [optional] 
**origin_path** | **str** |  | [optional] 
**hmac_authentication** | **bool** |  | [optional] 
**hmac_region_name** | **str** |  | [optional] 
**hmac_access_key** | **str** |  | [optional] 
**hmac_secret_key** | **str** |  | [optional] 

## Example

```python
from edgeapplications.models.patch_origins_request import PatchOriginsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchOriginsRequest from a JSON string
patch_origins_request_instance = PatchOriginsRequest.from_json(json)
# print the JSON string representation of the object
print PatchOriginsRequest.to_json()

# convert the object into a dict
patch_origins_request_dict = patch_origins_request_instance.to_dict()
# create an instance of PatchOriginsRequest from a dict
patch_origins_request_form_dict = patch_origins_request.from_dict(patch_origins_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

