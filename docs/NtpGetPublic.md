# NtpGetPublic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether public servers are used for NTP | [optional] 
**servers** | **List[str]** | Array of the public servers that can be used for NTP, non-configurable fixed entries | [optional] 

## Example

```python
from bosch-alarm-map.models.ntp_get_public import NtpGetPublic

# TODO update the JSON string below
json = "{}"
# create an instance of NtpGetPublic from a JSON string
ntp_get_public_instance = NtpGetPublic.from_json(json)
# print the JSON string representation of the object
print(NtpGetPublic.to_json())

# convert the object into a dict
ntp_get_public_dict = ntp_get_public_instance.to_dict()
# create an instance of NtpGetPublic from a dict
ntp_get_public_from_dict = NtpGetPublic.from_dict(ntp_get_public_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


