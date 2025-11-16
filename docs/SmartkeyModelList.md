# SmartkeyModelList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**smartkey_model_sync_id** | **int** | Synchronization ID for the smart key database table. Will be changed for each change in the smart key database table. | 
**list** | [**List[SmartkeyModelListAllOfListInner]**](SmartkeyModelListAllOfListInner.md) | List of all smartkey models | [optional] 

## Example

```python
from openapi_client.models.smartkey_model_list import SmartkeyModelList

# TODO update the JSON string below
json = "{}"
# create an instance of SmartkeyModelList from a JSON string
smartkey_model_list_instance = SmartkeyModelList.from_json(json)
# print the JSON string representation of the object
print(SmartkeyModelList.to_json())

# convert the object into a dict
smartkey_model_list_dict = smartkey_model_list_instance.to_dict()
# create an instance of SmartkeyModelList from a dict
smartkey_model_list_from_dict = SmartkeyModelList.from_dict(smartkey_model_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


