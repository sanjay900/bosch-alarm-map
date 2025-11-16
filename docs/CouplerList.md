# CouplerList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**list** | [**List[Coupler]**](Coupler.md) | List of all couplers | [optional] 

## Example

```python
from openapi_client.models.coupler_list import CouplerList

# TODO update the JSON string below
json = "{}"
# create an instance of CouplerList from a JSON string
coupler_list_instance = CouplerList.from_json(json)
# print the JSON string representation of the object
print(CouplerList.to_json())

# convert the object into a dict
coupler_list_dict = coupler_list_instance.to_dict()
# create an instance of CouplerList from a dict
coupler_list_from_dict = CouplerList.from_dict(coupler_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


