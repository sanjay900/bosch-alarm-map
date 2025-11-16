# LsnbusList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**list** | [**List[Lsnbus]**](Lsnbus.md) | List of all lsnbuses | [optional] 

## Example

```python
from bosch_alarm_map.models.lsnbus_list import LsnbusList

# TODO update the JSON string below
json = "{}"
# create an instance of LsnbusList from a JSON string
lsnbus_list_instance = LsnbusList.from_json(json)
# print the JSON string representation of the object
print(LsnbusList.to_json())

# convert the object into a dict
lsnbus_list_dict = lsnbus_list_instance.to_dict()
# create an instance of LsnbusList from a dict
lsnbus_list_from_dict = LsnbusList.from_dict(lsnbus_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


