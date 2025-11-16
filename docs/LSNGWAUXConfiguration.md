# LSNGWAUXConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | LSN device internal name. | 
**reporting_number** | **int** | LSN device reporting number. | [optional] 
**supports_delayed_reporting** | **bool** | Delayed reporting support. | [optional] 

## Example

```python
from bosch-alarm-map.models.lsngwaux_configuration import LSNGWAUXConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of LSNGWAUXConfiguration from a JSON string
lsngwaux_configuration_instance = LSNGWAUXConfiguration.from_json(json)
# print the JSON string representation of the object
print(LSNGWAUXConfiguration.to_json())

# convert the object into a dict
lsngwaux_configuration_dict = lsngwaux_configuration_instance.to_dict()
# create an instance of LSNGWAUXConfiguration from a dict
lsngwaux_configuration_from_dict = LSNGWAUXConfiguration.from_dict(lsngwaux_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


