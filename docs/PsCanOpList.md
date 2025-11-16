# PsCanOpList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**list** | [**List[PsCanOp]**](PsCanOp.md) | List of all psCanOps | [optional] 

## Example

```python
from bosch-alarm-map.models.ps_can_op_list import PsCanOpList

# TODO update the JSON string below
json = "{}"
# create an instance of PsCanOpList from a JSON string
ps_can_op_list_instance = PsCanOpList.from_json(json)
# print the JSON string representation of the object
print(PsCanOpList.to_json())

# convert the object into a dict
ps_can_op_list_dict = ps_can_op_list_instance.to_dict()
# create an instance of PsCanOpList from a dict
ps_can_op_list_from_dict = PsCanOpList.from_dict(ps_can_op_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


