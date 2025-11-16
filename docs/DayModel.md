# DayModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **List[str]** | Define up to three timezones of the Daymodel. | [optional] 

## Example

```python
from openapi_client.models.day_model import DayModel

# TODO update the JSON string below
json = "{}"
# create an instance of DayModel from a JSON string
day_model_instance = DayModel.from_json(json)
# print the JSON string representation of the object
print(DayModel.to_json())

# convert the object into a dict
day_model_dict = day_model_instance.to_dict()
# create an instance of DayModel from a dict
day_model_from_dict = DayModel.from_dict(day_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


