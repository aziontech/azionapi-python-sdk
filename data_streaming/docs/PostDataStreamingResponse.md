# PostDataStreamingResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**template_id** | **int** | Options:  * &#x60;2&#x60; - Edge Applications Event Collector  * &#x60;4&#x60; - WAF Event Collector  * &#x60;86&#x60; - Edge Functions Event Collector  * &#x60;184&#x60; - Edge Applications + WAF Event Collector  * &#x60;251&#x60; - Activity History Collector  | [optional] 
**data_source** | **str** | Options:  * &#x60;http&#x60; - Edge Applications  * &#x60;waf&#x60; - WAF Events  * &#x60;cells_console&#x60; - Edge Functions  * &#x60;rtm_activity&#x60; - Activity History  | [optional] 
**active** | **bool** |  | [optional] 
**endpoint** | [**List[PostDataStreamingResponseEndpointInner]**](PostDataStreamingResponseEndpointInner.md) |  | [optional] 
**all_domains** | **bool** | Note:  * Field not used with the rtm_activity data source.  | [optional] 

## Example

```python
from data_streaming.models.post_data_streaming_response import PostDataStreamingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostDataStreamingResponse from a JSON string
post_data_streaming_response_instance = PostDataStreamingResponse.from_json(json)
# print the JSON string representation of the object
print PostDataStreamingResponse.to_json()

# convert the object into a dict
post_data_streaming_response_dict = post_data_streaming_response_instance.to_dict()
# create an instance of PostDataStreamingResponse from a dict
post_data_streaming_response_form_dict = post_data_streaming_response.from_dict(post_data_streaming_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


