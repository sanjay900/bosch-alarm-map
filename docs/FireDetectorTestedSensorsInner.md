# FireDetectorTestedSensorsInner

When device is in walktest, the array contains objects with the possible types “o”, “t” or “c” and its combinations. The tested field indicates whether the sensor has been tested successfully. The array is only filled while walktest is active. Otherwise it is empty (i.e. [])

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | When device is in walktest, the array contains objects with the possible types “o”, “t” or “c” and its combinations. The array is only filled while walktest is active. Otherwise it is empty (i.e. []) | [optional] 
**tested** | **bool** | The tested field indicates whether the sensor has been tested successfully | [optional] 

## Example

```python
from bosch_alarm_map.models.fire_detector_tested_sensors_inner import FireDetectorTestedSensorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FireDetectorTestedSensorsInner from a JSON string
fire_detector_tested_sensors_inner_instance = FireDetectorTestedSensorsInner.from_json(json)
# print the JSON string representation of the object
print(FireDetectorTestedSensorsInner.to_json())

# convert the object into a dict
fire_detector_tested_sensors_inner_dict = fire_detector_tested_sensors_inner_instance.to_dict()
# create an instance of FireDetectorTestedSensorsInner from a dict
fire_detector_tested_sensors_inner_from_dict = FireDetectorTestedSensorsInner.from_dict(fire_detector_tested_sensors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


