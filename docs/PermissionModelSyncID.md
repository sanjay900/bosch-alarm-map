# PermissionModelSyncID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission_model_sync_id** | **int** | Synchronization ID for the permission table. Will be changed for each change in the permission database table. | 

## Example

```python
from bosch-alarm-map.models.permission_model_sync_id import PermissionModelSyncID

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionModelSyncID from a JSON string
permission_model_sync_id_instance = PermissionModelSyncID.from_json(json)
# print the JSON string representation of the object
print(PermissionModelSyncID.to_json())

# convert the object into a dict
permission_model_sync_id_dict = permission_model_sync_id_instance.to_dict()
# create an instance of PermissionModelSyncID from a dict
permission_model_sync_id_from_dict = PermissionModelSyncID.from_dict(permission_model_sync_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


