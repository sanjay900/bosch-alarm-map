# InfrastructureDeviceProperties

List of configured properties of a device. Can be empty.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generic** | [**List[InfrastructureDeviceGenericProperty]**](InfrastructureDeviceGenericProperty.md) |  | [optional] 
**rps** | [**List[InfrastructureDeviceRPSProperty]**](InfrastructureDeviceRPSProperty.md) |  | [optional] 

## Example

```python
from bosch-alarm-map.models.infrastructure_device_properties import InfrastructureDeviceProperties

# TODO update the JSON string below
json = "{}"
# create an instance of InfrastructureDeviceProperties from a JSON string
infrastructure_device_properties_instance = InfrastructureDeviceProperties.from_json(json)
# print the JSON string representation of the object
print(InfrastructureDeviceProperties.to_json())

# convert the object into a dict
infrastructure_device_properties_dict = infrastructure_device_properties_instance.to_dict()
# create an instance of InfrastructureDeviceProperties from a dict
infrastructure_device_properties_from_dict = InfrastructureDeviceProperties.from_dict(infrastructure_device_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


