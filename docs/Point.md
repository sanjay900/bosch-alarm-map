# Point


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**op_state** | [**DeviceOpState**](DeviceOpState.md) |  | [optional] 
**enabled** | **bool** | True if device is currently enabled, otherwise false. | [optional] 
**walktest** | [**DeviceWalktest**](DeviceWalktest.md) |  | [optional] 
**incs** | **List[str]** | A list of incidents that relate to this device. In case the opState is MALFUNCTION the incident will give more detailed information about the error condition the device is in. | [optional] 
**active** | **bool** | True if point is active | [optional] 

## Example

```python
from bosch_alarm_map.models.point import Point

# TODO update the JSON string below
json = "{}"
# create an instance of Point from a JSON string
point_instance = Point.from_json(json)
# print the JSON string representation of the object
print(Point.to_json())

# convert the object into a dict
point_dict = point_instance.to_dict()
# create an instance of Point from a dict
point_from_dict = Point.from_dict(point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


