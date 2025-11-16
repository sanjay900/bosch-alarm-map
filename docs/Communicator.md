# Communicator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**op_state** | [**DeviceOpState**](DeviceOpState.md) |  | [optional] 
**enabled** | **bool** | True if device is currently enabled, otherwise false. | [optional] 
**incs** | **List[str]** | A list of incidents that relate to this device. In case the opState is MALFUNCTION the incident will give more detailed information about the error condition the device is in. | [optional] 

## Example

```python
from bosch-alarm-map.models.communicator import Communicator

# TODO update the JSON string below
json = "{}"
# create an instance of Communicator from a JSON string
communicator_instance = Communicator.from_json(json)
# print the JSON string representation of the object
print(Communicator.to_json())

# convert the object into a dict
communicator_dict = communicator_instance.to_dict()
# create an instance of Communicator from a dict
communicator_from_dict = Communicator.from_dict(communicator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


