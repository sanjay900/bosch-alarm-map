# LSNGWLoopConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | LSN device internal name. | 
**devices** | [**List[LSNGWLoopConfigurationDevicesInner]**](LSNGWLoopConfigurationDevicesInner.md) | List of LSN devices connected to this LSN Loop. | 

## Example

```python
from bosch_alarm_map.models.lsngw_loop_configuration import LSNGWLoopConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of LSNGWLoopConfiguration from a JSON string
lsngw_loop_configuration_instance = LSNGWLoopConfiguration.from_json(json)
# print the JSON string representation of the object
print(LSNGWLoopConfiguration.to_json())

# convert the object into a dict
lsngw_loop_configuration_dict = lsngw_loop_configuration_instance.to_dict()
# create an instance of LSNGWLoopConfiguration from a dict
lsngw_loop_configuration_from_dict = LSNGWLoopConfiguration.from_dict(lsngw_loop_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


