# DeviceActivateDeactivate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** | This operation initiates activating/deactivating the device | [optional] 

## Example

```python
from bosch-alarm-map.models.device_activate_deactivate import DeviceActivateDeactivate

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceActivateDeactivate from a JSON string
device_activate_deactivate_instance = DeviceActivateDeactivate.from_json(json)
# print the JSON string representation of the object
print(DeviceActivateDeactivate.to_json())

# convert the object into a dict
device_activate_deactivate_dict = device_activate_deactivate_instance.to_dict()
# create an instance of DeviceActivateDeactivate from a dict
device_activate_deactivate_from_dict = DeviceActivateDeactivate.from_dict(device_activate_deactivate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


