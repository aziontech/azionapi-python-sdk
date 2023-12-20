# OriginsResultResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origin_id** | **int** |  | [optional] 
**origin_key** | **str** |  | [optional] 
**name** | **str** |  | 
**origin_type** | **str** |  | [optional] 
**addresses** | [**List[OriginsResultResponseAddresses]**](OriginsResultResponseAddresses.md) |  | [optional] 
**origin_protocol_policy** | **str** |  | [optional] 
**is_origin_redirection_enabled** | **bool** |  | [optional] 
**host_header** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**origin_path** | **str** |  | [optional] 
**connection_timeout** | **int** |  | [optional] 
**timeout_between_bytes** | **int** |  | [optional] 
**hmac_authentication** | **bool** |  | [optional] 
**hmac_region_name** | **str** |  | [optional] 
**hmac_access_key** | **str** |  | [optional] 
**hmac_secret_key** | **str** |  | [optional] 
**bucket** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 

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


