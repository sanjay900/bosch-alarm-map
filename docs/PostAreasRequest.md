# PostAreasRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** |  | [optional] 
**bypass_off_normal_devices** | **bool** | Bypass all devices that are off normal before arming. | [optional] 
**exit_delay** | **str** | Defines whether the arming should happen without a delay (zero) with the user configured default exit delay or with the extended exit delay as configured for the area. | [optional] 
**included_points** | **str** | Specifies which points should be put into test mode. | [optional] 

## Example

```python
from bosch_alarm_map.models.post_areas_request import PostAreasRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAreasRequest from a JSON string
post_areas_request_instance = PostAreasRequest.from_json(json)
# print the JSON string representation of the object
print(PostAreasRequest.to_json())

# convert the object into a dict
post_areas_request_dict = post_areas_request_instance.to_dict()
# create an instance of PostAreasRequest from a dict
post_areas_request_from_dict = PostAreasRequest.from_dict(post_areas_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


