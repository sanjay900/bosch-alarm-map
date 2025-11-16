# ChimeModeStartStop

This operation starts/stops chime mode in an area.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** |  | [optional] 

## Example

```python
from bosch_alarm_map.models.chime_mode_start_stop import ChimeModeStartStop

# TODO update the JSON string below
json = "{}"
# create an instance of ChimeModeStartStop from a JSON string
chime_mode_start_stop_instance = ChimeModeStartStop.from_json(json)
# print the JSON string representation of the object
print(ChimeModeStartStop.to_json())

# convert the object into a dict
chime_mode_start_stop_dict = chime_mode_start_stop_instance.to_dict()
# create an instance of ChimeModeStartStop from a dict
chime_mode_start_stop_from_dict = ChimeModeStartStop.from_dict(chime_mode_start_stop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


