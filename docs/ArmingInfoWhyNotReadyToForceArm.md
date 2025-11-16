# ArmingInfoWhyNotReadyToForceArm

Nested objects providing reasons why the area cannot be armed by bypassing off normal devices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**non_bypassable_faulted_devices** | **List[str]** | List of off normal devices that cannot be bypassed | [optional] 
**too_many_faulted_devices** | **List[str]** | List of all off normal devices, the count of which exceeds the number of devices that can be bypassed to arm the area | [optional] 
**too_many_bypassed_devices** | **bool** | Indicates that the area cannot be force armed because there are too many bypassed devices | [optional] 
**devices_bypassed_too_many_times** | **List[str]** | List of all off normal devices which have been bypassed multiple times exceeded the number of times a device can be bypassed | [optional] 
**system_wide_devices_faulted** | **List[str]** | List of all off normal devices which are considered as system wide devices | [optional] 
**related_areas_not_ready_to_arm** | **List[str]** | List of related areas which are not ready to arm which make this area not ready to arm | [optional] 
**related_areas_must_be_armed_first** | **List[str]** | List of related areas which need to be armed first before this area can be armed | [optional] 
**pending_incidents_in_area** | **bool** | Flag indicates whether there is an unhandled incident in the area | [optional] 
**area_in_walktest** | **bool** | Flag indicates whether the area is in walktest | [optional] 

## Example

```python
from openapi_client.models.arming_info_why_not_ready_to_force_arm import ArmingInfoWhyNotReadyToForceArm

# TODO update the JSON string below
json = "{}"
# create an instance of ArmingInfoWhyNotReadyToForceArm from a JSON string
arming_info_why_not_ready_to_force_arm_instance = ArmingInfoWhyNotReadyToForceArm.from_json(json)
# print the JSON string representation of the object
print(ArmingInfoWhyNotReadyToForceArm.to_json())

# convert the object into a dict
arming_info_why_not_ready_to_force_arm_dict = arming_info_why_not_ready_to_force_arm_instance.to_dict()
# create an instance of ArmingInfoWhyNotReadyToForceArm from a dict
arming_info_why_not_ready_to_force_arm_from_dict = ArmingInfoWhyNotReadyToForceArm.from_dict(arming_info_why_not_ready_to_force_arm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


