# DeviceEnableDisable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** | This operation initiates enabling/disabling the device | [optional] 

## Example

```python
from bosch-alarm-map.models.device_enable_disable import DeviceEnableDisable

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceEnableDisable from a JSON string
device_enable_disable_instance = DeviceEnableDisable.from_json(json)
# print the JSON string representation of the object
print(DeviceEnableDisable.to_json())

# convert the object into a dict
device_enable_disable_dict = device_enable_disable_instance.to_dict()
# create an instance of DeviceEnableDisable from a dict
device_enable_disable_from_dict = DeviceEnableDisable.from_dict(device_enable_disable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


