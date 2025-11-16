# SupervisedConns


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**enabled** | **bool** | True if device is currently enabled, otherwise false. | [optional] 
**incs** | **List[str]** | A list of incidents that relate to the supervised connection. | [optional] 

## Example

```python
from openapi_client.models.supervised_conns import SupervisedConns

# TODO update the JSON string below
json = "{}"
# create an instance of SupervisedConns from a JSON string
supervised_conns_instance = SupervisedConns.from_json(json)
# print the JSON string representation of the object
print(SupervisedConns.to_json())

# convert the object into a dict
supervised_conns_dict = supervised_conns_instance.to_dict()
# create an instance of SupervisedConns from a dict
supervised_conns_from_dict = SupervisedConns.from_dict(supervised_conns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


