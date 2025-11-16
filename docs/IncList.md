# IncList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**list** | [**List[Inc]**](Inc.md) | List of all incidents | [optional] 

## Example

```python
from openapi_client.models.inc_list import IncList

# TODO update the JSON string below
json = "{}"
# create an instance of IncList from a JSON string
inc_list_instance = IncList.from_json(json)
# print the JSON string representation of the object
print(IncList.to_json())

# convert the object into a dict
inc_list_dict = inc_list_instance.to_dict()
# create an instance of IncList from a dict
inc_list_from_dict = IncList.from_dict(inc_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


