# LSNND200ConfigurationAnyOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | LSN device internal name. | 
**area** | **str** | LSN device area. | 
**reporting_number** | **int** | LSN device reporting number. | [optional] 

## Example

```python
from bosch_alarm_map.models.lsnnd200_configuration_any_of import LSNND200ConfigurationAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of LSNND200ConfigurationAnyOf from a JSON string
lsnnd200_configuration_any_of_instance = LSNND200ConfigurationAnyOf.from_json(json)
# print the JSON string representation of the object
print(LSNND200ConfigurationAnyOf.to_json())

# convert the object into a dict
lsnnd200_configuration_any_of_dict = lsnnd200_configuration_any_of_instance.to_dict()
# create an instance of LSNND200ConfigurationAnyOf from a dict
lsnnd200_configuration_any_of_from_dict = LSNND200ConfigurationAnyOf.from_dict(lsnnd200_configuration_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


