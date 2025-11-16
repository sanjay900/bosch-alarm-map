# InternalProgram


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier. | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**active** | **bool** | True, if the internal program is active. False, otherwise. | [optional] 

## Example

```python
from bosch_alarm_map.models.internal_program import InternalProgram

# TODO update the JSON string below
json = "{}"
# create an instance of InternalProgram from a JSON string
internal_program_instance = InternalProgram.from_json(json)
# print the JSON string representation of the object
print(InternalProgram.to_json())

# convert the object into a dict
internal_program_dict = internal_program_instance.to_dict()
# create an instance of InternalProgram from a dict
internal_program_from_dict = InternalProgram.from_dict(internal_program_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


