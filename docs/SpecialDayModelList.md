# SpecialDayModelList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**special_day_model_sync_id** | **int** | Synchronization ID for the special day database table. Will be changed for each change in the special day database table. | 
**list** | [**List[SpecialDayModelListAllOfListInner]**](SpecialDayModelListAllOfListInner.md) | List of all special day models | [optional] 

## Example

```python
from bosch-alarm-map.models.special_day_model_list import SpecialDayModelList

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialDayModelList from a JSON string
special_day_model_list_instance = SpecialDayModelList.from_json(json)
# print the JSON string representation of the object
print(SpecialDayModelList.to_json())

# convert the object into a dict
special_day_model_list_dict = special_day_model_list_instance.to_dict()
# create an instance of SpecialDayModelList from a dict
special_day_model_list_from_dict = SpecialDayModelList.from_dict(special_day_model_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


