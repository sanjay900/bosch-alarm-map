# AccessModelList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_model_sync_id** | **int** | Synchronization ID for the access table. Will be changed for each change in the access database table. | 
**list** | [**List[AccessModelListAllOfListInner]**](AccessModelListAllOfListInner.md) | List of all access models | [optional] 

## Example

```python
from bosch_alarm_map.models.access_model_list import AccessModelList

# TODO update the JSON string below
json = "{}"
# create an instance of AccessModelList from a JSON string
access_model_list_instance = AccessModelList.from_json(json)
# print the JSON string representation of the object
print(AccessModelList.to_json())

# convert the object into a dict
access_model_list_dict = access_model_list_instance.to_dict()
# create an instance of AccessModelList from a dict
access_model_list_from_dict = AccessModelList.from_dict(access_model_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


