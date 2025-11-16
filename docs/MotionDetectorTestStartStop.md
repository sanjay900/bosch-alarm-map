# MotionDetectorTestStartStop

This operation starts/stops a motion detector test in the area.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** |  | [optional] 

## Example

```python
from bosch_alarm_map.models.motion_detector_test_start_stop import MotionDetectorTestStartStop

# TODO update the JSON string below
json = "{}"
# create an instance of MotionDetectorTestStartStop from a JSON string
motion_detector_test_start_stop_instance = MotionDetectorTestStartStop.from_json(json)
# print the JSON string representation of the object
print(MotionDetectorTestStartStop.to_json())

# convert the object into a dict
motion_detector_test_start_stop_dict = motion_detector_test_start_stop_instance.to_dict()
# create an instance of MotionDetectorTestStartStop from a dict
motion_detector_test_start_stop_from_dict = MotionDetectorTestStartStop.from_dict(motion_detector_test_start_stop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


