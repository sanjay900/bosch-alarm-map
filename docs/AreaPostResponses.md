# AreaPostResponses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**armed** | **bool** | Indicates whether area is armed | [optional] 
**transitional_state** | **str** | An empty JSON string (i.e. “”) indicates that area is not in a transitional state at the moment | [optional] 
**oii_armable** | **bool** | True, if it is possible to disarm/arm the area over the REST-API interface. False, if Areas are configured only to be disarmed/armed blocklocks. False, if Area has relationships to Parent Area Type: Shared Area or Parent Area Type: Pass Thru Area.  | [optional] 
**ready_to_arm** | **bool** | Indicates whether is area is ready to arm. If the area is already armed, then this flag will be false | [optional] 
**ready_to_disarm** | **bool** | Indicates whether this area can be disarmed. Will be false if the area is already disarmed. | [optional] 
**number_of_bypassed_devices** | **int** | Number of devices that are bypassed in that area | [optional] 
**walktest** | **str** |  | [optional] 
**motion_detector_test_active** | **bool** | Indicates whether motion detector test is active | [optional] 
**chime_mode_active** | **bool** | Indicates whether chime mode is active | [optional] 
**incs** | **List[str]** | This field shows the relationship between incidents (alarm/trouble) and an individual area. Details about the incident are contained in the incident resource at its URL. | [optional] 
**ready_to_force_arm** | **bool** | Indicates whether this area can be armed by bypassing off normal devices. If the area is already armed, this flag will be false. | [optional] 
**why_not_ready_to_arm** | [**ArmingInfoWhyNotReadyToArm**](ArmingInfoWhyNotReadyToArm.md) |  | [optional] 
**why_not_ready_to_force_arm** | [**ArmingInfoWhyNotReadyToForceArm**](ArmingInfoWhyNotReadyToForceArm.md) |  | [optional] 
**why_not_ready_to_disarm** | [**ArmingInfoWhyNotReadyToDisarm**](ArmingInfoWhyNotReadyToDisarm.md) |  | [optional] 

## Example

```python
from bosch-alarm-map.models.area_post_responses import AreaPostResponses

# TODO update the JSON string below
json = "{}"
# create an instance of AreaPostResponses from a JSON string
area_post_responses_instance = AreaPostResponses.from_json(json)
# print the JSON string representation of the object
print(AreaPostResponses.to_json())

# convert the object into a dict
area_post_responses_dict = area_post_responses_instance.to_dict()
# create an instance of AreaPostResponses from a dict
area_post_responses_from_dict = AreaPostResponses.from_dict(area_post_responses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


