# AreaAndTimeModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**always_allowed_permission_set** | **str** | The access permission level always granted to the user. | [optional] 
**restricted_by_area_permission_set** | **str** | This Parameter determines whether the user is restricted by an area permission set. | [optional] 
**restricted_by_time_permission_set** | **str** | This Parameter determines whether the user is restricted by a time permission set. | [optional] 
**restricted_by_area_and_time_permission_set** | **str** | This Parameter determines whether the user is restricted by an area and time permission set. | [optional] 
**area_list** | **List[str]** | List of areas related to the scheduled action. | [optional] 
**time_model_id** | **str** | Related time model to schedule an action. | [optional] 

## Example

```python
from openapi_client.models.area_and_time_model import AreaAndTimeModel

# TODO update the JSON string below
json = "{}"
# create an instance of AreaAndTimeModel from a JSON string
area_and_time_model_instance = AreaAndTimeModel.from_json(json)
# print the JSON string representation of the object
print(AreaAndTimeModel.to_json())

# convert the object into a dict
area_and_time_model_dict = area_and_time_model_instance.to_dict()
# create an instance of AreaAndTimeModel from a dict
area_and_time_model_from_dict = AreaAndTimeModel.from_dict(area_and_time_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


