# Config


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **List[str]** | Fixed type identifier | [optional] 
**var_self** | **str** | Link to the current resource | [optional] 
**area_configuration** | [**AreaConfiguration**](AreaConfiguration.md) | An array of area configuration objects. | [optional] 
**internal_programs_configuration** | [**InternalProgramsConfiguration**](InternalProgramsConfiguration.md) | An array of internal program configuration objects. | [optional] 
**device_configuration** | [**DeviceConfiguration**](DeviceConfiguration.md) | An array of device configuration objects. | [optional] 

## Example

```python
from openapi_client.models.config import Config

# TODO update the JSON string below
json = "{}"
# create an instance of Config from a JSON string
config_instance = Config.from_json(json)
# print the JSON string representation of the object
print(Config.to_json())

# convert the object into a dict
config_dict = config_instance.to_dict()
# create an instance of Config from a dict
config_from_dict = Config.from_dict(config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


