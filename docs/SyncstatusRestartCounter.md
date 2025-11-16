# SyncstatusRestartCounter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**restart_counter** | **int** | The number of restarts the MAP panel performed. If this counter jumps backwards, the MAP panel was updated. | 

## Example

```python
from bosch-alarm-map.models.syncstatus_restart_counter import SyncstatusRestartCounter

# TODO update the JSON string below
json = "{}"
# create an instance of SyncstatusRestartCounter from a JSON string
syncstatus_restart_counter_instance = SyncstatusRestartCounter.from_json(json)
# print the JSON string representation of the object
print(SyncstatusRestartCounter.to_json())

# convert the object into a dict
syncstatus_restart_counter_dict = syncstatus_restart_counter_instance.to_dict()
# create an instance of SyncstatusRestartCounter from a dict
syncstatus_restart_counter_from_dict = SyncstatusRestartCounter.from_dict(syncstatus_restart_counter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


