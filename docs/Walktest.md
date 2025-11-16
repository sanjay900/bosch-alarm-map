# Walktest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**user** | **str** | Id of the user that started the walktest | [optional] 
**interface** | **str** | Interface that was used to start the walktest | [optional] 
**wt** | [**List[WalktestWtInner]**](WalktestWtInner.md) | List of tuples of “area” and “wtStatus” | [optional] 

## Example

```python
from bosch-alarm-map.models.walktest import Walktest

# TODO update the JSON string below
json = "{}"
# create an instance of Walktest from a JSON string
walktest_instance = Walktest.from_json(json)
# print the JSON string representation of the object
print(Walktest.to_json())

# convert the object into a dict
walktest_dict = walktest_instance.to_dict()
# create an instance of Walktest from a dict
walktest_from_dict = Walktest.from_dict(walktest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


