# TimeModelPeriodInDaysInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_model_id** | **str** | Name of an existing day model | [optional] 
**priority** | **int** |  | [optional] 

## Example

```python
from bosch_alarm_map.models.time_model_period_in_days_inner import TimeModelPeriodInDaysInner

# TODO update the JSON string below
json = "{}"
# create an instance of TimeModelPeriodInDaysInner from a JSON string
time_model_period_in_days_inner_instance = TimeModelPeriodInDaysInner.from_json(json)
# print the JSON string representation of the object
print(TimeModelPeriodInDaysInner.to_json())

# convert the object into a dict
time_model_period_in_days_inner_dict = time_model_period_in_days_inner_instance.to_dict()
# create an instance of TimeModelPeriodInDaysInner from a dict
time_model_period_in_days_inner_from_dict = TimeModelPeriodInDaysInner.from_dict(time_model_period_in_days_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


