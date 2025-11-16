# Keyswitch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**op_state** | [**DeviceOpState**](DeviceOpState.md) |  | [optional] 
**incs** | **List[str]** | A list of incidents that relate to this device. In case the opState is MALFUNCTION the incident will give more detailed information about the error condition the device is in. | [optional] 
**enabled** | **bool** | True if device is currently enabled, otherwise false. | [optional] 
**active** | **bool** | True if device is currently activated, otherwise false. | [optional] 

## Example

```python
from bosch_alarm_map.models.keyswitch import Keyswitch

# TODO update the JSON string below
json = "{}"
# create an instance of Keyswitch from a JSON string
keyswitch_instance = Keyswitch.from_json(json)
# print the JSON string representation of the object
print(Keyswitch.to_json())

# convert the object into a dict
keyswitch_dict = keyswitch_instance.to_dict()
# create an instance of Keyswitch from a dict
keyswitch_from_dict = Keyswitch.from_dict(keyswitch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


