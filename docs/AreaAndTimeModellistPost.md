# AreaAndTimeModellistPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** |  | [optional] 
**area_and_time_model_sync_id** | **int** | Synchronization ID for the area and time table. Will be changed for each change in the area and time database table. | 

## Example

```python
from openapi_client.models.area_and_time_modellist_post import AreaAndTimeModellistPost

# TODO update the JSON string below
json = "{}"
# create an instance of AreaAndTimeModellistPost from a JSON string
area_and_time_modellist_post_instance = AreaAndTimeModellistPost.from_json(json)
# print the JSON string representation of the object
print(AreaAndTimeModellistPost.to_json())

# convert the object into a dict
area_and_time_modellist_post_dict = area_and_time_modellist_post_instance.to_dict()
# create an instance of AreaAndTimeModellistPost from a dict
area_and_time_modellist_post_from_dict = AreaAndTimeModellistPost.from_dict(area_and_time_modellist_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


