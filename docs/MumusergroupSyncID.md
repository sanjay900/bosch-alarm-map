# MumusergroupSyncID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mumusergroup_sync_id** | **int** | Synchronization ID for MUM user group. Will be changed for each change in the MUM user group. | 

## Example

```python
from bosch-alarm-map.models.mumusergroup_sync_id import MumusergroupSyncID

# TODO update the JSON string below
json = "{}"
# create an instance of MumusergroupSyncID from a JSON string
mumusergroup_sync_id_instance = MumusergroupSyncID.from_json(json)
# print the JSON string representation of the object
print(MumusergroupSyncID.to_json())

# convert the object into a dict
mumusergroup_sync_id_dict = mumusergroup_sync_id_instance.to_dict()
# create an instance of MumusergroupSyncID from a dict
mumusergroup_sync_id_from_dict = MumusergroupSyncID.from_dict(mumusergroup_sync_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


