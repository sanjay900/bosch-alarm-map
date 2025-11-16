# PermissionModelRemoteServiceCategoryPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**may_authorize_manufacturer_user** | **bool** | This Parameter determines whether the user can authorize manufacturer user access. | [optional] 
**may_authorize_rps_user** | **bool** | This Parameter determines whether the user can authorize remote programming software RPS for MAP user access. | [optional] 

## Example

```python
from bosch_alarm_map.models.permission_model_remote_service_category_permissions import PermissionModelRemoteServiceCategoryPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionModelRemoteServiceCategoryPermissions from a JSON string
permission_model_remote_service_category_permissions_instance = PermissionModelRemoteServiceCategoryPermissions.from_json(json)
# print the JSON string representation of the object
print(PermissionModelRemoteServiceCategoryPermissions.to_json())

# convert the object into a dict
permission_model_remote_service_category_permissions_dict = permission_model_remote_service_category_permissions_instance.to_dict()
# create an instance of PermissionModelRemoteServiceCategoryPermissions from a dict
permission_model_remote_service_category_permissions_from_dict = PermissionModelRemoteServiceCategoryPermissions.from_dict(permission_model_remote_service_category_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


