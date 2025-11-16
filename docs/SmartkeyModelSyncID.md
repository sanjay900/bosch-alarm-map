# SmartkeyModelSyncID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**smartkey_model_sync_id** | **int** | Synchronization ID for the smart key database table. Will be changed for each change in the smart key database table. | 

## Example

```python
from bosch-alarm-map.models.smartkey_model_sync_id import SmartkeyModelSyncID

# TODO update the JSON string below
json = "{}"
# create an instance of SmartkeyModelSyncID from a JSON string
smartkey_model_sync_id_instance = SmartkeyModelSyncID.from_json(json)
# print the JSON string representation of the object
print(SmartkeyModelSyncID.to_json())

# convert the object into a dict
smartkey_model_sync_id_dict = smartkey_model_sync_id_instance.to_dict()
# create an instance of SmartkeyModelSyncID from a dict
smartkey_model_sync_id_from_dict = SmartkeyModelSyncID.from_dict(smartkey_model_sync_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


