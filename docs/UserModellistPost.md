# UserModellistPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** |  | [optional] 
**user_model_sync_id** | **int** | Synchronization ID for the user database table. Will be changed for each change in the user database table. | 

## Example

```python
from bosch_alarm_map.models.user_modellist_post import UserModellistPost

# TODO update the JSON string below
json = "{}"
# create an instance of UserModellistPost from a JSON string
user_modellist_post_instance = UserModellistPost.from_json(json)
# print the JSON string representation of the object
print(UserModellistPost.to_json())

# convert the object into a dict
user_modellist_post_dict = user_modellist_post_instance.to_dict()
# create an instance of UserModellistPost from a dict
user_modellist_post_from_dict = UserModellistPost.from_dict(user_modellist_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


