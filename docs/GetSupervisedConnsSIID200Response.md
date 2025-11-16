# GetSupervisedConnsSIID200Response


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
from openapi_client.models.get_supervised_conns_siid200_response import GetSupervisedConnsSIID200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSupervisedConnsSIID200Response from a JSON string
get_supervised_conns_siid200_response_instance = GetSupervisedConnsSIID200Response.from_json(json)
# print the JSON string representation of the object
print(GetSupervisedConnsSIID200Response.to_json())

# convert the object into a dict
get_supervised_conns_siid200_response_dict = get_supervised_conns_siid200_response_instance.to_dict()
# create an instance of GetSupervisedConnsSIID200Response from a dict
get_supervised_conns_siid200_response_from_dict = GetSupervisedConnsSIID200Response.from_dict(get_supervised_conns_siid200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


