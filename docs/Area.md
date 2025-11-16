# Area


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**armed** | **bool** | Indicates whether MAP panel is armed | [optional] 
**transitional_state** | **str** | An empty JSON string (i.e. “”) indicates that area is not in a transitional state at the moment | [optional] 
**oii_armable** | **bool** | True, if it is possible to disarm/arm the area over the REST-API interface. False, if Areas are configured only to be disarmed/armed blocklocks. False, if Area has relationships to Parent Area Type: Shared Area or Parent Area Type: Pass Thru Area.  | [optional] 
**ready_to_arm** | **bool** | If true, arming of the area is possible. Arming can either be done by a user using MAP system peripherals e.g. Keypad, Smartkey or via the REST-API, if area is “REST-API (OII) Armable”. | [optional] 
**ready_to_disarm** | **bool** | If true, disarming of the area is possible. Disarming can either be done by a user using MAP system peripherals e.g. Keypad, Smartkey or via the REST-API, if area is “REST-API (OII) Armable”. | [optional] 
**number_of_bypassed_devices** | **int** | Number of devices that are bypassed in that area | [optional] 
**walktest** | **str** | If empty, then no walktest is running for this area. Otherwise this field contains the link to the active walktest relative to the server based URL. | [optional] 
**motion_detector_test_active** | **bool** | Indicates whether motion detector test is active | [optional] 
**chime_mode_active** | **bool** | Indicates whether chime mode is active | [optional] 
**incs** | **List[str]** | This field shows the relationship between incidents (alarm/trouble) and an individual area. Details about the incident are contained in the incident resource at its URL. | [optional] 

## Example

```python
from bosch_alarm_map.models.area import Area

# TODO update the JSON string below
json = "{}"
# create an instance of Area from a JSON string
area_instance = Area.from_json(json)
# print the JSON string representation of the object
print(Area.to_json())

# convert the object into a dict
area_dict = area_instance.to_dict()
# create an instance of Area from a dict
area_from_dict = Area.from_dict(area_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


