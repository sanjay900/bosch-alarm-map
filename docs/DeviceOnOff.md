# DeviceOnOff


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** | This operation initiates turning on/off the device | [optional] 

## Example

```python
from bosch-alarm-map.models.device_on_off import DeviceOnOff

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceOnOff from a JSON string
device_on_off_instance = DeviceOnOff.from_json(json)
# print the JSON string representation of the object
print(DeviceOnOff.to_json())

# convert the object into a dict
device_on_off_dict = device_on_off_instance.to_dict()
# create an instance of DeviceOnOff from a dict
device_on_off_from_dict = DeviceOnOff.from_dict(device_on_off_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


