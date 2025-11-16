# PermissionModelOperationsCategoryPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**may_disable_device** | **bool** | This Parameter determines whether the user can block system devices. | [optional] 
**may_enable_device** | **bool** | This Parameter determines whether the user can return a system device from disabled to enabled status. | [optional] 
**may_turn_chime_on_off** | **bool** | This Parameter determines whether the user can turn Chime Mode on or off. | [optional] 
**may_change_schedule** | **bool** | This Parameter determines whether the user can change the date/time of scheduled events from the Keypad. | [optional] 
**may_edit_blocking_time** | **bool** | This Parameter determines whether the user can edit blocking time for disarming of areas. | [optional] 

## Example

```python
from bosch-alarm-map.models.permission_model_operations_category_permissions import PermissionModelOperationsCategoryPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionModelOperationsCategoryPermissions from a JSON string
permission_model_operations_category_permissions_instance = PermissionModelOperationsCategoryPermissions.from_json(json)
# print the JSON string representation of the object
print(PermissionModelOperationsCategoryPermissions.to_json())

# convert the object into a dict
permission_model_operations_category_permissions_dict = permission_model_operations_category_permissions_instance.to_dict()
# create an instance of PermissionModelOperationsCategoryPermissions from a dict
permission_model_operations_category_permissions_from_dict = PermissionModelOperationsCategoryPermissions.from_dict(permission_model_operations_category_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


