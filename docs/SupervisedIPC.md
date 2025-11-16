# SupervisedIPC


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**enabled** | **bool** | True if device is currently enabled, otherwise false. | [optional] 
**incs** | **List[str]** | A list of incidents that relate to the supervised connection. | [optional] 
**path** | **str** | Indicates the IPC communication path | [optional] 

## Example

```python
from openapi_client.models.supervised_ipc import SupervisedIPC

# TODO update the JSON string below
json = "{}"
# create an instance of SupervisedIPC from a JSON string
supervised_ipc_instance = SupervisedIPC.from_json(json)
# print the JSON string representation of the object
print(SupervisedIPC.to_json())

# convert the object into a dict
supervised_ipc_dict = supervised_ipc_instance.to_dict()
# create an instance of SupervisedIPC from a dict
supervised_ipc_from_dict = SupervisedIPC.from_dict(supervised_ipc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


