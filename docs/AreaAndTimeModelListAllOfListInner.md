# AreaAndTimeModelListAllOfListInner


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

## Example

```python
from bosch_alarm_map.models.area_and_time_model_list_all_of_list_inner import AreaAndTimeModelListAllOfListInner

# TODO update the JSON string below
json = "{}"
# create an instance of AreaAndTimeModelListAllOfListInner from a JSON string
area_and_time_model_list_all_of_list_inner_instance = AreaAndTimeModelListAllOfListInner.from_json(json)
# print the JSON string representation of the object
print(AreaAndTimeModelListAllOfListInner.to_json())

# convert the object into a dict
area_and_time_model_list_all_of_list_inner_dict = area_and_time_model_list_all_of_list_inner_instance.to_dict()
# create an instance of AreaAndTimeModelListAllOfListInner from a dict
area_and_time_model_list_all_of_list_inner_from_dict = AreaAndTimeModelListAllOfListInner.from_dict(area_and_time_model_list_all_of_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


