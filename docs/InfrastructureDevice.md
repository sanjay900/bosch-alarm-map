# InfrastructureDevice

Device that is physically connected to the MAP.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Device configured name. Usually related to device type, but can be changed to anything via RPS. | [optional] 
**type** | [**InfrastructureDeviceSIType**](InfrastructureDeviceSIType.md) |  | [optional] 
**siid** | **str** | Security Identifier (SI) ID that is used internally to communicate with the device. | [optional] 
**properties** | [**InfrastructureDeviceProperties**](InfrastructureDeviceProperties.md) |  | [optional] 
**devices** | [**List[InfrastructureDevice]**](InfrastructureDevice.md) | List of sub-devices physically connected to this device. Can be empty. | [optional] 

## Example

```python
from bosch-alarm-map.models.infrastructure_device import InfrastructureDevice

# TODO update the JSON string below
json = "{}"
# create an instance of InfrastructureDevice from a JSON string
infrastructure_device_instance = InfrastructureDevice.from_json(json)
# print the JSON string representation of the object
print(InfrastructureDevice.to_json())

# convert the object into a dict
infrastructure_device_dict = infrastructure_device_instance.to_dict()
# create an instance of InfrastructureDevice from a dict
infrastructure_device_from_dict = InfrastructureDevice.from_dict(infrastructure_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


