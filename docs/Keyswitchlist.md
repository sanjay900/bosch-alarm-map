# Keyswitchlist


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**list** | [**List[Keyswitch]**](Keyswitch.md) | List of all keyswitches | [optional] 

## Example

```python
from bosch_alarm_map.models.keyswitchlist import Keyswitchlist

# TODO update the JSON string below
json = "{}"
# create an instance of Keyswitchlist from a JSON string
keyswitchlist_instance = Keyswitchlist.from_json(json)
# print the JSON string representation of the object
print(Keyswitchlist.to_json())

# convert the object into a dict
keyswitchlist_dict = keyswitchlist_instance.to_dict()
# create an instance of Keyswitchlist from a dict
keyswitchlist_from_dict = Keyswitchlist.from_dict(keyswitchlist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


