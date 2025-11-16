# PermissionModelUserCategoryPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**may_add_user** | **bool** | This Parameter determines whether the user can add users to the system. | [optional] 
**may_delete_user** | **bool** | This Parameter determines whether the user can delete other users from the system. | [optional] 
**may_change_user_passcode** | **bool** | This Parameter determines whether the user can change another user&#39;s passcode | [optional] 

## Example

```python
from openapi_client.models.permission_model_user_category_permissions import PermissionModelUserCategoryPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionModelUserCategoryPermissions from a JSON string
permission_model_user_category_permissions_instance = PermissionModelUserCategoryPermissions.from_json(json)
# print the JSON string representation of the object
print(PermissionModelUserCategoryPermissions.to_json())

# convert the object into a dict
permission_model_user_category_permissions_dict = permission_model_user_category_permissions_instance.to_dict()
# create an instance of PermissionModelUserCategoryPermissions from a dict
permission_model_user_category_permissions_from_dict = PermissionModelUserCategoryPermissions.from_dict(permission_model_user_category_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


