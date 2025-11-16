# PostOutputsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** | This operation initiates turning on/off the device | [optional] 

## Example

```python
from bosch_alarm_map.models.post_outputs_request import PostOutputsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostOutputsRequest from a JSON string
post_outputs_request_instance = PostOutputsRequest.from_json(json)
# print the JSON string representation of the object
print(PostOutputsRequest.to_json())

# convert the object into a dict
post_outputs_request_dict = post_outputs_request_instance.to_dict()
# create an instance of PostOutputsRequest from a dict
post_outputs_request_from_dict = PostOutputsRequest.from_dict(post_outputs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


