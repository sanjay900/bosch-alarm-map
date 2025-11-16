# LSNLoopNonSilentHoldupPointPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of a device. | 
**name** | **str** | LSN device internal name. | 
**area** | **str** | LSN device area. | 
**point_type** | **str** | Point device type. | 
**supports_delayed_reporting** | **bool** | Delayed reporting support. | [optional] 
**walktest_category** | [**LSNWalktestCategoryProperty**](LSNWalktestCategoryProperty.md) |  | [optional] 

## Example

```python
from openapi_client.models.lsn_loop_non_silent_holdup_point_post import LSNLoopNonSilentHoldupPointPost

# TODO update the JSON string below
json = "{}"
# create an instance of LSNLoopNonSilentHoldupPointPost from a JSON string
lsn_loop_non_silent_holdup_point_post_instance = LSNLoopNonSilentHoldupPointPost.from_json(json)
# print the JSON string representation of the object
print(LSNLoopNonSilentHoldupPointPost.to_json())

# convert the object into a dict
lsn_loop_non_silent_holdup_point_post_dict = lsn_loop_non_silent_holdup_point_post_instance.to_dict()
# create an instance of LSNLoopNonSilentHoldupPointPost from a dict
lsn_loop_non_silent_holdup_point_post_from_dict = LSNLoopNonSilentHoldupPointPost.from_dict(lsn_loop_non_silent_holdup_point_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


