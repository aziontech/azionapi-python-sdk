# GetRecordsResponse

Object returned by get zone record

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **int** | The schema version | [optional] 
**count** | **int** | Number of records | [optional] 
**total_pages** | **int** | The total pages | [optional] 
**links** | [**GetZonesResponseLinks**](GetZonesResponseLinks.md) |  | [optional] 
**results** | [**GetRecordsResponseResults**](GetRecordsResponseResults.md) |  | [optional] 

## Example

```python
from idns.models.get_records_response import GetRecordsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRecordsResponse from a JSON string
get_records_response_instance = GetRecordsResponse.from_json(json)
# print the JSON string representation of the object
print GetRecordsResponse.to_json()

# convert the object into a dict
get_records_response_dict = get_records_response_instance.to_dict()
# create an instance of GetRecordsResponse from a dict
get_records_response_form_dict = get_records_response.from_dict(get_records_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


