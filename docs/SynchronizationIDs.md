# SynchronizationIDs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_model_sync_id** | **int** | Synchronization ID for the user database table. Will be changed for each change in the user database table. | 
**day_model_sync_id** | **int** | Synchronization ID for the day database table. Will be changed for each change in the day database table. | 
**time_model_sync_id** | **int** | Synchronization ID for the time database table. Will be changed for each change in the time database table. | [optional] 
**special_day_model_sync_id** | **int** | Synchronization ID for the special day database table. Will be changed for each change in the special day database table. | 
**area_and_time_model_sync_id** | **int** | Synchronization ID for the area and time table. Will be changed for each change in the area and time database table. | 
**smartkey_model_sync_id** | **int** | Synchronization ID for the smart key database table. Will be changed for each change in the smart key database table. | 
**access_model_sync_id** | **int** | Synchronization ID for the access table. Will be changed for each change in the access database table. | 
**permission_model_sync_id** | **int** | Synchronization ID for the permission table. Will be changed for each change in the permission database table. | 
**mumusergroup_sync_id** | **int** | Synchronization ID for MUM user group. Will be changed for each change in the MUM user group. | 
**uptime** | **int** | The MAP panel uptime, seconds since the last boot. If this counter jumps backwards, the MAP panel was rebooted. | 
**restart_counter** | **int** | The number of restarts the MAP panel performed. If this counter jumps backwards, the MAP panel was updated. | 
**master_key_checksum** | **str** | Checksum of the Master Key | 
**master_key_timestamp** | **str** | Timestamp of the Master Key | 
**shared_key_checksum** | **str** | Checksum of the Shared Key | 
**shared_key_timestamp** | **str** | Timestamp of the Shared Key | 
**allow_sending_user_dbif_armed** | **bool** | Flags whether it is possible to do database modifications using REST-API. Configurable in RPS for MAP &#39;Allow sending user database if armed&#39;. | 

## Example

```python
from bosch-alarm-map.models.synchronization_ids import SynchronizationIDs

# TODO update the JSON string below
json = "{}"
# create an instance of SynchronizationIDs from a JSON string
synchronization_ids_instance = SynchronizationIDs.from_json(json)
# print the JSON string representation of the object
print(SynchronizationIDs.to_json())

# convert the object into a dict
synchronization_ids_dict = synchronization_ids_instance.to_dict()
# create an instance of SynchronizationIDs from a dict
synchronization_ids_from_dict = SynchronizationIDs.from_dict(synchronization_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


