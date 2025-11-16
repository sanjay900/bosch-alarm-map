# LSNStdIntr54Configuration


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
**sensitivity** | [**LSNDetectorSensitivityProperty**](LSNDetectorSensitivityProperty.md) |  | [optional] 

## Example

```python
from openapi_client.models.lsn_std_intr54_configuration import LSNStdIntr54Configuration

# TODO update the JSON string below
json = "{}"
# create an instance of LSNStdIntr54Configuration from a JSON string
lsn_std_intr54_configuration_instance = LSNStdIntr54Configuration.from_json(json)
# print the JSON string representation of the object
print(LSNStdIntr54Configuration.to_json())

# convert the object into a dict
lsn_std_intr54_configuration_dict = lsn_std_intr54_configuration_instance.to_dict()
# create an instance of LSNStdIntr54Configuration from a dict
lsn_std_intr54_configuration_from_dict = LSNStdIntr54Configuration.from_dict(lsn_std_intr54_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


