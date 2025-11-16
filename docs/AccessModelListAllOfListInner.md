# AccessModelListAllOfListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_model_id** | **str** | Unique name of an Access Model. The name is used to identify the item on the MAP System. The following characters are forbidden by the choose of the identifier name: \&quot; @ ; | 
**access_profile_level** | **int** | Numerical value that determines which users can be edited by users assigned to an Access Profile (4 &#x3D; highest level, 998 &#x3D; lowest level) | [optional] 
**area_and_time_model_list** | **List[str]** | List of Area and Time Model IDs that have beed assign to this access profile  | [optional] 

## Example

```python
from bosch_alarm_map.models.access_model_list_all_of_list_inner import AccessModelListAllOfListInner

# TODO update the JSON string below
json = "{}"
# create an instance of AccessModelListAllOfListInner from a JSON string
access_model_list_all_of_list_inner_instance = AccessModelListAllOfListInner.from_json(json)
# print the JSON string representation of the object
print(AccessModelListAllOfListInner.to_json())

# convert the object into a dict
access_model_list_all_of_list_inner_dict = access_model_list_all_of_list_inner_instance.to_dict()
# create an instance of AccessModelListAllOfListInner from a dict
access_model_list_all_of_list_inner_from_dict = AccessModelListAllOfListInner.from_dict(access_model_list_all_of_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


