# LSNLoopNonBypassableTechnicalPointPost


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
from openapi_client.models.lsn_loop_non_bypassable_technical_point_post import LSNLoopNonBypassableTechnicalPointPost

# TODO update the JSON string below
json = "{}"
# create an instance of LSNLoopNonBypassableTechnicalPointPost from a JSON string
lsn_loop_non_bypassable_technical_point_post_instance = LSNLoopNonBypassableTechnicalPointPost.from_json(json)
# print the JSON string representation of the object
print(LSNLoopNonBypassableTechnicalPointPost.to_json())

# convert the object into a dict
lsn_loop_non_bypassable_technical_point_post_dict = lsn_loop_non_bypassable_technical_point_post_instance.to_dict()
# create an instance of LSNLoopNonBypassableTechnicalPointPost from a dict
lsn_loop_non_bypassable_technical_point_post_from_dict = LSNLoopNonBypassableTechnicalPointPost.from_dict(lsn_loop_non_bypassable_technical_point_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


