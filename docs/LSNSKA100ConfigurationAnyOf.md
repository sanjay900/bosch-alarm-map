# LSNSKA100ConfigurationAnyOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | LSN device internal name. | 
**area** | **str** | LSN device area. | 
**reporting_number** | **int** | LSN device reporting number. | [optional] 

## Example

```python
from openapi_client.models.lsnska100_configuration_any_of import LSNSKA100ConfigurationAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of LSNSKA100ConfigurationAnyOf from a JSON string
lsnska100_configuration_any_of_instance = LSNSKA100ConfigurationAnyOf.from_json(json)
# print the JSON string representation of the object
print(LSNSKA100ConfigurationAnyOf.to_json())

# convert the object into a dict
lsnska100_configuration_any_of_dict = lsnska100_configuration_any_of_instance.to_dict()
# create an instance of LSNSKA100ConfigurationAnyOf from a dict
lsnska100_configuration_any_of_from_dict = LSNSKA100ConfigurationAnyOf.from_dict(lsnska100_configuration_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


