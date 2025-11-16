# LSNLoopDevicePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of a device. | 
**name** | **str** | LSN device internal name. | 
**area** | **str** | LSN device area. | 

## Example

```python
from openapi_client.models.lsn_loop_device_post import LSNLoopDevicePost

# TODO update the JSON string below
json = "{}"
# create an instance of LSNLoopDevicePost from a JSON string
lsn_loop_device_post_instance = LSNLoopDevicePost.from_json(json)
# print the JSON string representation of the object
print(LSNLoopDevicePost.to_json())

# convert the object into a dict
lsn_loop_device_post_dict = lsn_loop_device_post_instance.to_dict()
# create an instance of LSNLoopDevicePost from a dict
lsn_loop_device_post_from_dict = LSNLoopDevicePost.from_dict(lsn_loop_device_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


