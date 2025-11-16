# AreaList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**list** | [**List[Area]**](Area.md) | List of all areas | [optional] 

## Example

```python
from bosch_alarm_map.models.area_list import AreaList

# TODO update the JSON string below
json = "{}"
# create an instance of AreaList from a JSON string
area_list_instance = AreaList.from_json(json)
# print the JSON string representation of the object
print(AreaList.to_json())

# convert the object into a dict
area_list_dict = area_list_instance.to_dict()
# create an instance of AreaList from a dict
area_list_from_dict = AreaList.from_dict(area_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


