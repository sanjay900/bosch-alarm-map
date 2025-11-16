# GetAreaandtimemodel200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area_and_time_model_id** | **str** | The Unique name of a AreaandTimeModel. The name is used to identify the item on the MAP system.The following characters are forbidden in identifier name: \&quot; @ ;  | 
**always_allowed_permission_set** | **str** | The access permission level always granted to the user. | [optional] 
**restricted_by_area_permission_set** | **str** | This Parameter determines whether the user is restricted by an area permission set. | [optional] 
**restricted_by_time_permission_set** | **str** | This Parameter determines whether the user is restricted by a time permission set. | [optional] 
**restricted_by_area_and_time_permission_set** | **str** | This Parameter determines whether the user is restricted by an area and time permission set. | [optional] 
**area_list** | **List[str]** | List of areas related to the scheduled action. | [optional] 
**time_model_id** | **str** | Related time model to schedule an action. | [optional] 
**area_and_time_model_sync_id** | **int** | Synchronization ID for the area and time table. Will be changed for each change in the area and time database table. | 

## Example

```python
from bosch-alarm-map.models.get_areaandtimemodel200_response import GetAreaandtimemodel200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAreaandtimemodel200Response from a JSON string
get_areaandtimemodel200_response_instance = GetAreaandtimemodel200Response.from_json(json)
# print the JSON string representation of the object
print(GetAreaandtimemodel200Response.to_json())

# convert the object into a dict
get_areaandtimemodel200_response_dict = get_areaandtimemodel200_response_instance.to_dict()
# create an instance of GetAreaandtimemodel200Response from a dict
get_areaandtimemodel200_response_from_dict = GetAreaandtimemodel200Response.from_dict(get_areaandtimemodel200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


