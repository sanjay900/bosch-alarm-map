# DayModelListAllOfListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_model_id** | **str** | Unique name of a DayModel. The name is used to identify the item on the MAP System. The following characters are forbidden in identifier name: \&quot; @ ;  | 
**interval** | **List[str]** | Define up to three timezones of the Daymodel. | [optional] 

## Example

```python
from bosch_alarm_map.models.day_model_list_all_of_list_inner import DayModelListAllOfListInner

# TODO update the JSON string below
json = "{}"
# create an instance of DayModelListAllOfListInner from a JSON string
day_model_list_all_of_list_inner_instance = DayModelListAllOfListInner.from_json(json)
# print the JSON string representation of the object
print(DayModelListAllOfListInner.to_json())

# convert the object into a dict
day_model_list_all_of_list_inner_dict = day_model_list_all_of_list_inner_instance.to_dict()
# create an instance of DayModelListAllOfListInner from a dict
day_model_list_all_of_list_inner_from_dict = DayModelListAllOfListInner.from_dict(day_model_list_all_of_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


