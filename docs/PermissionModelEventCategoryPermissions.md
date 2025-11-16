# PermissionModelEventCategoryPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**may_clear_internal_alarm** | **bool** | This Parameter determines whether the user can clear internal alarm (an alarm that does not report to the central station). | [optional] 
**may_clear_external_alarm** | **bool** | This Parameter determines whether the user can clear an antennal alarm (an alarm that triggers a siren and reports to the central station). | [optional] 
**may_clear_tamper** | **bool** | This Parameter determines whether the user can clear a tamper alert. | [optional] 
**may_clear_trouble** | **bool** | This Parameter determines whether the user can clear a trouble alert. | [optional] 
**may_clear_battery_trouble** | **bool** | This Parameter determines whether the user can clear a battery trouble. | [optional] 
**may_silence** | **bool** | This Parameter determines whether the user can silence events. | [optional] 
**may_clear_main_power_failure** | **bool** | This Parameter determines whether the user can clear power failure alert. | [optional] 
**may_clear_ats** | **bool** | This Parameter determines whether the user can clear ATS. | [optional] 

## Example

```python
from bosch-alarm-map.models.permission_model_event_category_permissions import PermissionModelEventCategoryPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionModelEventCategoryPermissions from a JSON string
permission_model_event_category_permissions_instance = PermissionModelEventCategoryPermissions.from_json(json)
# print the JSON string representation of the object
print(PermissionModelEventCategoryPermissions.to_json())

# convert the object into a dict
permission_model_event_category_permissions_dict = permission_model_event_category_permissions_instance.to_dict()
# create an instance of PermissionModelEventCategoryPermissions from a dict
permission_model_event_category_permissions_from_dict = PermissionModelEventCategoryPermissions.from_dict(permission_model_event_category_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


