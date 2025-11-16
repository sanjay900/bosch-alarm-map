# AreaArm

This command is used to arm an area.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** | Indicates arming activity to be started | [optional] 
**bypass_off_normal_devices** | **bool** | Bypass all devices that are off normal before arming. | [optional] 
**exit_delay** | **str** | Defines whether the arming should happen without a delay (zero) with the user configured default exit delay or with the extended exit delay as configured for the area. | [optional] 

## Example

```python
from openapi_client.models.area_arm import AreaArm

# TODO update the JSON string below
json = "{}"
# create an instance of AreaArm from a JSON string
area_arm_instance = AreaArm.from_json(json)
# print the JSON string representation of the object
print(AreaArm.to_json())

# convert the object into a dict
area_arm_dict = area_arm_instance.to_dict()
# create an instance of AreaArm from a dict
area_arm_from_dict = AreaArm.from_dict(area_arm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


