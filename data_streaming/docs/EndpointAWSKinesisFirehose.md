# EndpointAWSKinesisFirehose


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_type** | **str** |  | [optional] 
**access_key** | **str** |  | [optional] 
**stream_name** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**secret_key** | **str** |  | [optional] 

## Example

```python
from data_streaming.models.endpoint_aws_kinesis_firehose import EndpointAWSKinesisFirehose

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointAWSKinesisFirehose from a JSON string
endpoint_aws_kinesis_firehose_instance = EndpointAWSKinesisFirehose.from_json(json)
# print the JSON string representation of the object
print EndpointAWSKinesisFirehose.to_json()

# convert the object into a dict
endpoint_aws_kinesis_firehose_dict = endpoint_aws_kinesis_firehose_instance.to_dict()
# create an instance of EndpointAWSKinesisFirehose from a dict
endpoint_aws_kinesis_firehose_form_dict = endpoint_aws_kinesis_firehose.from_dict(endpoint_aws_kinesis_firehose_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


