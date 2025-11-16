# Keypad


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**op_state** | [**DeviceOpState**](DeviceOpState.md) |  | [optional] 
**enabled** | **bool** | True if device is currently enabled, otherwise false. | [optional] 
**incs** | **List[str]** | A list of incidents that relate to this device. In case the opState is MALFUNCTION the incident will give more detailed information about the error condition the device is in. | [optional] 
**activated** | **bool** | True if device is currently activated, otherwise false. | [optional] 
**user_id** | **str** | The user ID of the user that is currently logged into the Keypad. In case no user is logged in, the Empty string “” will be set. Thus, a client that is subscribed for events for a Keypad will receive a state change event including timestamp when a user logs in or / off. | [optional] 

## Example

```python
from bosch-alarm-map.models.keypad import Keypad

# TODO update the JSON string below
json = "{}"
# create an instance of Keypad from a JSON string
keypad_instance = Keypad.from_json(json)
# print the JSON string representation of the object
print(Keypad.to_json())

# convert the object into a dict
keypad_dict = keypad_instance.to_dict()
# create an instance of Keypad from a dict
keypad_from_dict = Keypad.from_dict(keypad_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


