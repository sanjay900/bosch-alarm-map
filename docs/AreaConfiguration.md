# AreaConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name used to identify the area. | [optional] 
**siid** | **str** | Auto generated unique Identifier. A, B, C and D are integer values. String would be “ControlPanelArea” or “Area” | [optional] 
**disarm_if_all_disarmed** | **str** | The control panel area (CPA) can only be disarmed if all other system areas have been disarmed. (Applicable only for Control Panel Area) | [optional] 
**auto_disarmed** | **bool** | When all the areas in the system are disarmed, the Control Panel Area (CPA), if armed, will disarm. (Applicable only for Control Panel Area) | [optional] 
**parent_area_type** | **str** | Defines the Parent Areas arming relationship with child areas.   - NOTAPARENT: Area contains no child devices. &lt;br&gt;   - MASTER: Area contains child area and its relationship is explained by “ChildAreaOptions” attribute.   - SHARED: Area arms automatically when all child areas are armed. Area disarms automatically when one of the child area is disarmed.   - BANK: Can be armed only after all child areas are armed.&lt;br&gt;   - PASSTHRU: Area arms automatically when one of the child areas is armed. Area disarms automatically when all child areas are disarmed.  | [optional] 
**child_area_options** | **str** | Configurable only for Master Area. &lt;br&gt;   - NONE: Not arming/disarming relationship with its child areas .   - ARMABLEIFCHILDARMED: Can be armed only if all child areas armed.   - ARMDISARMCHILDAREAS: Area will arm/disarm child areas when it is being armed/disarmed.  | [optional] 
**contained_area_list** | **List[str]** | List of all child area(s) SIIDs. | [optional] 
**device_list** | **List[str]** | List of SIIDs of all devices configured in the area. | [optional] 

## Example

```python
from bosch-alarm-map.models.area_configuration import AreaConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AreaConfiguration from a JSON string
area_configuration_instance = AreaConfiguration.from_json(json)
# print the JSON string representation of the object
print(AreaConfiguration.to_json())

# convert the object into a dict
area_configuration_dict = area_configuration_instance.to_dict()
# create an instance of AreaConfiguration from a dict
area_configuration_from_dict = AreaConfiguration.from_dict(area_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


