# PostTimemodelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** |  | 
**time_model_id** | **str** | Unique Name of the Time model. The name is used to identify the item on the MAP System. The following characters are forbidden in identifier name: \&quot; @ ;  | 
**reference_date** | **str** | starting date of the Time model | [optional] 
**ignore_special_days** | **bool** | When set, the time model is active on special days. Special days are then ignored. | [optional] 
**period_in_days** | [**List[TimeModelPeriodInDaysInner]**](TimeModelPeriodInDaysInner.md) | The number of days in a Period for a Time Model. | [optional] 
**special_days** | **List[str]** | List of Special Days. | [optional] 
**time_model_sync_id** | **int** | Synchronization ID for the time database table. Will be changed for each change in the time database table. | [optional] 

## Example

```python
from bosch-alarm-map.models.post_timemodel_request import PostTimemodelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostTimemodelRequest from a JSON string
post_timemodel_request_instance = PostTimemodelRequest.from_json(json)
# print the JSON string representation of the object
print(PostTimemodelRequest.to_json())

# convert the object into a dict
post_timemodel_request_dict = post_timemodel_request_instance.to_dict()
# create an instance of PostTimemodelRequest from a dict
post_timemodel_request_from_dict = PostTimemodelRequest.from_dict(post_timemodel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


