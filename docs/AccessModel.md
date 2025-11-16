# AccessModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_profile_level** | **int** | Numerical value that determines which users can be edited by users assigned to an Access Profile (4 &#x3D; highest level, 998 &#x3D; lowest level) | [optional] 
**area_and_time_model_list** | **List[str]** | List of Area and Time Model IDs that have beed assign to this access profile  | [optional] 

## Example

```python
from bosch-alarm-map.models.access_model import AccessModel

# TODO update the JSON string below
json = "{}"
# create an instance of AccessModel from a JSON string
access_model_instance = AccessModel.from_json(json)
# print the JSON string representation of the object
print(AccessModel.to_json())

# convert the object into a dict
access_model_dict = access_model_instance.to_dict()
# create an instance of AccessModel from a dict
access_model_from_dict = AccessModel.from_dict(access_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


