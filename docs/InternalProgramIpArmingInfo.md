# InternalProgramIpArmingInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** | This command provides information about the reasons why the internal program cannot be activated. It provides the list of related device urls that prevent the internal program from being activated. | [optional] 

## Example

```python
from bosch_alarm_map.models.internal_program_ip_arming_info import InternalProgramIpArmingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of InternalProgramIpArmingInfo from a JSON string
internal_program_ip_arming_info_instance = InternalProgramIpArmingInfo.from_json(json)
# print the JSON string representation of the object
print(InternalProgramIpArmingInfo.to_json())

# convert the object into a dict
internal_program_ip_arming_info_dict = internal_program_ip_arming_info_instance.to_dict()
# create an instance of InternalProgramIpArmingInfo from a dict
internal_program_ip_arming_info_from_dict = InternalProgramIpArmingInfo.from_dict(internal_program_ip_arming_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


