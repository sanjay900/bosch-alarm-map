# ArmingInfoWhyNotReadyToArm

Nested objects providing reasons why the area is not ready to arm

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bypassable_faulted_devices** | **List[str]** | List of off normal devices that can be bypassed while arming | [optional] 

## Example

```python
from bosch-alarm-map.models.arming_info_why_not_ready_to_arm import ArmingInfoWhyNotReadyToArm

# TODO update the JSON string below
json = "{}"
# create an instance of ArmingInfoWhyNotReadyToArm from a JSON string
arming_info_why_not_ready_to_arm_instance = ArmingInfoWhyNotReadyToArm.from_json(json)
# print the JSON string representation of the object
print(ArmingInfoWhyNotReadyToArm.to_json())

# convert the object into a dict
arming_info_why_not_ready_to_arm_dict = arming_info_why_not_ready_to_arm_instance.to_dict()
# create an instance of ArmingInfoWhyNotReadyToArm from a dict
arming_info_why_not_ready_to_arm_from_dict = ArmingInfoWhyNotReadyToArm.from_dict(arming_info_why_not_ready_to_arm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


