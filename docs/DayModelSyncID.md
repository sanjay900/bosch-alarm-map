# DayModelSyncID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_model_sync_id** | **int** | Synchronization ID for the day database table. Will be changed for each change in the day database table. | 

## Example

```python
from bosch-alarm-map.models.day_model_sync_id import DayModelSyncID

# TODO update the JSON string below
json = "{}"
# create an instance of DayModelSyncID from a JSON string
day_model_sync_id_instance = DayModelSyncID.from_json(json)
# print the JSON string representation of the object
print(DayModelSyncID.to_json())

# convert the object into a dict
day_model_sync_id_dict = day_model_sync_id_instance.to_dict()
# create an instance of DayModelSyncID from a dict
day_model_sync_id_from_dict = DayModelSyncID.from_dict(day_model_sync_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


