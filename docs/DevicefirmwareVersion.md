# DevicefirmwareVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firmware_version** | **str** | Firmware version of a DEModule, Keypad, Power Supply or LSNGateway in format MAJOR.MINOR.MICRO | [optional] 

## Example

```python
from bosch_alarm_map.models.devicefirmware_version import DevicefirmwareVersion

# TODO update the JSON string below
json = "{}"
# create an instance of DevicefirmwareVersion from a JSON string
devicefirmware_version_instance = DevicefirmwareVersion.from_json(json)
# print the JSON string representation of the object
print(DevicefirmwareVersion.to_json())

# convert the object into a dict
devicefirmware_version_dict = devicefirmware_version_instance.to_dict()
# create an instance of DevicefirmwareVersion from a dict
devicefirmware_version_from_dict = DevicefirmwareVersion.from_dict(devicefirmware_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


