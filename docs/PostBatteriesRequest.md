# PostBatteriesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** | This operation initiates bypassing/unbypassing the device.  Bypassing a device will mean that only non-bypassable incidents will be generated from the device. Usually it is used to allow arming of an area even if the device is not normal e.g. an open window.  | [optional] 

## Example

```python
from bosch_alarm_map.models.post_batteries_request import PostBatteriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostBatteriesRequest from a JSON string
post_batteries_request_instance = PostBatteriesRequest.from_json(json)
# print the JSON string representation of the object
print(PostBatteriesRequest.to_json())

# convert the object into a dict
post_batteries_request_dict = post_batteries_request_instance.to_dict()
# create an instance of PostBatteriesRequest from a dict
post_batteries_request_from_dict = PostBatteriesRequest.from_dict(post_batteries_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


