# LSNUP370TConfiguration


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
**reporting_number** | **int** | LSN device reporting number. | [optional] 
**antimask_latched** | **bool** | Determines whether the Anti-mask alarm condition will require a reset. | [optional] [default to False]
**antimask_sensitivity** | [**LSNAntimaskSensitivityProperty**](LSNAntimaskSensitivityProperty.md) |  | [optional] [default to LSNAntimaskSensitivityProperty.STANDARD]
**sensitivity_detection_range** | [**LSNAntimaskSensitivityDetectionRangeProperty**](LSNAntimaskSensitivityDetectionRangeProperty.md) |  | [optional] [default to LSNAntimaskSensitivityDetectionRangeProperty.MEDIUM_MINUS__10_METER]

## Example

```python
from openapi_client.models.lsnup370_t_configuration import LSNUP370TConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of LSNUP370TConfiguration from a JSON string
lsnup370_t_configuration_instance = LSNUP370TConfiguration.from_json(json)
# print the JSON string representation of the object
print(LSNUP370TConfiguration.to_json())

# convert the object into a dict
lsnup370_t_configuration_dict = lsnup370_t_configuration_instance.to_dict()
# create an instance of LSNUP370TConfiguration from a dict
lsnup370_t_configuration_from_dict = LSNUP370TConfiguration.from_dict(lsnup370_t_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


