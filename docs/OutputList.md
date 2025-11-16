# OutputList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**list** | [**List[Output]**](Output.md) | List of all outputs | [optional] 

## Example

```python
from openapi_client.models.output_list import OutputList

# TODO update the JSON string below
json = "{}"
# create an instance of OutputList from a JSON string
output_list_instance = OutputList.from_json(json)
# print the JSON string representation of the object
print(OutputList.to_json())

# convert the object into a dict
output_list_dict = output_list_instance.to_dict()
# create an instance of OutputList from a dict
output_list_from_dict = OutputList.from_dict(output_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


