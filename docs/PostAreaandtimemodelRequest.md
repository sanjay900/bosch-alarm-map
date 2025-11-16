# PostAreaandtimemodelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** |  | 
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
from openapi_client.models.post_areaandtimemodel_request import PostAreaandtimemodelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAreaandtimemodelRequest from a JSON string
post_areaandtimemodel_request_instance = PostAreaandtimemodelRequest.from_json(json)
# print the JSON string representation of the object
print(PostAreaandtimemodelRequest.to_json())

# convert the object into a dict
post_areaandtimemodel_request_dict = post_areaandtimemodel_request_instance.to_dict()
# create an instance of PostAreaandtimemodelRequest from a dict
post_areaandtimemodel_request_from_dict = PostAreaandtimemodelRequest.from_dict(post_areaandtimemodel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


