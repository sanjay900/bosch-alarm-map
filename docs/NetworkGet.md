# NetworkGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** |  | [optional] 
**dhcp** | **bool** |  | [optional] 
**ipv4_address** | **str** | Current IP address of the device | [optional] 
**ipv4_netmask** | **str** | Current subnet mask used by the device | [optional] 
**ipv4_gateway** | **str** | Current default gateway used by the device | [optional] 

## Example

```python
from bosch-alarm-map.models.network_get import NetworkGet

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkGet from a JSON string
network_get_instance = NetworkGet.from_json(json)
# print the JSON string representation of the object
print(NetworkGet.to_json())

# convert the object into a dict
network_get_dict = network_get_instance.to_dict()
# create an instance of NetworkGet from a dict
network_get_from_dict = NetworkGet.from_dict(network_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


