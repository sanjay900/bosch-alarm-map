# PostKeypadSIIDRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** | The firmware version command retrieves the version of the firmware running on the device | [optional] 

## Example

```python
from bosch_alarm_map.models.post_keypad_siid_request import PostKeypadSIIDRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostKeypadSIIDRequest from a JSON string
post_keypad_siid_request_instance = PostKeypadSIIDRequest.from_json(json)
# print the JSON string representation of the object
print(PostKeypadSIIDRequest.to_json())

# convert the object into a dict
post_keypad_siid_request_dict = post_keypad_siid_request_instance.to_dict()
# create an instance of PostKeypadSIIDRequest from a dict
post_keypad_siid_request_from_dict = PostKeypadSIIDRequest.from_dict(post_keypad_siid_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


