# ApplicationOrigins


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**origin_type** | **str** |  | [optional] 
**origin_id** | **str** |  | [optional] 

## Example

```python
from edgeapplications.models.application_origins import ApplicationOrigins

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationOrigins from a JSON string
application_origins_instance = ApplicationOrigins.from_json(json)
# print the JSON string representation of the object
print(ApplicationOrigins.to_json())

# convert the object into a dict
application_origins_dict = application_origins_instance.to_dict()
# create an instance of ApplicationOrigins from a dict
application_origins_from_dict = ApplicationOrigins.from_dict(application_origins_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


