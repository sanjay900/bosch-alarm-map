# PermissionModelList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission_model_sync_id** | **int** | Synchronization ID for the permission table. Will be changed for each change in the permission database table. | 
**list** | [**List[PermissionModelListAllOfListInner]**](PermissionModelListAllOfListInner.md) | List of all permission models | [optional] 

## Example

```python
from bosch_alarm_map.models.permission_model_list import PermissionModelList

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionModelList from a JSON string
permission_model_list_instance = PermissionModelList.from_json(json)
# print the JSON string representation of the object
print(PermissionModelList.to_json())

# convert the object into a dict
permission_model_list_dict = permission_model_list_instance.to_dict()
# create an instance of PermissionModelList from a dict
permission_model_list_from_dict = PermissionModelList.from_dict(permission_model_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


