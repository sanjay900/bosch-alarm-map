# LSNStdIntr53Configuration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of a device. | 
**name** | **str** | LSN device internal name. | 
**area** | **str** | LSN device area. | 
**point_type** | **str** | Point device type. | 
**supports_delayed_reporting** | **bool** | Delayed reporting support. | [optional] 
**walktest_category** | [**LSNWalktestCategoryProperty**](LSNWalktestCategoryProperty.md) |  | [optional] 
**chime_mode_capable** | **bool** | Controls whether the point can trigger the chime tone on Keypad. | [optional] 
**delay_for_alarm_detection** | **int** | Delay for alarm detection in seconds. | [optional] 
**entry_point** | **str** | Device entry point. | [optional] 
**exit_point** | **str** | Device exit point. | [optional] 
**walktest_trigger_frequency** | [**LSNWalktestTriggerFrequencyProperty**](LSNWalktestTriggerFrequencyProperty.md) |  | [optional] 
**loop_current_index** | **int** | LSN device loop current index. | 
**reporting_number** | **int** | LSN device reporting number. | [optional] 
**antimask_detection** | **bool** | LSN antimask detection status. | [optional] 
**antimask_latched** | **bool** | Determines whether the Anti-mask alarm condition will require a reset. | [optional] [default to False]
**antimask_sensitivity** | [**LSNAntimaskSensitivityProperty**](LSNAntimaskSensitivityProperty.md) |  | [optional] [default to LSNAntimaskSensitivityProperty.STANDARD]
**pir_mode** | **bool** | LSN PIR mode status. | [optional] 
**sensitivity** | [**LSNDetectorSensitivityProperty**](LSNDetectorSensitivityProperty.md) |  | [optional] 

## Example

```python
from bosch_alarm_map.models.lsn_std_intr53_configuration import LSNStdIntr53Configuration

# TODO update the JSON string below
json = "{}"
# create an instance of LSNStdIntr53Configuration from a JSON string
lsn_std_intr53_configuration_instance = LSNStdIntr53Configuration.from_json(json)
# print the JSON string representation of the object
print(LSNStdIntr53Configuration.to_json())

# convert the object into a dict
lsn_std_intr53_configuration_dict = lsn_std_intr53_configuration_instance.to_dict()
# create an instance of LSNStdIntr53Configuration from a dict
lsn_std_intr53_configuration_from_dict = LSNStdIntr53Configuration.from_dict(lsn_std_intr53_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


