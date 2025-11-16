# AreaAndTimeModelList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area_and_time_model_sync_id** | **int** | Synchronization ID for the area and time table. Will be changed for each change in the area and time database table. | 
**list** | [**List[AreaAndTimeModelListAllOfListInner]**](AreaAndTimeModelListAllOfListInner.md) | List of all area and time models | [optional] 

## Example

```python
from bosch_alarm_map.models.area_and_time_model_list import AreaAndTimeModelList

# TODO update the JSON string below
json = "{}"
# create an instance of AreaAndTimeModelList from a JSON string
area_and_time_model_list_instance = AreaAndTimeModelList.from_json(json)
# print the JSON string representation of the object
print(AreaAndTimeModelList.to_json())

# convert the object into a dict
area_and_time_model_list_dict = area_and_time_model_list_instance.to_dict()
# create an instance of AreaAndTimeModelList from a dict
area_and_time_model_list_from_dict = AreaAndTimeModelList.from_dict(area_and_time_model_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


