# ArmingInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**armed** | **bool** | Indicates whether area is armed | [optional] 
**ready_to_arm** | **bool** | Indicates whether is area is ready to arm. If the area is already armed, then this flag will be false | [optional] 
**ready_to_force_arm** | **bool** | Indicates whether this area can be armed by bypassing off normal devices. If the area is already armed, this flag will be false. | [optional] 
**ready_to_disarm** | **bool** | Indicates whether this area can be disarmed. Will be false if the area is already disarmed. | [optional] 
**why_not_ready_to_arm** | [**ArmingInfoWhyNotReadyToArm**](ArmingInfoWhyNotReadyToArm.md) |  | [optional] 
**why_not_ready_to_force_arm** | [**ArmingInfoWhyNotReadyToForceArm**](ArmingInfoWhyNotReadyToForceArm.md) |  | [optional] 
**why_not_ready_to_disarm** | [**ArmingInfoWhyNotReadyToDisarm**](ArmingInfoWhyNotReadyToDisarm.md) |  | [optional] 

## Example

```python
from bosch-alarm-map.models.arming_info import ArmingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArmingInfo from a JSON string
arming_info_instance = ArmingInfo.from_json(json)
# print the JSON string representation of the object
print(ArmingInfo.to_json())

# convert the object into a dict
arming_info_dict = arming_info_instance.to_dict()
# create an instance of ArmingInfo from a dict
arming_info_from_dict = ArmingInfo.from_dict(arming_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


