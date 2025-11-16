# PermissionModelID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission_model_id** | **str** | Unique name of an existing permission model.  The name is used to identify the item on the MAP system. The following charaters are forbidden in identifier name: \&quot; @ ;  | 

## Example

```python
from bosch-alarm-map.models.permission_model_id import PermissionModelID

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionModelID from a JSON string
permission_model_id_instance = PermissionModelID.from_json(json)
# print the JSON string representation of the object
print(PermissionModelID.to_json())

# convert the object into a dict
permission_model_id_dict = permission_model_id_instance.to_dict()
# create an instance of PermissionModelID from a dict
permission_model_id_from_dict = PermissionModelID.from_dict(permission_model_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


