# NtpPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public** | **bool** | Enables or disables usage of public servers for NTP | [optional] 
**custom** | **List[str]** | Array of custom NTP servers, 1 or 2 entries are supported. Set to empty array to disable. Both URL (IP) and port must be provided in format URL:port | [optional] 

## Example

```python
from bosch_alarm_map.models.ntp_post import NtpPost

# TODO update the JSON string below
json = "{}"
# create an instance of NtpPost from a JSON string
ntp_post_instance = NtpPost.from_json(json)
# print the JSON string representation of the object
print(NtpPost.to_json())

# convert the object into a dict
ntp_post_dict = ntp_post_instance.to_dict()
# create an instance of NtpPost from a dict
ntp_post_from_dict = NtpPost.from_dict(ntp_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


