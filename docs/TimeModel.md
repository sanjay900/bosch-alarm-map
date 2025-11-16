# TimeModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_date** | **str** | starting date of the Time model | [optional] 
**ignore_special_days** | **bool** | When set, the time model is active on special days. Special days are then ignored. | [optional] 
**period_in_days** | [**List[TimeModelPeriodInDaysInner]**](TimeModelPeriodInDaysInner.md) | The number of days in a Period for a Time Model. | [optional] 
**special_days** | **List[str]** | List of Special Days. | [optional] 

## Example

```python
from bosch-alarm-map.models.time_model import TimeModel

# TODO update the JSON string below
json = "{}"
# create an instance of TimeModel from a JSON string
time_model_instance = TimeModel.from_json(json)
# print the JSON string representation of the object
print(TimeModel.to_json())

# convert the object into a dict
time_model_dict = time_model_instance.to_dict()
# create an instance of TimeModel from a dict
time_model_from_dict = TimeModel.from_dict(time_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


