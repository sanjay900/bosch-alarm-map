# SubList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**list** | [**List[Sub]**](Sub.md) | List of current subscriptions (respecting the access rights of the user) | [optional] 

## Example

```python
from bosch_alarm_map.models.sub_list import SubList

# TODO update the JSON string below
json = "{}"
# create an instance of SubList from a JSON string
sub_list_instance = SubList.from_json(json)
# print the JSON string representation of the object
print(SubList.to_json())

# convert the object into a dict
sub_list_dict = sub_list_instance.to_dict()
# create an instance of SubList from a dict
sub_list_from_dict = SubList.from_dict(sub_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


