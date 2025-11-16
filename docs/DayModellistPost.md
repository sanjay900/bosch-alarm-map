# DayModellistPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** |  | [optional] 
**day_model_sync_id** | **int** | Synchronization ID for the day database table. Will be changed for each change in the day database table. | 

## Example

```python
from bosch_alarm_map.models.day_modellist_post import DayModellistPost

# TODO update the JSON string below
json = "{}"
# create an instance of DayModellistPost from a JSON string
day_modellist_post_instance = DayModellistPost.from_json(json)
# print the JSON string representation of the object
print(DayModellistPost.to_json())

# convert the object into a dict
day_modellist_post_dict = day_modellist_post_instance.to_dict()
# create an instance of DayModellistPost from a dict
day_modellist_post_from_dict = DayModellistPost.from_dict(day_modellist_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


