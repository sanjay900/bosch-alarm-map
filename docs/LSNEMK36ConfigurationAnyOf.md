# LSNEMK36ConfigurationAnyOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | LSN device internal name. | 
**area** | **str** | LSN device area. | 
**reporting_number** | **int** | LSN device reporting number. | [optional] 
**walktest_trigger_frequency** | [**LSNWalktestTriggerFrequencyProperty**](LSNWalktestTriggerFrequencyProperty.md) |  | [optional] 

## Example

```python
from openapi_client.models.lsnemk36_configuration_any_of import LSNEMK36ConfigurationAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of LSNEMK36ConfigurationAnyOf from a JSON string
lsnemk36_configuration_any_of_instance = LSNEMK36ConfigurationAnyOf.from_json(json)
# print the JSON string representation of the object
print(LSNEMK36ConfigurationAnyOf.to_json())

# convert the object into a dict
lsnemk36_configuration_any_of_dict = lsnemk36_configuration_any_of_instance.to_dict()
# create an instance of LSNEMK36ConfigurationAnyOf from a dict
lsnemk36_configuration_any_of_from_dict = LSNEMK36ConfigurationAnyOf.from_dict(lsnemk36_configuration_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


