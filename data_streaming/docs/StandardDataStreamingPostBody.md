# StandardDataStreamingPostBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**template_id** | **int** | Options:  * &#x60;2&#x60; - Edge Applications Event Collector  * &#x60;4&#x60; - WAF Event Collector  * &#x60;86&#x60; - Edge Functions Event Collector  * &#x60;184&#x60; - Edge Applications + WAF Event Collector  * &#x60;251&#x60; - Activity History Collector  | [optional] 
**data_source** | **str** | Options:  * &#x60;http&#x60; - Edge Applications (default)  * &#x60;waf&#x60; - WAF Events  * &#x60;cells_console&#x60; - Edge Functions  * &#x60;rtm_activity&#x60; - Activity History  | [optional] 
**active** | **bool** |  | [optional] [default to True]
**endpoint** | [**DataStreamingEndpointTypeStandard**](DataStreamingEndpointTypeStandard.md) |  | [optional] 
**domains_ids** | **List[int]** | Note:  * Field not used with the rtm_activity data source.  | [optional] 
**all_domains** | **bool** | Note:  * Field not used with the rtm_activity data source.  | [optional] [default to False]

## Example

```python
from data_streaming.models.standard_data_streaming_post_body import StandardDataStreamingPostBody

# TODO update the JSON string below
json = "{}"
# create an instance of StandardDataStreamingPostBody from a JSON string
standard_data_streaming_post_body_instance = StandardDataStreamingPostBody.from_json(json)
# print the JSON string representation of the object
print StandardDataStreamingPostBody.to_json()

# convert the object into a dict
standard_data_streaming_post_body_dict = standard_data_streaming_post_body_instance.to_dict()
# create an instance of StandardDataStreamingPostBody from a dict
standard_data_streaming_post_body_form_dict = standard_data_streaming_post_body.from_dict(standard_data_streaming_post_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


