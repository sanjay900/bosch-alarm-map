# SmartkeyList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**list** | [**List[Smartkey]**](Smartkey.md) | List of all Smartkeys | [optional] 

## Example

```python
from openapi_client.models.smartkey_list import SmartkeyList

# TODO update the JSON string below
json = "{}"
# create an instance of SmartkeyList from a JSON string
smartkey_list_instance = SmartkeyList.from_json(json)
# print the JSON string representation of the object
print(SmartkeyList.to_json())

# convert the object into a dict
smartkey_list_dict = smartkey_list_instance.to_dict()
# create an instance of SmartkeyList from a dict
smartkey_list_from_dict = SmartkeyList.from_dict(smartkey_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


