# PermissionModelArmCategoryPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**may_arm_area** | **bool** | This Parameter determines whether the user can arm an area. | [optional] 
**may_arm_with_active_tamper** | **bool** | This Parameter determines whether the user can arm the system if there is an active tamper condition. | [optional] 
**may_disarm_area** | **bool** | This Parameter determines whether the user can disarm an area. | [optional] 
**may_disarm_only_from_alarm** | **bool** | This Parameter determines whether the user can disarm the system only when there is an active alarm condition. | [optional] 
**may_bypass_detector** | **bool** | This Parameter determines whether the user can bypass detectors. | [optional] 
**may_force_bypass_detectors_in_area** | **bool** | This Parameter determines whether the user can bypass detectors while force the area. | [optional] 
**may_un_bypass_detector** | **bool** | This Parameter determines whether the user can return a detector from bypassed to active status. | [optional] 
**may_un_bypassforciblybypassed_detectors_in_ar** | **bool** | This Parameter determines whether the user can return forcibly bypassed detectors in an area from bypassed to active status. | [optional] 
**may_switch_internal_program_on_off** | **bool** | This Parameter determines whether the user can turn internal programs on or off. | [optional] 

## Example

```python
from bosch-alarm-map.models.permission_model_arm_category_permissions import PermissionModelArmCategoryPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionModelArmCategoryPermissions from a JSON string
permission_model_arm_category_permissions_instance = PermissionModelArmCategoryPermissions.from_json(json)
# print the JSON string representation of the object
print(PermissionModelArmCategoryPermissions.to_json())

# convert the object into a dict
permission_model_arm_category_permissions_dict = permission_model_arm_category_permissions_instance.to_dict()
# create an instance of PermissionModelArmCategoryPermissions from a dict
permission_model_arm_category_permissions_from_dict = PermissionModelArmCategoryPermissions.from_dict(permission_model_arm_category_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


