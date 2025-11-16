# TimeModelSyncID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_model_sync_id** | **int** | Synchronization ID for the time database table. Will be changed for each change in the time database table. | [optional] 

## Example

```python
from bosch_alarm_map.models.time_model_sync_id import TimeModelSyncID

# TODO update the JSON string below
json = "{}"
# create an instance of TimeModelSyncID from a JSON string
time_model_sync_id_instance = TimeModelSyncID.from_json(json)
# print the JSON string representation of the object
print(TimeModelSyncID.to_json())

# convert the object into a dict
time_model_sync_id_dict = time_model_sync_id_instance.to_dict()
# create an instance of TimeModelSyncID from a dict
time_model_sync_id_from_dict = TimeModelSyncID.from_dict(time_model_sync_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


