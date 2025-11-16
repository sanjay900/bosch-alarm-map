# DayModelID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_model_id** | **str** | Unique name of a DayModel. The name is used to identify the item on the MAP System. The following characters are forbidden in identifier name: \&quot; @ ;  | 

## Example

```python
from bosch-alarm-map.models.day_model_id import DayModelID

# TODO update the JSON string below
json = "{}"
# create an instance of DayModelID from a JSON string
day_model_id_instance = DayModelID.from_json(json)
# print the JSON string representation of the object
print(DayModelID.to_json())

# convert the object into a dict
day_model_id_dict = day_model_id_instance.to_dict()
# create an instance of DayModelID from a dict
day_model_id_from_dict = DayModelID.from_dict(day_model_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


