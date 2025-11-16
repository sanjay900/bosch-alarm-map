# GetPermissionmodel200Response


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
**permission_model_sync_id** | **int** | Synchronization ID for the permission table. Will be changed for each change in the permission database table. | 

## Example

```python
from bosch-alarm-map.models.get_permissionmodel200_response import GetPermissionmodel200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPermissionmodel200Response from a JSON string
get_permissionmodel200_response_instance = GetPermissionmodel200Response.from_json(json)
# print the JSON string representation of the object
print(GetPermissionmodel200Response.to_json())

# convert the object into a dict
get_permissionmodel200_response_dict = get_permissionmodel200_response_instance.to_dict()
# create an instance of GetPermissionmodel200Response from a dict
get_permissionmodel200_response_from_dict = GetPermissionmodel200Response.from_dict(get_permissionmodel200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


