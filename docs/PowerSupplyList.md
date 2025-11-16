# PowerSupplyList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**list** | [**List[PowerSupply]**](PowerSupply.md) | List of all powerSupplies | [optional] 

## Example

```python
from bosch_alarm_map.models.power_supply_list import PowerSupplyList

# TODO update the JSON string below
json = "{}"
# create an instance of PowerSupplyList from a JSON string
power_supply_list_instance = PowerSupplyList.from_json(json)
# print the JSON string representation of the object
print(PowerSupplyList.to_json())

# convert the object into a dict
power_supply_list_dict = power_supply_list_instance.to_dict()
# create an instance of PowerSupplyList from a dict
power_supply_list_from_dict = PowerSupplyList.from_dict(power_supply_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


