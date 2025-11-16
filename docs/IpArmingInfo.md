# IpArmingInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_list** | **List[str]** | The list of devices urls that prevent the internal program from being activated | [optional] 
**activated** | **bool** | Indicates whether internal program is activated | [optional] 
**can_be_activated** | **bool** | Indicates whether internal program can be activated. If it is already activated, then this flag will be false | [optional] 

## Example

```python
from openapi_client.models.ip_arming_info import IpArmingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IpArmingInfo from a JSON string
ip_arming_info_instance = IpArmingInfo.from_json(json)
# print the JSON string representation of the object
print(IpArmingInfo.to_json())

# convert the object into a dict
ip_arming_info_dict = ip_arming_info_instance.to_dict()
# create an instance of IpArmingInfo from a dict
ip_arming_info_from_dict = IpArmingInfo.from_dict(ip_arming_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


