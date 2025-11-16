# LSNLoopNonBypassableIntrusionPointPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of a device. | 
**name** | **str** | LSN device internal name. | 
**area** | **str** | LSN device area. | 
**point_type** | **str** | Point device type. | 
**supports_delayed_reporting** | **bool** | Delayed reporting support. | [optional] 
**walktest_category** | [**LSNWalktestCategoryProperty**](LSNWalktestCategoryProperty.md) |  | [optional] 
**chime_mode_capable** | **bool** | Controls whether the point can trigger the chime tone on Keypad. | [optional] 
**delay_for_alarm_detection** | **int** | Delay for alarm detection in seconds. | [optional] 
**entry_point** | **str** | Device entry point. | [optional] 
**exit_point** | **str** | Device exit point. | [optional] 
**walktest_trigger_frequency** | [**LSNWalktestTriggerFrequencyProperty**](LSNWalktestTriggerFrequencyProperty.md) |  | [optional] 

## Example

```python
from openapi_client.models.lsn_loop_non_bypassable_intrusion_point_post import LSNLoopNonBypassableIntrusionPointPost

# TODO update the JSON string below
json = "{}"
# create an instance of LSNLoopNonBypassableIntrusionPointPost from a JSON string
lsn_loop_non_bypassable_intrusion_point_post_instance = LSNLoopNonBypassableIntrusionPointPost.from_json(json)
# print the JSON string representation of the object
print(LSNLoopNonBypassableIntrusionPointPost.to_json())

# convert the object into a dict
lsn_loop_non_bypassable_intrusion_point_post_dict = lsn_loop_non_bypassable_intrusion_point_post_instance.to_dict()
# create an instance of LSNLoopNonBypassableIntrusionPointPost from a dict
lsn_loop_non_bypassable_intrusion_point_post_from_dict = LSNLoopNonBypassableIntrusionPointPost.from_dict(lsn_loop_non_bypassable_intrusion_point_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


