# CreateOriginsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**origin_type** | **str** |  | [optional] 
**addresses** | [**List[CreateOriginsRequestAddresses]**](CreateOriginsRequestAddresses.md) |  | [optional] 
**origin_protocol_policy** | **str** |  | [optional] 
**host_header** | **str** |  | [optional] 
**origin_path** | **str** |  | [optional] 
**hmac_authentication** | **bool** |  | [optional] 
**hmac_region_name** | **str** |  | [optional] 
**hmac_access_key** | **str** |  | [optional] 
**hmac_secret_key** | **str** |  | [optional] 
**bucket** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 

## Example

```python
from edgeapplications.models.create_origins_request import CreateOriginsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOriginsRequest from a JSON string
create_origins_request_instance = CreateOriginsRequest.from_json(json)
# print the JSON string representation of the object
print CreateOriginsRequest.to_json()

# convert the object into a dict
create_origins_request_dict = create_origins_request_instance.to_dict()
# create an instance of CreateOriginsRequest from a dict
create_origins_request_form_dict = create_origins_request.from_dict(create_origins_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


