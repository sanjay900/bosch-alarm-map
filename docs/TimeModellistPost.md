# TimeModellistPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** |  | [optional] 
**time_model_sync_id** | **int** | Synchronization ID for the time database table. Will be changed for each change in the time database table. | [optional] 

## Example

```python
from bosch-alarm-map.models.time_modellist_post import TimeModellistPost

# TODO update the JSON string below
json = "{}"
# create an instance of TimeModellistPost from a JSON string
time_modellist_post_instance = TimeModellistPost.from_json(json)
# print the JSON string representation of the object
print(TimeModellistPost.to_json())

# convert the object into a dict
time_modellist_post_dict = time_modellist_post_instance.to_dict()
# create an instance of TimeModellistPost from a dict
time_modellist_post_from_dict = TimeModellistPost.from_dict(time_modellist_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


