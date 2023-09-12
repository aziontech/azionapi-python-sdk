# UpdateOriginsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**origin_type** | **str** |  | [optional] 
**addresses** | [**List[CreateOriginsRequestAddresses]**](CreateOriginsRequestAddresses.md) |  | 
**origin_protocol_policy** | **str** |  | [optional] 
**host_header** | **str** |  | 
**origin_path** | **str** |  | [optional] 
**hmac_authentication** | **bool** |  | [optional] 
**hmac_region_name** | **str** |  | [optional] 
**hmac_access_key** | **str** |  | [optional] 
**hmac_secret_key** | **str** |  | [optional] 

## Example

```python
from edgeapplications.models.update_origins_request import UpdateOriginsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOriginsRequest from a JSON string
update_origins_request_instance = UpdateOriginsRequest.from_json(json)
# print the JSON string representation of the object
print UpdateOriginsRequest.to_json()

# convert the object into a dict
update_origins_request_dict = update_origins_request_instance.to_dict()
# create an instance of UpdateOriginsRequest from a dict
update_origins_request_form_dict = update_origins_request.from_dict(update_origins_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


