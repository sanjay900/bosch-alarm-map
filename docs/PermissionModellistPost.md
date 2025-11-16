# PermissionModellistPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** |  | [optional] 
**permission_model_sync_id** | **int** | Synchronization ID for the permission table. Will be changed for each change in the permission database table. | 

## Example

```python
from bosch_alarm_map.models.permission_modellist_post import PermissionModellistPost

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionModellistPost from a JSON string
permission_modellist_post_instance = PermissionModellistPost.from_json(json)
# print the JSON string representation of the object
print(PermissionModellistPost.to_json())

# convert the object into a dict
permission_modellist_post_dict = permission_modellist_post_instance.to_dict()
# create an instance of PermissionModellistPost from a dict
permission_modellist_post_from_dict = PermissionModellistPost.from_dict(permission_modellist_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


