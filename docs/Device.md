# Device


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**op_state** | [**DeviceOpState**](DeviceOpState.md) |  | [optional] 
**incs** | **List[str]** | A list of incidents that relate to this device. In case the opState is MALFUNCTION the incident will give more detailed information about the error condition the device is in. | [optional] 
**enabled** | **bool** | True if device is currently enabled, otherwise false. | [optional] 
**active** | **bool** | True if device is currently activated, otherwise false. | [optional] 
**on** | **bool** | True if output is on | [optional] 
**walktest** | [**DeviceWalktest**](DeviceWalktest.md) |  | [optional] 
**bypassed** | **bool** | True if device is currently bypassed, otherwise false | [optional] 
**activated** | **bool** | True if device is currently activated, otherwise false. | [optional] 
**user_id** | **str** | The user ID of the user that is currently logged into the Keypad. In case no user is logged in, the Empty string “” will be set. Thus, a client that is subscribed for events for a Keypad will receive a state change event including timestamp when a user logs in or off.   | [optional] 
**locked** | **bool** | True if arming device is locked (resulting in the door being locked) | [optional] 
**update** | [**DeviceUpdate**](DeviceUpdate.md) |  | [optional] 
**usable** | **bool** | True if the arming device can be used to arm/disarm the area | [optional] 

## Example

```python
from bosch-alarm-map.models.device import Device

# TODO update the JSON string below
json = "{}"
# create an instance of Device from a JSON string
device_instance = Device.from_json(json)
# print the JSON string representation of the object
print(Device.to_json())

# convert the object into a dict
device_dict = device_instance.to_dict()
# create an instance of Device from a dict
device_from_dict = Device.from_dict(device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


