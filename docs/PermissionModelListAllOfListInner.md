# PermissionModelListAllOfListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission_model_id** | **str** | Unique name of an existing permission model.  The name is used to identify the item on the MAP system. The following charaters are forbidden in identifier name: \&quot; @ ;  | 
**arm_category_permissions** | [**PermissionModelArmCategoryPermissions**](PermissionModelArmCategoryPermissions.md) |  | [optional] 
**event_category_permissions** | [**PermissionModelEventCategoryPermissions**](PermissionModelEventCategoryPermissions.md) |  | [optional] 
**maintenance_category_permissions** | [**PermissionModelMaintenanceCategoryPermissions**](PermissionModelMaintenanceCategoryPermissions.md) |  | [optional] 
**operations_category_permissions** | [**PermissionModelOperationsCategoryPermissions**](PermissionModelOperationsCategoryPermissions.md) |  | [optional] 
**remote_service_category_permissions** | [**PermissionModelRemoteServiceCategoryPermissions**](PermissionModelRemoteServiceCategoryPermissions.md) |  | [optional] 
**status_category_permissions** | [**PermissionModelStatusCategoryPermissions**](PermissionModelStatusCategoryPermissions.md) |  | [optional] 
**user_category_permissions** | [**PermissionModelUserCategoryPermissions**](PermissionModelUserCategoryPermissions.md) |  | [optional] 

## Example

```python
from bosch_alarm_map.models.permission_model_list_all_of_list_inner import PermissionModelListAllOfListInner

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionModelListAllOfListInner from a JSON string
permission_model_list_all_of_list_inner_instance = PermissionModelListAllOfListInner.from_json(json)
# print the JSON string representation of the object
print(PermissionModelListAllOfListInner.to_json())

# convert the object into a dict
permission_model_list_all_of_list_inner_dict = permission_model_list_all_of_list_inner_instance.to_dict()
# create an instance of PermissionModelListAllOfListInner from a dict
permission_model_list_all_of_list_inner_from_dict = PermissionModelListAllOfListInner.from_dict(permission_model_list_all_of_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


