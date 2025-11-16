# AccessModelSyncID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_model_sync_id** | **int** | Synchronization ID for the access table. Will be changed for each change in the access database table. | 

## Example

```python
from openapi_client.models.access_model_sync_id import AccessModelSyncID

# TODO update the JSON string below
json = "{}"
# create an instance of AccessModelSyncID from a JSON string
access_model_sync_id_instance = AccessModelSyncID.from_json(json)
# print the JSON string representation of the object
print(AccessModelSyncID.to_json())

# convert the object into a dict
access_model_sync_id_dict = access_model_sync_id_instance.to_dict()
# create an instance of AccessModelSyncID from a dict
access_model_sync_id_from_dict = AccessModelSyncID.from_dict(access_model_sync_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


