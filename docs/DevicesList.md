# DevicesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**list** | [**List[Device]**](Device.md) | List of all devices | [optional] 

## Example

```python
from bosch_alarm_map.models.devices_list import DevicesList

# TODO update the JSON string below
json = "{}"
# create an instance of DevicesList from a JSON string
devices_list_instance = DevicesList.from_json(json)
# print the JSON string representation of the object
print(DevicesList.to_json())

# convert the object into a dict
devices_list_dict = devices_list_instance.to_dict()
# create an instance of DevicesList from a dict
devices_list_from_dict = DevicesList.from_dict(devices_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


