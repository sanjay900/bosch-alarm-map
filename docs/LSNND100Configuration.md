# LSNND100Configuration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of a device. | 
**name** | **str** | LSN device internal name. | 
**area** | **str** | LSN device area. | 
**point_type** | **str** | Point device type. | 
**supports_delayed_reporting** | **bool** | Delayed reporting support. | [optional] 
**walktest_category** | [**LSNWalktestCategoryProperty**](LSNWalktestCategoryProperty.md) |  | [optional] 
**reporting_number** | **int** | LSN device reporting number. | [optional] 

## Example

```python
from bosch_alarm_map.models.lsnnd100_configuration import LSNND100Configuration

# TODO update the JSON string below
json = "{}"
# create an instance of LSNND100Configuration from a JSON string
lsnnd100_configuration_instance = LSNND100Configuration.from_json(json)
# print the JSON string representation of the object
print(LSNND100Configuration.to_json())

# convert the object into a dict
lsnnd100_configuration_dict = lsnnd100_configuration_instance.to_dict()
# create an instance of LSNND100Configuration from a dict
lsnnd100_configuration_from_dict = LSNND100Configuration.from_dict(lsnnd100_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


