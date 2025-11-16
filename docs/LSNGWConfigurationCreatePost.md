# LSNGWConfigurationCreatePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection** | **str** | Specifies the port where the device is connected to. | 
**name** | **str** | LSN GW device internal name. | 
**area** | **str** | Area of the device. | 
**serial_number** | **str** | Product ID (serial number) of the device. | 
**reporting_number** | **int** | LSN device reporting number. | [optional] 
**bus_mode** | **str** | Bus mode of the device. | [optional] 
**supports_delayed_reporting** | **bool** | Delayed reporting support. | [optional] 
**consider_device_missing_as_alarm** | **bool** | If set to true, missing device will be considered as alarm. | [optional] 
**consider_loop_failure_as_tamper_in_armed_condition** | **bool** | If set to true, any loop error will be considered as tamper alarm. | [optional] 
**consider_loop_failure_as_tamper_in_disarmed_condition** | **bool** | If set to true, any loop error will be considered as tamper alarm. | [optional] 
**loop_failure_indication** | [**LSNLoopFailureIndicationProperty**](LSNLoopFailureIndicationProperty.md) |  | [optional] 
**aux** | [**List[LSNGWAUXConfiguration]**](LSNGWAUXConfiguration.md) | List of AUX power devices related to this LSN GW. | 
**loop** | [**LSNGWLoopConfiguration**](LSNGWLoopConfiguration.md) | List of the loop devices connected to this LSN GW. | 
**cmd** | **str** | POST request command. | 

## Example

```python
from bosch_alarm_map.models.lsngw_configuration_create_post import LSNGWConfigurationCreatePost

# TODO update the JSON string below
json = "{}"
# create an instance of LSNGWConfigurationCreatePost from a JSON string
lsngw_configuration_create_post_instance = LSNGWConfigurationCreatePost.from_json(json)
# print the JSON string representation of the object
print(LSNGWConfigurationCreatePost.to_json())

# convert the object into a dict
lsngw_configuration_create_post_dict = lsngw_configuration_create_post_instance.to_dict()
# create an instance of LSNGWConfigurationCreatePost from a dict
lsngw_configuration_create_post_from_dict = LSNGWConfigurationCreatePost.from_dict(lsngw_configuration_create_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


