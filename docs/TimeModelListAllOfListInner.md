# TimeModelListAllOfListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_model_id** | **str** | Unique Name of the Time model. The name is used to identify the item on the MAP System. The following characters are forbidden in identifier name: \&quot; @ ;  | 
**reference_date** | **str** | starting date of the Time model | [optional] 
**ignore_special_days** | **bool** | When set, the time model is active on special days. Special days are then ignored. | [optional] 
**period_in_days** | [**List[TimeModelPeriodInDaysInner]**](TimeModelPeriodInDaysInner.md) | The number of days in a Period for a Time Model. | [optional] 
**special_days** | **List[str]** | List of Special Days. | [optional] 

## Example

```python
from openapi_client.models.time_model_list_all_of_list_inner import TimeModelListAllOfListInner

# TODO update the JSON string below
json = "{}"
# create an instance of TimeModelListAllOfListInner from a JSON string
time_model_list_all_of_list_inner_instance = TimeModelListAllOfListInner.from_json(json)
# print the JSON string representation of the object
print(TimeModelListAllOfListInner.to_json())

# convert the object into a dict
time_model_list_all_of_list_inner_dict = time_model_list_all_of_list_inner_instance.to_dict()
# create an instance of TimeModelListAllOfListInner from a dict
time_model_list_all_of_list_inner_from_dict = TimeModelListAllOfListInner.from_dict(time_model_list_all_of_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


