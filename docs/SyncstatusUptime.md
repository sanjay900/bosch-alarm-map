# SyncstatusUptime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uptime** | **int** | The MAP panel uptime, seconds since the last boot. If this counter jumps backwards, the MAP panel was rebooted. | 

## Example

```python
from bosch-alarm-map.models.syncstatus_uptime import SyncstatusUptime

# TODO update the JSON string below
json = "{}"
# create an instance of SyncstatusUptime from a JSON string
syncstatus_uptime_instance = SyncstatusUptime.from_json(json)
# print the JSON string representation of the object
print(SyncstatusUptime.to_json())

# convert the object into a dict
syncstatus_uptime_dict = syncstatus_uptime_instance.to_dict()
# create an instance of SyncstatusUptime from a dict
syncstatus_uptime_from_dict = SyncstatusUptime.from_dict(syncstatus_uptime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


