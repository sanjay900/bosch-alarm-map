# WalktestList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**list** | [**List[Walktest]**](Walktest.md) | List of all walktests | [optional] 

## Example

```python
from bosch-alarm-map.models.walktest_list import WalktestList

# TODO update the JSON string below
json = "{}"
# create an instance of WalktestList from a JSON string
walktest_list_instance = WalktestList.from_json(json)
# print the JSON string representation of the object
print(WalktestList.to_json())

# convert the object into a dict
walktest_list_dict = walktest_list_instance.to_dict()
# create an instance of WalktestList from a dict
walktest_list_from_dict = WalktestList.from_dict(walktest_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


