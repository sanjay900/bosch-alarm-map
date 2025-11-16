# SmartkeyModelListPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** |  | [optional] 
**smartkey_model_sync_id** | **int** | Synchronization ID for the smart key database table. Will be changed for each change in the smart key database table. | 

## Example

```python
from bosch_alarm_map.models.smartkey_model_list_post import SmartkeyModelListPost

# TODO update the JSON string below
json = "{}"
# create an instance of SmartkeyModelListPost from a JSON string
smartkey_model_list_post_instance = SmartkeyModelListPost.from_json(json)
# print the JSON string representation of the object
print(SmartkeyModelListPost.to_json())

# convert the object into a dict
smartkey_model_list_post_dict = smartkey_model_list_post_instance.to_dict()
# create an instance of SmartkeyModelListPost from a dict
smartkey_model_list_post_from_dict = SmartkeyModelListPost.from_dict(smartkey_model_list_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


