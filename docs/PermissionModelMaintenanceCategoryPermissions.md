# PermissionModelMaintenanceCategoryPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**may_adjust_control_center_volume_backlight** | **bool** | This Parameter determines whether the user can adjust the Keypads volume and backlight settings. | [optional] 
**may_change_output_state** | **bool** | This Parameter determines whether the user can change the active/ inactive state of system outputs from the Keypad. | [optional] 
**may_set_date_time** | **bool** | This Parameter determines whether the user can change the system date and time. | [optional] 
**may_test_bell** | **bool** | This Parameter determines whether the user can perform a system belt test. | [optional] 
**may_test_motion_detectors** | **bool** | This Parameter determines whether the user can perform a motion detector test. | [optional] 
**may_walk_test_automatic_points** | **bool** | This Parameter determines whether the user can perform a walk test on automatic points, e.g. detectors with integrated test transmitter. | [optional] 
**may_walk_test_points** | **bool** | This Parameter determines whether the user can perform a walk test on controlled points. | [optional] 
**may_change_network_setting** | **bool** | This Parameter determines whether the user can change the network settings. | [optional] 

## Example

```python
from openapi_client.models.permission_model_maintenance_category_permissions import PermissionModelMaintenanceCategoryPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionModelMaintenanceCategoryPermissions from a JSON string
permission_model_maintenance_category_permissions_instance = PermissionModelMaintenanceCategoryPermissions.from_json(json)
# print the JSON string representation of the object
print(PermissionModelMaintenanceCategoryPermissions.to_json())

# convert the object into a dict
permission_model_maintenance_category_permissions_dict = permission_model_maintenance_category_permissions_instance.to_dict()
# create an instance of PermissionModelMaintenanceCategoryPermissions from a dict
permission_model_maintenance_category_permissions_from_dict = PermissionModelMaintenanceCategoryPermissions.from_dict(permission_model_maintenance_category_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


