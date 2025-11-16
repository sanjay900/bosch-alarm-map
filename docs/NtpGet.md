# NtpGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Timestamp and server of the last received NTP state otherwise empty | [optional] 
**resync** | **int** | Seconds until a next periodic NTP synchronization, value of 0 is shown in case of disabled NTP. Periodic synchronization is done once per 7 days | [optional] 
**public** | [**NtpGetPublic**](NtpGetPublic.md) |  | [optional] 
**custom** | [**NtpGetCustom**](NtpGetCustom.md) |  | [optional] 

## Example

```python
from bosch-alarm-map.models.ntp_get import NtpGet

# TODO update the JSON string below
json = "{}"
# create an instance of NtpGet from a JSON string
ntp_get_instance = NtpGet.from_json(json)
# print the JSON string representation of the object
print(NtpGet.to_json())

# convert the object into a dict
ntp_get_dict = ntp_get_instance.to_dict()
# create an instance of NtpGet from a dict
ntp_get_from_dict = NtpGet.from_dict(ntp_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


