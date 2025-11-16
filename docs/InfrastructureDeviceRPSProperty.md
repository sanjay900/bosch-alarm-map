# InfrastructureDeviceRPSProperty

RPS specific parameter of a logical device.  The parameter is represented as name-value pair. The MAP supports up to three values for each parameter, with the first value being mandatory and the other two being optional. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Parameter name | [optional] 
**value** | **str** | Parameter value (required) | [optional] 

## Example

```python
from openapi_client.models.infrastructure_device_rps_property import InfrastructureDeviceRPSProperty

# TODO update the JSON string below
json = "{}"
# create an instance of InfrastructureDeviceRPSProperty from a JSON string
infrastructure_device_rps_property_instance = InfrastructureDeviceRPSProperty.from_json(json)
# print the JSON string representation of the object
print(InfrastructureDeviceRPSProperty.to_json())

# convert the object into a dict
infrastructure_device_rps_property_dict = infrastructure_device_rps_property_instance.to_dict()
# create an instance of InfrastructureDeviceRPSProperty from a dict
infrastructure_device_rps_property_from_dict = InfrastructureDeviceRPSProperty.from_dict(infrastructure_device_rps_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


