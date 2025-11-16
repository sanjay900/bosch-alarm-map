# Batterycharger


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
from bosch-alarm-map.models.batterycharger import Batterycharger

# TODO update the JSON string below
json = "{}"
# create an instance of Batterycharger from a JSON string
batterycharger_instance = Batterycharger.from_json(json)
# print the JSON string representation of the object
print(Batterycharger.to_json())

# convert the object into a dict
batterycharger_dict = batterycharger_instance.to_dict()
# create an instance of Batterycharger from a dict
batterycharger_from_dict = Batterycharger.from_dict(batterycharger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


