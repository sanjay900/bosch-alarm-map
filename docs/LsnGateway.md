# LsnGateway


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**op_state** | [**DeviceOpState**](DeviceOpState.md) |  | [optional] 
**enabled** | **bool** | True if device is currently enabled, otherwise false. | [optional] 
**incs** | **List[str]** | A list of incidents that relate to this device. In case the opState is MALFUNCTION the incident will give more detailed information about the error condition the device is in. | [optional] 

## Example

```python
from openapi_client.models.lsn_gateway import LsnGateway

# TODO update the JSON string below
json = "{}"
# create an instance of LsnGateway from a JSON string
lsn_gateway_instance = LsnGateway.from_json(json)
# print the JSON string representation of the object
print(LsnGateway.to_json())

# convert the object into a dict
lsn_gateway_dict = lsn_gateway_instance.to_dict()
# create an instance of LsnGateway from a dict
lsn_gateway_from_dict = LsnGateway.from_dict(lsn_gateway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


