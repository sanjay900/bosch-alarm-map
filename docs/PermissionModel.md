# PermissionModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arm_category_permissions** | [**PermissionModelArmCategoryPermissions**](PermissionModelArmCategoryPermissions.md) |  | [optional] 
**event_category_permissions** | [**PermissionModelEventCategoryPermissions**](PermissionModelEventCategoryPermissions.md) |  | [optional] 
**maintenance_category_permissions** | [**PermissionModelMaintenanceCategoryPermissions**](PermissionModelMaintenanceCategoryPermissions.md) |  | [optional] 
**operations_category_permissions** | [**PermissionModelOperationsCategoryPermissions**](PermissionModelOperationsCategoryPermissions.md) |  | [optional] 
**remote_service_category_permissions** | [**PermissionModelRemoteServiceCategoryPermissions**](PermissionModelRemoteServiceCategoryPermissions.md) |  | [optional] 
**status_category_permissions** | [**PermissionModelStatusCategoryPermissions**](PermissionModelStatusCategoryPermissions.md) |  | [optional] 
**user_category_permissions** | [**PermissionModelUserCategoryPermissions**](PermissionModelUserCategoryPermissions.md) |  | [optional] 

## Example

```python
from bosch-alarm-map.models.permission_model import PermissionModel

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionModel from a JSON string
permission_model_instance = PermissionModel.from_json(json)
# print the JSON string representation of the object
print(PermissionModel.to_json())

# convert the object into a dict
permission_model_dict = permission_model_instance.to_dict()
# create an instance of PermissionModel from a dict
permission_model_from_dict = PermissionModel.from_dict(permission_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


