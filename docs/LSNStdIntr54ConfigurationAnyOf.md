# LSNStdIntr54ConfigurationAnyOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | LSN device internal name. | 
**area** | **str** | LSN device area. | 
**loop_current_index** | **int** | LSN device loop current index. | 
**reporting_number** | **int** | LSN device reporting number. | [optional] 
**sensitivity** | [**LSNDetectorSensitivityProperty**](LSNDetectorSensitivityProperty.md) |  | [optional] 

## Example

```python
from bosch_alarm_map.models.lsn_std_intr54_configuration_any_of import LSNStdIntr54ConfigurationAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of LSNStdIntr54ConfigurationAnyOf from a JSON string
lsn_std_intr54_configuration_any_of_instance = LSNStdIntr54ConfigurationAnyOf.from_json(json)
# print the JSON string representation of the object
print(LSNStdIntr54ConfigurationAnyOf.to_json())

# convert the object into a dict
lsn_std_intr54_configuration_any_of_dict = lsn_std_intr54_configuration_any_of_instance.to_dict()
# create an instance of LSNStdIntr54ConfigurationAnyOf from a dict
lsn_std_intr54_configuration_any_of_from_dict = LSNStdIntr54ConfigurationAnyOf.from_dict(lsn_std_intr54_configuration_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


