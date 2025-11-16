# MainList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**list** | [**List[Main]**](Main.md) | List of all mains | [optional] 

## Example

```python
from bosch_alarm_map.models.main_list import MainList

# TODO update the JSON string below
json = "{}"
# create an instance of MainList from a JSON string
main_list_instance = MainList.from_json(json)
# print the JSON string representation of the object
print(MainList.to_json())

# convert the object into a dict
main_list_dict = main_list_instance.to_dict()
# create an instance of MainList from a dict
main_list_from_dict = MainList.from_dict(main_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


