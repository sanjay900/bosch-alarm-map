# DayModelList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_model_sync_id** | **int** | Synchronization ID for the day database table. Will be changed for each change in the day database table. | 
**list** | [**List[DayModelListAllOfListInner]**](DayModelListAllOfListInner.md) | List of daymodels | [optional] 

## Example

```python
from bosch-alarm-map.models.day_model_list import DayModelList

# TODO update the JSON string below
json = "{}"
# create an instance of DayModelList from a JSON string
day_model_list_instance = DayModelList.from_json(json)
# print the JSON string representation of the object
print(DayModelList.to_json())

# convert the object into a dict
day_model_list_dict = day_model_list_instance.to_dict()
# create an instance of DayModelList from a dict
day_model_list_from_dict = DayModelList.from_dict(day_model_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


