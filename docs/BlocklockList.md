# BlocklockList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**list** | [**List[Blocklock]**](Blocklock.md) | List of all blocklocks | [optional] 

## Example

```python
from bosch-alarm-map.models.blocklock_list import BlocklockList

# TODO update the JSON string below
json = "{}"
# create an instance of BlocklockList from a JSON string
blocklock_list_instance = BlocklockList.from_json(json)
# print the JSON string representation of the object
print(BlocklockList.to_json())

# convert the object into a dict
blocklock_list_dict = blocklock_list_instance.to_dict()
# create an instance of BlocklockList from a dict
blocklock_list_from_dict = BlocklockList.from_dict(blocklock_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


