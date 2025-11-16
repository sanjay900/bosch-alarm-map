# TimeModelList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_model_sync_id** | **int** | Synchronization ID for the time database table. Will be changed for each change in the time database table. | [optional] 
**list** | [**List[TimeModelListAllOfListInner]**](TimeModelListAllOfListInner.md) | List of all time models | [optional] 

## Example

```python
from bosch_alarm_map.models.time_model_list import TimeModelList

# TODO update the JSON string below
json = "{}"
# create an instance of TimeModelList from a JSON string
time_model_list_instance = TimeModelList.from_json(json)
# print the JSON string representation of the object
print(TimeModelList.to_json())

# convert the object into a dict
time_model_list_dict = time_model_list_instance.to_dict()
# create an instance of TimeModelList from a dict
time_model_list_from_dict = TimeModelList.from_dict(time_model_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


