# UserModelSyncID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_model_sync_id** | **int** | Synchronization ID for the user database table. Will be changed for each change in the user database table. | 

## Example

```python
from openapi_client.models.user_model_sync_id import UserModelSyncID

# TODO update the JSON string below
json = "{}"
# create an instance of UserModelSyncID from a JSON string
user_model_sync_id_instance = UserModelSyncID.from_json(json)
# print the JSON string representation of the object
print(UserModelSyncID.to_json())

# convert the object into a dict
user_model_sync_id_dict = user_model_sync_id_instance.to_dict()
# create an instance of UserModelSyncID from a dict
user_model_sync_id_from_dict = UserModelSyncID.from_dict(user_model_sync_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


