# InternalProgramList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**list** | [**List[InternalProgram]**](InternalProgram.md) | List of all internal programs | [optional] 

## Example

```python
from bosch-alarm-map.models.internal_program_list import InternalProgramList

# TODO update the JSON string below
json = "{}"
# create an instance of InternalProgramList from a JSON string
internal_program_list_instance = InternalProgramList.from_json(json)
# print the JSON string representation of the object
print(InternalProgramList.to_json())

# convert the object into a dict
internal_program_list_dict = internal_program_list_instance.to_dict()
# create an instance of InternalProgramList from a dict
internal_program_list_from_dict = InternalProgramList.from_dict(internal_program_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


