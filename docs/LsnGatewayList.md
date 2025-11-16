# LsnGatewayList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**list** | [**List[LsnGateway]**](LsnGateway.md) | List of all lsnGateways | [optional] 

## Example

```python
from bosch-alarm-map.models.lsn_gateway_list import LsnGatewayList

# TODO update the JSON string below
json = "{}"
# create an instance of LsnGatewayList from a JSON string
lsn_gateway_list_instance = LsnGatewayList.from_json(json)
# print the JSON string representation of the object
print(LsnGatewayList.to_json())

# convert the object into a dict
lsn_gateway_list_dict = lsn_gateway_list_instance.to_dict()
# create an instance of LsnGatewayList from a dict
lsn_gateway_list_from_dict = LsnGatewayList.from_dict(lsn_gateway_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


