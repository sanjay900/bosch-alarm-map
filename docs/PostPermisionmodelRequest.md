# PostPermisionmodelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** |  | 
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
from openapi_client.models.post_permisionmodel_request import PostPermisionmodelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostPermisionmodelRequest from a JSON string
post_permisionmodel_request_instance = PostPermisionmodelRequest.from_json(json)
# print the JSON string representation of the object
print(PostPermisionmodelRequest.to_json())

# convert the object into a dict
post_permisionmodel_request_dict = post_permisionmodel_request_instance.to_dict()
# create an instance of PostPermisionmodelRequest from a dict
post_permisionmodel_request_from_dict = PostPermisionmodelRequest.from_dict(post_permisionmodel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


