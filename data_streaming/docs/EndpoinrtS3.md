# EndpoinrtS3


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_type** | **str** |  | [optional] 
**access_key** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**object_key_prefix** | **str** |  | [optional] 
**bucket_name** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**host_url** | **str** |  | [optional] 
**secret_key** | **str** |  | [optional] 

## Example

```python
from data_streaming.models.endpoinrt_s3 import EndpoinrtS3

# TODO update the JSON string below
json = "{}"
# create an instance of EndpoinrtS3 from a JSON string
endpoinrt_s3_instance = EndpoinrtS3.from_json(json)
# print the JSON string representation of the object
print EndpoinrtS3.to_json()

# convert the object into a dict
endpoinrt_s3_dict = endpoinrt_s3_instance.to_dict()
# create an instance of EndpoinrtS3 from a dict
endpoinrt_s3_form_dict = endpoinrt_s3.from_dict(endpoinrt_s3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


