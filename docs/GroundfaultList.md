# GroundfaultList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**list** | [**List[Groundfault]**](Groundfault.md) | List of all groundfaults | [optional] 

## Example

```python
from openapi_client.models.groundfault_list import GroundfaultList

# TODO update the JSON string below
json = "{}"
# create an instance of GroundfaultList from a JSON string
groundfault_list_instance = GroundfaultList.from_json(json)
# print the JSON string representation of the object
print(GroundfaultList.to_json())

# convert the object into a dict
groundfault_list_dict = groundfault_list_instance.to_dict()
# create an instance of GroundfaultList from a dict
groundfault_list_from_dict = GroundfaultList.from_dict(groundfault_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


