# PermissionModelStatusCategoryPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**may_view_area_status** | **bool** | This Parameter determines whether the user can view an area\&quot;s status. | [optional] 
**may_view_device_status** | **bool** | This Parameter determines whether the user can view system device status. | [optional] 
**may_view_duress_alarm** | **bool** | This Parameter determines whether the user can view duress alarms. | [optional] 
**may_view_alarm_count** | **bool** | This Parameter determines whether the user can view the alarm counter. | [optional] 
**may_view_event_memory** | **bool** | This Parameter determines whether the user can view the alarm memory. | [optional] 
**may_view_control_panel_history** | **bool** | This Parameter determines whether the user can view the control panel&#39;s history list. | [optional] 
**may_print_control_panel_history** | **bool** | This Parameter determines whether the user can print the control panel&#39;s history events. | [optional] 
**may_view_control_panel_version** | **bool** | This Parameter determines whether the user can view the control panel&#39;s firmware version. | [optional] 

## Example

```python
from openapi_client.models.permission_model_status_category_permissions import PermissionModelStatusCategoryPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionModelStatusCategoryPermissions from a JSON string
permission_model_status_category_permissions_instance = PermissionModelStatusCategoryPermissions.from_json(json)
# print the JSON string representation of the object
print(PermissionModelStatusCategoryPermissions.to_json())

# convert the object into a dict
permission_model_status_category_permissions_dict = permission_model_status_category_permissions_instance.to_dict()
# create an instance of PermissionModelStatusCategoryPermissions from a dict
permission_model_status_category_permissions_from_dict = PermissionModelStatusCategoryPermissions.from_dict(permission_model_status_category_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


