# NtpGetCustom


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether custom servers are configured | [optional] 
**servers** | **List[str]** | Array of the custom servers that can be used for NTP, up to 2 entries | [optional] 

## Example

```python
from bosch_alarm_map.models.ntp_get_custom import NtpGetCustom

# TODO update the JSON string below
json = "{}"
# create an instance of NtpGetCustom from a JSON string
ntp_get_custom_instance = NtpGetCustom.from_json(json)
# print the JSON string representation of the object
print(NtpGetCustom.to_json())

# convert the object into a dict
ntp_get_custom_dict = ntp_get_custom_instance.to_dict()
# create an instance of NtpGetCustom from a dict
ntp_get_custom_from_dict = NtpGetCustom.from_dict(ntp_get_custom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


