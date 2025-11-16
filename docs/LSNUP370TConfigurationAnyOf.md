# LSNUP370TConfigurationAnyOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | LSN device internal name. | 
**area** | **str** | LSN device area. | 
**reporting_number** | **int** | LSN device reporting number. | [optional] 
**antimask_latched** | **bool** | Determines whether the Anti-mask alarm condition will require a reset. | [optional] [default to False]
**antimask_sensitivity** | [**LSNAntimaskSensitivityProperty**](LSNAntimaskSensitivityProperty.md) |  | [optional] [default to LSNAntimaskSensitivityProperty.STANDARD]
**sensitivity_detection_range** | [**LSNAntimaskSensitivityDetectionRangeProperty**](LSNAntimaskSensitivityDetectionRangeProperty.md) |  | [optional] [default to LSNAntimaskSensitivityDetectionRangeProperty.MEDIUM_MINUS__10_METER]

## Example

```python
from bosch_alarm_map.models.lsnup370_t_configuration_any_of import LSNUP370TConfigurationAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of LSNUP370TConfigurationAnyOf from a JSON string
lsnup370_t_configuration_any_of_instance = LSNUP370TConfigurationAnyOf.from_json(json)
# print the JSON string representation of the object
print(LSNUP370TConfigurationAnyOf.to_json())

# convert the object into a dict
lsnup370_t_configuration_any_of_dict = lsnup370_t_configuration_any_of_instance.to_dict()
# create an instance of LSNUP370TConfigurationAnyOf from a dict
lsnup370_t_configuration_any_of_from_dict = LSNUP370TConfigurationAnyOf.from_dict(lsnup370_t_configuration_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


