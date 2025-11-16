# Smartkey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**op_state** | [**DeviceOpState**](DeviceOpState.md) |  | [optional] 
**enabled** | **bool** | True if device is currently enabled, otherwise false. | [optional] 
**bypassed** | **bool** | True if device is currently bypassed, otherwise false | [optional] 
**incs** | **List[str]** | A list of incidents that relate to this device. In case the opState is MALFUNCTION the incident will give more detailed information about the error condition the device is in. | [optional] 
**locked** | **bool** | True if arming device is locked (resulting in the door being locked) | [optional] 
**usable** | **bool** | True if the arming device can be used to arm/disarm the area | [optional] 
**update** | [**DeviceUpdate**](DeviceUpdate.md) |  | [optional] 

## Example

```python
from bosch_alarm_map.models.smartkey import Smartkey

# TODO update the JSON string below
json = "{}"
# create an instance of Smartkey from a JSON string
smartkey_instance = Smartkey.from_json(json)
# print the JSON string representation of the object
print(Smartkey.to_json())

# convert the object into a dict
smartkey_dict = smartkey_instance.to_dict()
# create an instance of Smartkey from a dict
smartkey_from_dict = Smartkey.from_dict(smartkey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


