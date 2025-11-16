# GetAccessmodel200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_model_id** | **str** | Unique name of an Access Model. The name is used to identify the item on the MAP System. The following characters are forbidden by the choose of the identifier name: \&quot; @ ; | 
**access_profile_level** | **int** | Numerical value that determines which users can be edited by users assigned to an Access Profile (4 &#x3D; highest level, 998 &#x3D; lowest level) | [optional] 
**area_and_time_model_list** | **List[str]** | List of Area and Time Model IDs that have beed assign to this access profile  | [optional] 
**access_model_sync_id** | **int** | Synchronization ID for the access table. Will be changed for each change in the access database table. | 

## Example

```python
from bosch-alarm-map.models.get_accessmodel200_response import GetAccessmodel200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccessmodel200Response from a JSON string
get_accessmodel200_response_instance = GetAccessmodel200Response.from_json(json)
# print the JSON string representation of the object
print(GetAccessmodel200Response.to_json())

# convert the object into a dict
get_accessmodel200_response_dict = get_accessmodel200_response_instance.to_dict()
# create an instance of GetAccessmodel200Response from a dict
get_accessmodel200_response_from_dict = GetAccessmodel200Response.from_dict(get_accessmodel200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


