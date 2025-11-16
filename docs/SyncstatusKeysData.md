# SyncstatusKeysData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**master_key_checksum** | **str** | Checksum of the Master Key | 
**master_key_timestamp** | **str** | Timestamp of the Master Key | 
**shared_key_checksum** | **str** | Checksum of the Shared Key | 
**shared_key_timestamp** | **str** | Timestamp of the Shared Key | 

## Example

```python
from bosch-alarm-map.models.syncstatus_keys_data import SyncstatusKeysData

# TODO update the JSON string below
json = "{}"
# create an instance of SyncstatusKeysData from a JSON string
syncstatus_keys_data_instance = SyncstatusKeysData.from_json(json)
# print the JSON string representation of the object
print(SyncstatusKeysData.to_json())

# convert the object into a dict
syncstatus_keys_data_dict = syncstatus_keys_data_instance.to_dict()
# create an instance of SyncstatusKeysData from a dict
syncstatus_keys_data_from_dict = SyncstatusKeysData.from_dict(syncstatus_keys_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


