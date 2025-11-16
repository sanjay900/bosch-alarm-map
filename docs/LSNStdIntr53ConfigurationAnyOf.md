# LSNStdIntr53ConfigurationAnyOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | LSN device internal name. | 
**area** | **str** | LSN device area. | 
**loop_current_index** | **int** | LSN device loop current index. | 
**reporting_number** | **int** | LSN device reporting number. | [optional] 
**antimask_detection** | **bool** | LSN antimask detection status. | [optional] 
**antimask_latched** | **bool** | Determines whether the Anti-mask alarm condition will require a reset. | [optional] [default to False]
**antimask_sensitivity** | [**LSNAntimaskSensitivityProperty**](LSNAntimaskSensitivityProperty.md) |  | [optional] [default to LSNAntimaskSensitivityProperty.STANDARD]
**pir_mode** | **bool** | LSN PIR mode status. | [optional] 
**sensitivity** | [**LSNDetectorSensitivityProperty**](LSNDetectorSensitivityProperty.md) |  | [optional] 

## Example

```python
from openapi_client.models.lsn_std_intr53_configuration_any_of import LSNStdIntr53ConfigurationAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of LSNStdIntr53ConfigurationAnyOf from a JSON string
lsn_std_intr53_configuration_any_of_instance = LSNStdIntr53ConfigurationAnyOf.from_json(json)
# print the JSON string representation of the object
print(LSNStdIntr53ConfigurationAnyOf.to_json())

# convert the object into a dict
lsn_std_intr53_configuration_any_of_dict = lsn_std_intr53_configuration_any_of_instance.to_dict()
# create an instance of LSNStdIntr53ConfigurationAnyOf from a dict
lsn_std_intr53_configuration_any_of_from_dict = LSNStdIntr53ConfigurationAnyOf.from_dict(lsn_std_intr53_configuration_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


