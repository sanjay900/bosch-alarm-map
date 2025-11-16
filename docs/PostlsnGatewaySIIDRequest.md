# PostlsnGatewaySIIDRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** | The firmware version command retrieves the version of the firmware running on the device | [optional] 

## Example

```python
from bosch_alarm_map.models.postlsn_gateway_siid_request import PostlsnGatewaySIIDRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostlsnGatewaySIIDRequest from a JSON string
postlsn_gateway_siid_request_instance = PostlsnGatewaySIIDRequest.from_json(json)
# print the JSON string representation of the object
print(PostlsnGatewaySIIDRequest.to_json())

# convert the object into a dict
postlsn_gateway_siid_request_dict = postlsn_gateway_siid_request_instance.to_dict()
# create an instance of PostlsnGatewaySIIDRequest from a dict
postlsn_gateway_siid_request_from_dict = PostlsnGatewaySIIDRequest.from_dict(postlsn_gateway_siid_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


