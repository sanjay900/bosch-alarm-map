# ArmingInfoWhyNotReadyToDisarm

Nested objects providing reasons why the area is not ready to disarm

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**related_areas_not_ready_to_disarm** | **List[str]** | List of related areas which are not ready to disarm which make this area not ready to disarm | [optional] 
**related_areas_must_be_disarmed_first** | **List[str]** | List of related areas which need to be disarmed before this area can be disarmed | [optional] 
**virtual_outputs_off_prevents_disarming** | **List[str]** | List of virtual outputs which are off preventing the area from disarming | [optional] 
**active_blocking_time_prevents_disarming** | **bool** | Flag indicates whether a blocking time is active which prevents the area from disarming | [optional] 

## Example

```python
from bosch_alarm_map.models.arming_info_why_not_ready_to_disarm import ArmingInfoWhyNotReadyToDisarm

# TODO update the JSON string below
json = "{}"
# create an instance of ArmingInfoWhyNotReadyToDisarm from a JSON string
arming_info_why_not_ready_to_disarm_instance = ArmingInfoWhyNotReadyToDisarm.from_json(json)
# print the JSON string representation of the object
print(ArmingInfoWhyNotReadyToDisarm.to_json())

# convert the object into a dict
arming_info_why_not_ready_to_disarm_dict = arming_info_why_not_ready_to_disarm_instance.to_dict()
# create an instance of ArmingInfoWhyNotReadyToDisarm from a dict
arming_info_why_not_ready_to_disarm_from_dict = ArmingInfoWhyNotReadyToDisarm.from_dict(arming_info_why_not_ready_to_disarm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


