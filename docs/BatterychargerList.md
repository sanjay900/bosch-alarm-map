# BatterychargerList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**list** | [**List[Batterycharger]**](Batterycharger.md) | List of all battery chargers | [optional] 

## Example

```python
from openapi_client.models.batterycharger_list import BatterychargerList

# TODO update the JSON string below
json = "{}"
# create an instance of BatterychargerList from a JSON string
batterycharger_list_instance = BatterychargerList.from_json(json)
# print the JSON string representation of the object
print(BatterychargerList.to_json())

# convert the object into a dict
batterycharger_list_dict = batterycharger_list_instance.to_dict()
# create an instance of BatterychargerList from a dict
batterycharger_list_from_dict = BatterychargerList.from_dict(batterycharger_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


