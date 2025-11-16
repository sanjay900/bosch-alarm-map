# Output


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**op_state** | [**DeviceOpState**](DeviceOpState.md) |  | [optional] 
**enabled** | **bool** | True if device is currently enabled, otherwise false. | [optional] 
**incs** | **List[str]** | A list of incidents that relate to this device. In case the opState is MALFUNCTION the incident will give more detailed information about the error condition the device is in. | [optional] 
**on** | **bool** | True if output is on | [optional] 

## Example

```python
from bosch-alarm-map.models.output import Output

# TODO update the JSON string below
json = "{}"
# create an instance of Output from a JSON string
output_instance = Output.from_json(json)
# print the JSON string representation of the object
print(Output.to_json())

# convert the object into a dict
output_dict = output_instance.to_dict()
# create an instance of Output from a dict
output_from_dict = Output.from_dict(output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


