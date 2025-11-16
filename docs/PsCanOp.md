# PsCanOp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**op_state** | [**DeviceOpState**](DeviceOpState.md) |  | [optional] 
**incs** | **List[str]** | A list of incidents that relate to this device. In case the opState is MALFUNCTION the incident will give more detailed information about the error condition the device is in. | [optional] 

## Example

```python
from bosch_alarm_map.models.ps_can_op import PsCanOp

# TODO update the JSON string below
json = "{}"
# create an instance of PsCanOp from a JSON string
ps_can_op_instance = PsCanOp.from_json(json)
# print the JSON string representation of the object
print(PsCanOp.to_json())

# convert the object into a dict
ps_can_op_dict = ps_can_op_instance.to_dict()
# create an instance of PsCanOp from a dict
ps_can_op_from_dict = PsCanOp.from_dict(ps_can_op_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


