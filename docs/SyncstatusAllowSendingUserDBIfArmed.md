# SyncstatusAllowSendingUserDBIfArmed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_sending_user_dbif_armed** | **bool** | Flags whether it is possible to do database modifications using REST-API. Configurable in RPS for MAP &#39;Allow sending user database if armed&#39;. | 

## Example

```python
from openapi_client.models.syncstatus_allow_sending_user_dbif_armed import SyncstatusAllowSendingUserDBIfArmed

# TODO update the JSON string below
json = "{}"
# create an instance of SyncstatusAllowSendingUserDBIfArmed from a JSON string
syncstatus_allow_sending_user_dbif_armed_instance = SyncstatusAllowSendingUserDBIfArmed.from_json(json)
# print the JSON string representation of the object
print(SyncstatusAllowSendingUserDBIfArmed.to_json())

# convert the object into a dict
syncstatus_allow_sending_user_dbif_armed_dict = syncstatus_allow_sending_user_dbif_armed_instance.to_dict()
# create an instance of SyncstatusAllowSendingUserDBIfArmed from a dict
syncstatus_allow_sending_user_dbif_armed_from_dict = SyncstatusAllowSendingUserDBIfArmed.from_dict(syncstatus_allow_sending_user_dbif_armed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


