# FireDetector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**op_state** | [**DeviceOpState**](DeviceOpState.md) |  | [optional] 
**enabled** | **bool** | True if device is currently enabled, otherwise false. | [optional] 
**incs** | **List[str]** | A list of incidents that relate to this device. In case the opState is MALFUNCTION the incident will give more detailed information about the error condition the device is in. | [optional] 
**tested_sensors** | [**List[FireDetectorTestedSensorsInner]**](FireDetectorTestedSensorsInner.md) | Array that contains one object for each sensor of this particular device. | [optional] 

## Example

```python
from bosch-alarm-map.models.fire_detector import FireDetector

# TODO update the JSON string below
json = "{}"
# create an instance of FireDetector from a JSON string
fire_detector_instance = FireDetector.from_json(json)
# print the JSON string representation of the object
print(FireDetector.to_json())

# convert the object into a dict
fire_detector_dict = fire_detector_instance.to_dict()
# create an instance of FireDetector from a dict
fire_detector_from_dict = FireDetector.from_dict(fire_detector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


