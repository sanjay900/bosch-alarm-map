# DeviceBypassUnbypass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** | This operation initiates bypassing/unbypassing the device.  Bypassing a device will mean that only non-bypassable incidents will be generated from the device. Usually it is used to allow arming of an area even if the device is not normal e.g. an open window.  | [optional] 

## Example

```python
from openapi_client.models.device_bypass_unbypass import DeviceBypassUnbypass

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceBypassUnbypass from a JSON string
device_bypass_unbypass_instance = DeviceBypassUnbypass.from_json(json)
# print the JSON string representation of the object
print(DeviceBypassUnbypass.to_json())

# convert the object into a dict
device_bypass_unbypass_dict = device_bypass_unbypass_instance.to_dict()
# create an instance of DeviceBypassUnbypass from a dict
device_bypass_unbypass_from_dict = DeviceBypassUnbypass.from_dict(device_bypass_unbypass_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


