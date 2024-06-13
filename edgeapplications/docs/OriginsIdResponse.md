# OriginsIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**OriginsResultResponse**](OriginsResultResponse.md) |  | 
**schema_version** | **int** |  | 

## Example

```python
from edgeapplications.models.origins_id_response import OriginsIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OriginsIdResponse from a JSON string
origins_id_response_instance = OriginsIdResponse.from_json(json)
# print the JSON string representation of the object
print(OriginsIdResponse.to_json())

# convert the object into a dict
origins_id_response_dict = origins_id_response_instance.to_dict()
# create an instance of OriginsIdResponse from a dict
origins_id_response_from_dict = OriginsIdResponse.from_dict(origins_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


