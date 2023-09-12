# CustomDataStreamingPostBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**data_source** | **str** | Options:  * &#x60;http&#x60; - Edge Applications (default)  * &#x60;waf&#x60; - WAF Events  * &#x60;cells_console&#x60; - Edge Functions  * &#x60;rtm_activity&#x60; - Activity History    | [optional] 
**template_model** | **str** | Note:  * Add all variables and values that will be used to stream according to the data source you choose to use.    * All data streaming [variables can be found on the reference documentation](https://www.azion.com/en/documentation/products/data-streaming/#selecting-data-sources).    | [optional] 
**active** | **bool** |  | [optional] [default to True]

## Example

```python
from data_streaming.models.custom_data_streaming_post_body import CustomDataStreamingPostBody

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDataStreamingPostBody from a JSON string
custom_data_streaming_post_body_instance = CustomDataStreamingPostBody.from_json(json)
# print the JSON string representation of the object
print CustomDataStreamingPostBody.to_json()

# convert the object into a dict
custom_data_streaming_post_body_dict = custom_data_streaming_post_body_instance.to_dict()
# create an instance of CustomDataStreamingPostBody from a dict
custom_data_streaming_post_body_form_dict = custom_data_streaming_post_body.from_dict(custom_data_streaming_post_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


