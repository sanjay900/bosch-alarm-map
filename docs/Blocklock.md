# Blocklock


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

## Example

```python
from openapi_client.models.blocklock import Blocklock

# TODO update the JSON string below
json = "{}"
# create an instance of Blocklock from a JSON string
blocklock_instance = Blocklock.from_json(json)
# print the JSON string representation of the object
print(Blocklock.to_json())

# convert the object into a dict
blocklock_dict = blocklock_instance.to_dict()
# create an instance of Blocklock from a dict
blocklock_from_dict = Blocklock.from_dict(blocklock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


