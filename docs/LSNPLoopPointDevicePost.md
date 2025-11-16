# LSNPLoopPointDevicePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of a device. | 
**name** | **str** | LSN device internal name. | 
**area** | **str** | LSN device area. | 
**point_type** | **str** | Point device type. | 

## Example

```python
from bosch_alarm_map.models.lsnp_loop_point_device_post import LSNPLoopPointDevicePost

# TODO update the JSON string below
json = "{}"
# create an instance of LSNPLoopPointDevicePost from a JSON string
lsnp_loop_point_device_post_instance = LSNPLoopPointDevicePost.from_json(json)
# print the JSON string representation of the object
print(LSNPLoopPointDevicePost.to_json())

# convert the object into a dict
lsnp_loop_point_device_post_dict = lsnp_loop_point_device_post_instance.to_dict()
# create an instance of LSNPLoopPointDevicePost from a dict
lsnp_loop_point_device_post_from_dict = LSNPLoopPointDevicePost.from_dict(lsnp_loop_point_device_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


