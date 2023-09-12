# PostCustomDataStreamingResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**data_source** | **str** | Options:  * &#x60;http&#x60; - Edge Applications  * &#x60;waf&#x60; - WAF Events  * &#x60;cells_console&#x60; - Edge Functions  * &#x60;rtm_activity&#x60; - Activity History    | [optional] 
**template_model** | **str** | Note:  * Add all variables and values that will be used to stream according to the data source you choose to use.    | [optional] 
**active** | **bool** |  | [optional] 
**endpoint** | **str** |  | [optional] 
**all_domains** | **bool** | Note:  * Field not used with the rtm_activity data source.  | [optional] 

## Example

```python
from data_streaming.models.post_custom_data_streaming_response import PostCustomDataStreamingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostCustomDataStreamingResponse from a JSON string
post_custom_data_streaming_response_instance = PostCustomDataStreamingResponse.from_json(json)
# print the JSON string representation of the object
print PostCustomDataStreamingResponse.to_json()

# convert the object into a dict
post_custom_data_streaming_response_dict = post_custom_data_streaming_response_instance.to_dict()
# create an instance of PostCustomDataStreamingResponse from a dict
post_custom_data_streaming_response_form_dict = post_custom_data_streaming_response.from_dict(post_custom_data_streaming_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


