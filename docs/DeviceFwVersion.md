# DeviceFwVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** | The firmware version command retrieves the version of the firmware running on the device | [optional] 

## Example

```python
from bosch_alarm_map.models.device_fw_version import DeviceFwVersion

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceFwVersion from a JSON string
device_fw_version_instance = DeviceFwVersion.from_json(json)
# print the JSON string representation of the object
print(DeviceFwVersion.to_json())

# convert the object into a dict
device_fw_version_dict = device_fw_version_instance.to_dict()
# create an instance of DeviceFwVersion from a dict
device_fw_version_from_dict = DeviceFwVersion.from_dict(device_fw_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


