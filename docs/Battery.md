# Battery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**op_state** | [**DeviceOpState**](DeviceOpState.md) |  | [optional] 
**enabled** | **bool** | True if device is currently enabled, otherwise false. | [optional] 
**bypassed** | **bool** | True if device is currently bypassed, otherwise false | [optional] 
**incs** | **List[str]** | A list of incidents that relate to this device. In case the opState is MALFUNCTION the incident will give more detailed information about the error condition the device is in. | [optional] 

## Example

```python
from bosch_alarm_map.models.battery import Battery

# TODO update the JSON string below
json = "{}"
# create an instance of Battery from a JSON string
battery_instance = Battery.from_json(json)
# print the JSON string representation of the object
print(Battery.to_json())

# convert the object into a dict
battery_dict = battery_instance.to_dict()
# create an instance of Battery from a dict
battery_from_dict = Battery.from_dict(battery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


