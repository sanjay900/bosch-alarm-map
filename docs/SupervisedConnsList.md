# SupervisedConnsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**list** | [**List[GetSupervisedConnsSIID200Response]**](GetSupervisedConnsSIID200Response.md) | List of all supervised connections | [optional] 

## Example

```python
from bosch-alarm-map.models.supervised_conns_list import SupervisedConnsList

# TODO update the JSON string below
json = "{}"
# create an instance of SupervisedConnsList from a JSON string
supervised_conns_list_instance = SupervisedConnsList.from_json(json)
# print the JSON string representation of the object
print(SupervisedConnsList.to_json())

# convert the object into a dict
supervised_conns_list_dict = supervised_conns_list_instance.to_dict()
# create an instance of SupervisedConnsList from a dict
supervised_conns_list_from_dict = SupervisedConnsList.from_dict(supervised_conns_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


