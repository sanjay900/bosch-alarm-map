# BatteryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**list** | [**List[Battery]**](Battery.md) | List of all batteries | [optional] 

## Example

```python
from bosch_alarm_map.models.battery_list import BatteryList

# TODO update the JSON string below
json = "{}"
# create an instance of BatteryList from a JSON string
battery_list_instance = BatteryList.from_json(json)
# print the JSON string representation of the object
print(BatteryList.to_json())

# convert the object into a dict
battery_list_dict = battery_list_instance.to_dict()
# create an instance of BatteryList from a dict
battery_list_from_dict = BatteryList.from_dict(battery_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


