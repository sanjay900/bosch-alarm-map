# LSNLoopLatchingBypassableTechnicalPointPost


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
from bosch-alarm-map.models.lsn_loop_latching_bypassable_technical_point_post import LSNLoopLatchingBypassableTechnicalPointPost

# TODO update the JSON string below
json = "{}"
# create an instance of LSNLoopLatchingBypassableTechnicalPointPost from a JSON string
lsn_loop_latching_bypassable_technical_point_post_instance = LSNLoopLatchingBypassableTechnicalPointPost.from_json(json)
# print the JSON string representation of the object
print(LSNLoopLatchingBypassableTechnicalPointPost.to_json())

# convert the object into a dict
lsn_loop_latching_bypassable_technical_point_post_dict = lsn_loop_latching_bypassable_technical_point_post_instance.to_dict()
# create an instance of LSNLoopLatchingBypassableTechnicalPointPost from a dict
lsn_loop_latching_bypassable_technical_point_post_from_dict = LSNLoopLatchingBypassableTechnicalPointPost.from_dict(lsn_loop_latching_bypassable_technical_point_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


