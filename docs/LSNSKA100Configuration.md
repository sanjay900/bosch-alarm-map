# LSNSKA100Configuration


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

## Example

```python
from openapi_client.models.lsnska100_configuration import LSNSKA100Configuration

# TODO update the JSON string below
json = "{}"
# create an instance of LSNSKA100Configuration from a JSON string
lsnska100_configuration_instance = LSNSKA100Configuration.from_json(json)
# print the JSON string representation of the object
print(LSNSKA100Configuration.to_json())

# convert the object into a dict
lsnska100_configuration_dict = lsnska100_configuration_instance.to_dict()
# create an instance of LSNSKA100Configuration from a dict
lsnska100_configuration_from_dict = LSNSKA100Configuration.from_dict(lsnska100_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


