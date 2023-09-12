# OriginsResultResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origin_id** | **int** |  | 
**origin_key** | **str** |  | 
**name** | **str** |  | 
**origin_type** | **str** |  | 
**addresses** | [**List[OriginsResultResponseAddresses]**](OriginsResultResponseAddresses.md) |  | 
**origin_protocol_policy** | **str** |  | 
**is_origin_redirection_enabled** | **bool** |  | 
**host_header** | **str** |  | 
**method** | **str** |  | 
**origin_path** | **str** |  | 
**connection_timeout** | **int** |  | 
**timeout_between_bytes** | **int** |  | 
**hmac_authentication** | **bool** |  | 
**hmac_region_name** | **str** |  | 
**hmac_access_key** | **str** |  | 
**hmac_secret_key** | **str** |  | 

## Example

```python
from edgeapplications.models.origins_result_response import OriginsResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OriginsResultResponse from a JSON string
origins_result_response_instance = OriginsResultResponse.from_json(json)
# print the JSON string representation of the object
print OriginsResultResponse.to_json()

# convert the object into a dict
origins_result_response_dict = origins_result_response_instance.to_dict()
# create an instance of OriginsResultResponse from a dict
origins_result_response_form_dict = origins_result_response.from_dict(origins_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


