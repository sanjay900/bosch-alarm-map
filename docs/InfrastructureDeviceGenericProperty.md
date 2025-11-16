# InfrastructureDeviceGenericProperty

Parameter of a logical device.  The parameter is represented as name-value pair. The MAP supports up to three values for each parameter, with the first value being mandatory and the other two being optional. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Parameter name | [optional] 
**value** | **str** | Parameter value (required) | [optional] 
**second_value** | **str** | Parameter second value (optional) | [optional] 
**third_value** | **str** | Parameter third value (optional) | [optional] 

## Example

```python
from openapi_client.models.infrastructure_device_generic_property import InfrastructureDeviceGenericProperty

# TODO update the JSON string below
json = "{}"
# create an instance of InfrastructureDeviceGenericProperty from a JSON string
infrastructure_device_generic_property_instance = InfrastructureDeviceGenericProperty.from_json(json)
# print the JSON string representation of the object
print(InfrastructureDeviceGenericProperty.to_json())

# convert the object into a dict
infrastructure_device_generic_property_dict = infrastructure_device_generic_property_instance.to_dict()
# create an instance of InfrastructureDeviceGenericProperty from a dict
infrastructure_device_generic_property_from_dict = InfrastructureDeviceGenericProperty.from_dict(infrastructure_device_generic_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


